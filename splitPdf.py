#!/usr/local/bin/python3

#refs https://stackoverflow.com/questions/13345593/split-each-pdf-page-in-two

import sys
import argparse
from io import FileIO as file
import copy
import math
from PyPDF2 import PdfFileReader, PdfFileWriter

parser = argparse.ArgumentParser()

parser.add_argument("input", help="Input pdf file")
parser.add_argument("output", help="Output pdf file")

args = parser.parse_args()

def split_pages():

    src_f = file(args.input, 'r+b')
    dst_f = file(args.output, 'w+b')

    input = PdfFileReader(src_f)
    output = PdfFileWriter()

    for i in range(input.getNumPages()):
        p = input.getPage(i)
        q = copy.copy(p)
        q.mediaBox = copy.copy(p.mediaBox)

        x1, x2 = p.mediaBox.lowerLeft
        x3, x4 = p.mediaBox.upperRight

        x1, x2 = math.floor(x1), math.floor(x2)
        x3, x4 = math.floor(x3), math.floor(x4)
        x5, x6 = math.floor(x3/2), math.floor(x4/2)

        if x3 > x4:
            # horizontal
            p.mediaBox.upperRight = (x5, x4)
            p.mediaBox.lowerLeft = (x1, x2)

            q.mediaBox.upperRight = (x3, x4)
            q.mediaBox.lowerLeft = (x5, x2)
        else:
            # vertical
            p.mediaBox.upperRight = (x3, x4)
            p.mediaBox.lowerLeft = (x1, x6)

            q.mediaBox.upperRight = (x3, x6)
            q.mediaBox.lowerLeft = (x1, x2)


        p.artBox = p.mediaBox
        p.bleedBox = p.mediaBox
        p.cropBox = p.mediaBox

        q.artBox = q.mediaBox
        q.bleedBox = q.mediaBox
        q.cropBox = q.mediaBox

        output.insertPage(q,i)
        output.insertPage(p,i+(i+1)%2)

    output.write(dst_f)
    src_f.close()
    dst_f.close()

split_pages()