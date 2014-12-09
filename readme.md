A short script to rotate pdf files.
Uses python with the argparse and pyPdf modules.

Most pdf viewers allow to rotate pdf files, but only until you close the file.
This script writes a new pdf file from an existing one, applying a rotation to every page of the original.

Usage :

rotatePdf.py [-h] [-angle ANGLE] [-direction DIRECTION] input output

positional arguments:
  input                 Input pdf file
  output                Output pdf file

optional arguments:
  -h, --help            show this help message and exit
  -angle ANGLE          Rotation angle
  -direction DIRECTION  One of 'clockwise' or 'counterclockwise'

