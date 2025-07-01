#!/usr/local/bin/python3

import sys
import argparse
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser()
parser.add_argument("input1", help="Input pdf file 1")
parser.add_argument("input2", help="Input pdf file 2")
parser.add_argument("output", help="Output pdf file")
args = parser.parse_args()

def merge_alternate_pages():
    reader1 = PdfReader(args.input1)
    reader2 = PdfReader(args.input2)
    writer = PdfWriter()

    n = len(reader1.pages)
    if n != len(reader2.pages):
        print("Error: The two input PDFs must have the same number of pages.")
        sys.exit(1)

    # input1: 1,3,5,...  (0,2,4,...)
    # input2: -1,-3,-5,... (n-2, n-3, n-5,...)
    pages1 = [reader1.pages[i] for i in range(0, n, 2)]
    pages2 = [reader2.pages[i] for i in range(n-2, -1, -2)]

    # 交替合并
    for i in range(max(len(pages1), len(pages2))):
        if i < len(pages1):
            writer.add_page(pages1[i])
        if i < len(pages2):
            writer.add_page(pages2[i])

    with open(args.output, 'wb') as f:
        writer.write(f)

if __name__ == "__main__":
    merge_alternate_pages()
