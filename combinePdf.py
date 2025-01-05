#!/usr/local/bin/python3
import sys
import argparse
from io import FileIO as file

parser = argparse.ArgumentParser()

parser.add_argument("output", help="Output pdf file")
parser.add_argument("pdfs", nargs='+', help="Input pdf file")

args = parser.parse_args()

from pypdf import PdfMerger
merger = PdfMerger()

for pdf in args.pdfs:
    print(pdf)
    merger.append(pdf)

print("write to " + args.output)
merger.write(args.output)
merger.close()
