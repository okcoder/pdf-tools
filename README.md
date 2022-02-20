

## Environment
```
okcoder@MacBook-Pro rotatePDF % sw_vers
ProductName:	macOS
ProductVersion:	11.2.3
BuildVersion:	20D91
okcoder@MacBook-Pro ~ % python3 --version
Python 3.9.4
okcoder@MacBook-Pro ~ % pip3 --version
pip 21.0.1 from /usr/local/lib/python3.9/site-packages/pip (python 3.9)
okcoder@MacBook-Pro ~ % pip3 show PyPDF2
Name: PyPDF2
Version: 1.26.0
Summary: PDF toolkit
Home-page: http://mstamy2.github.com/PyPDF2
Author: Mathieu Fenniak
Author-email: biziqe@mathieu.fenniak.net
License: UNKNOWN
Location: /usr/local/lib/python3.9/site-packages
Requires: 
Required-by: 
okcoder@MacBook-Pro ~ % 
```

## How to setup

```
brew install python
pip3 install PyPDF2
sudo mkdir -p /opt/pdf-tools
sudo cp rotatePdf.py /opt/pdf-tools/
sudo cp splitPdf.py /opt/pdf-tools/
sudo cp pdf-rotate-left /opt/pdf-tools/
sudo cp pdf-split /opt/pdf-tools/
echo 'export PATH=$PATH:/opt/pdf-tools/'>>~/.zshrc
```

## Usage
```
pdf-rotate-left ${file}
pdf-split ${file}
```
