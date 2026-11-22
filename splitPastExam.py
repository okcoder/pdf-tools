#!/usr/bin/env python3
"""Split past-exam spreads and move the first half after the questions."""

import argparse
from copy import copy
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
from pypdf.generic import DictionaryObject, NameObject, NumberObject, RectangleObject, TextStringObject


def positive_int(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("解答用紙のページ数は1以上にしてください")
    return number


def half_page(page, side):
    # Copy the page before changing its boxes so that the other half and the
    # original page do not inherit the crop.
    half = copy(page)
    x0, y0 = page.mediabox.lower_left
    x1, y1 = page.mediabox.upper_right
    if x1 - x0 >= y1 - y0:
        # Landscape spread: first=left, second=right.
        middle = (x0 + x1) / 2
        if side == "first":
            box = RectangleObject((x0, y0, middle, y1))
        else:
            box = RectangleObject((middle, y0, x1, y1))
    else:
        # Portrait spread: first=top, second=bottom.
        middle = (y0 + y1) / 2
        if side == "first":
            box = RectangleObject((x0, middle, x1, y1))
        else:
            box = RectangleObject((x0, y0, x1, middle))

    for name in ("mediabox", "cropbox", "artbox", "bleedbox", "trimbox"):
        setattr(half, name, RectangleObject(box))
    return half


def upright_page(page, rotate=False):
    # A PDF can store a page sideways and display it using /Rotate. Normalize
    # that rotation before cutting, so the aspect-ratio test uses visual size.
    upright = copy(page)
    if rotate:
        upright.rotate(270)
    if upright.rotation:
        upright.transfer_rotation_to_content()
    return upright


def add_labeled_page(writer, page, label, labels_enabled):
    writer.add_page(page)
    if not labels_enabled:
        return

    box = page.mediabox
    x0, y0 = float(box.left), float(box.bottom)
    x1, y1 = float(box.right), float(box.top)
    # Keep the box at the top, 10 pt from the visible left edge.
    rect = (min(x1, x0 + 10), max(y0, y1 - 40), min(x1, x0 + 218), y1)
    annotation = FreeText(
        text=label,
        rect=rect,
        font="Hiragino Sans GB",
        font_size="16pt",
        font_color="000000",
        border_color=None,
        background_color=None,
    )
    # FreeText's style string is not honored by every viewer. Provide a real
    # default appearance as well so the larger font is consistently visible.
    annotation[NameObject("/DA")] = TextStringObject("/Helv 20 Tf 0 0 0 rg")
    annotation[NameObject("/Q")] = NumberObject(0)  # Left-aligned text.
    annotation[NameObject("/DR")] = DictionaryObject({
        NameObject("/Font"): DictionaryObject({
            NameObject("/Helv"): DictionaryObject({
                NameObject("/Type"): NameObject("/Font"),
                NameObject("/Subtype"): NameObject("/Type1"),
                NameObject("/BaseFont"): NameObject("/Helvetica"),
            }),
        }),
    })
    writer.add_annotation(page_number=len(writer.pages) - 1, annotation=annotation)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="入力PDF")
    parser.add_argument("output", type=Path, help="出力PDF（入力とは別のファイル）")
    parser.add_argument(
        "-a", "--answer-pages", type=positive_int, default=1,
        help="末尾にある解答用紙のページ数（既定: 1）",
    )
    parser.add_argument(
        "--rotate", action="store_true",
        help="問題ページを反時計回りに90度回転してから分割する",
    )
    parser.add_argument(
        "--labels", action="store_true",
        help="分割後のページに順序確認用ラベルを付ける",
    )
    parser.add_argument(
        "--title", metavar="TEXT",
        help="全出力ページのラベルを置き換える文字列（指定時は --labels を無視）",
    )
    args = parser.parse_args()

    if args.input.resolve() == args.output.resolve():
        parser.error("入力PDFと出力PDFは別のファイルにしてください")

    reader = PdfReader(args.input)
    question_count = len(reader.pages) - args.answer_pages
    if question_count < 1:
        parser.error("解答用紙を除いて、問題ページが1ページ以上必要です")

    writer = PdfWriter()
    show_text = args.labels or args.title is not None

    def displayed_label(default_label):
        return args.title if args.title is not None else default_label

    first_page = upright_page(reader.pages[0], args.rotate)
    first_half = half_page(first_page, "first")
    horizontal = first_page.mediabox.width >= first_page.mediabox.height
    add_labeled_page(
        writer, half_page(first_page, "second"),
        displayed_label("1右" if horizontal else "1下"), show_text,
    )
    for number, page in enumerate(reader.pages[1:question_count], start=2):
        upright = upright_page(page, args.rotate)
        horizontal = upright.mediabox.width >= upright.mediabox.height
        add_labeled_page(
            writer, half_page(upright, "first"),
            displayed_label(f"{number}{'左' if horizontal else '上'}"), show_text,
        )
        add_labeled_page(
            writer, half_page(upright, "second"),
            displayed_label(f"{number}{'右' if horizontal else '下'}"), show_text,
        )
    horizontal = first_page.mediabox.width >= first_page.mediabox.height
    add_labeled_page(
        writer, first_half,
        displayed_label("1左" if horizontal else "1上"), show_text,
    )
    for number, page in enumerate(reader.pages[question_count:], start=1):
        label = "解答用紙" if args.answer_pages == 1 else f"解答用紙{number}"
        add_labeled_page(writer, page, displayed_label(label), show_text)

    with args.output.open("wb") as destination:
        writer.write(destination)


if __name__ == "__main__":
    main()
