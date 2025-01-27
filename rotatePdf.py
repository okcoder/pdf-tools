#!/usr/local/bin/python3
import sys
import argparse
from io import FileIO as file

parser = argparse.ArgumentParser()

parser.add_argument("input", help="Input pdf file")
parser.add_argument("output", help="Output pdf file")
parser.add_argument("-angle", default=90, help="Rotation angle")
parser.add_argument("-direction", default="counterclockwise", help="One of 'clockwise' or 'counterclockwise'")
parser.add_argument("-pages", default="all", help="Python list (with enclosing [] and comma separated) of page numbers, starting from 1.\n\tExample: [1, 7, 8, 13]")

args = parser.parse_args()
angle = args.angle
direction = args.direction
PAGES = False
if args.pages != "all":
    PAGES = True
    pages = sorted(eval(args.pages))

from pypdf import PdfReader, PdfWriter
inFile = PdfReader(file(args.input, "rb"))
outFile = PdfWriter()

if PAGES:
    nextPage = pages.pop(0)

for i in range(0,inFile.get_num_pages()):
    page = inFile.get_page(i)
    if PAGES and (nextPage is None or i+1 != nextPage):
        outFile.add_page(page)
    else:
        if direction == "counterclockwise":
            outFile.add_page(page.rotate(360-args.angle))
        else:
            outFile.add_page(page.rotate(args.angle))
        if PAGES and len(pages) > 0:
            nextPage = pages.pop(0)
    outFile.write(file(args.output, "wb"))
