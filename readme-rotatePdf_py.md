A short script to rotate pdf files. <br/>
Uses python with the argparse and pyPdf modules.

Most pdf viewers allow to rotate pdf files, but only until you close the file. <br/>
This script writes a new pdf file from an existing one, applying a rotation to every page of the original.

Usage :

```python rotatePdf.py [-h] [-angle ANGLE] [-direction DIRECTION] [-pages PAGES] input output```

positional arguments: <br/>
&emsp;**input** &nbsp;&nbsp; &emsp; Input pdf file <br/>
&emsp;**output**             &emsp; Output pdf file


optional arguments: <br/>
&emsp;**-h, --help** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; show this help message and exit <br/> 
&emsp;**-angle ANGLE** &emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;           Rotation angle in degrees. Default is _90_. <br/>
&emsp;**-direction DIRECTION** &emsp;                                 One of _clockwise_ or _counterclockwise_. Default is _counterclockwise_. <br/>
&emsp;**-pages** &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;                                               Python list (with enclosing _[]_ and _,_ separated) of page numbers, starting from 1. Default is _all_.&emsp;&emsp;Example:&emsp;_[1, 7, 8, 13]_

