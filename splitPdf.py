#!/usr/local/bin/python3

#refs https://stackoverflow.com/questions/13345593/split-each-pdf-page-in-two

import sys
import argparse
from io import FileIO as file
import copy
import math
from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser()

parser.add_argument("input", help="Input pdf file")
parser.add_argument("output", help="Output pdf file")

args = parser.parse_args()

def split_pages():

    src_f = file(args.input, 'r+b')
    dst_f = file(args.output, 'w+b')

    input = PdfReader(src_f)
    output = PdfWriter()

    for i in range(len(input.pages)):
        p = input.pages[i]
        q = copy.copy(p)
        q.mediabox = copy.copy(p.mediabox)

        x1, x2 = p.mediabox.lower_left
        x3, x4 = p.mediabox.upper_right

        x1, x2 = math.floor(x1), math.floor(x2)
        x3, x4 = math.floor(x3), math.floor(x4)
        x5, x6 = math.floor(x3/2), math.floor(x4/2)

        if x3 > x4:
            # horizontal
            p.mediabox.upper_right = (x5, x4)
            p.mediabox.lower_left = (x1, x2)

            q.mediabox.upper_right = (x3, x4)
            q.mediabox.lower_left = (x5, x2)
        else:
            # vertical
            p.mediabox.upper_right = (x3, x4)
            p.mediabox.lower_left = (x1, x6)

            q.mediabox.upper_right = (x3, x6)
            q.mediabox.lower_left = (x1, x2)


        p.artbox = p.mediabox
        p.bleedbox = p.mediabox
        p.cropbox = p.mediabox

        q.artbox = q.mediabox
        q.bleedbox = q.mediabox
        q.cropbox = q.mediabox

        output.insert_page(q,i)
        output.insert_page(p,i+(i+1)%2)

    with open(args.output, 'wb') as dst_f:
        output.write(dst_f)

split_pages()