#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input", help="Input pdf file")
parser.add_argument("output", help="Output pdf file")
parser.add_argument("-angle", default=90, help="Rotation angle")
parser.add_argument("-direction", default="counterclockwise", help="One of 'clockwise' or 'counterclockwise'")

args = parser.parse_args()
angle = args.angle
direction = args.direction

from pyPdf import PdfFileWriter, PdfFileReader
inFile = PdfFileReader(file(args.input, "rb"))
outFile = PdfFileWriter()
for i in range(0,inFile.getNumPages()):
    page = inFile.getPage(i)
    if direction == "counterclockwise":
        outFile.addPage(page.rotateCounterClockwise(args.angle))
    else:
        outFile.addPage(page.rotateClockwise(args.angle))
    outFile.write(file(args.output, "wb"))

