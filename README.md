## Environment

```
okcoder@MacBook-Pro rotatePDF % sw_vers
ProductName:            macOS
ProductVersion:         15.2
BuildVersion:           24C101
okcoder@MacBook-Pro ~ % python3 --version
Python 3.12.3
okcoder@MacBook-Pro ~ % pip3 --version
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
okcoder@MacBook-Pro ~ % pip3 show pypdf
Name: pypdf
Version: 4.3.1
Summary: A pure-python PDF library capable of splitting, merging, cropping, and transforming PDF files
Home-page:
Author:
Author-email: Mathieu Fenniak <biziqe@mathieu.fenniak.net>
License:
Location: /usr/local/lib/python3.12/site-packages
Requires:
Required-by:
okcoder@MacBook-Pro ~ %
```

## How to setup

```
brew install python
pip3 install pypdf
sudo mkdir -p /opt/pdf-tools
sudo cp rotatePdf.py /opt/pdf-tools/
sudo cp splitPdf.py /opt/pdf-tools/
sudo cp combinePdf.py /opt/pdf-tools/
sudo cp pdf-rotate-left /opt/pdf-tools/
sudo cp pdf-split /opt/pdf-tools/
sudo cp pdf-combine /opt/pdf-tools/
echo 'export PATH=$PATH:/opt/pdf-tools/'>>~/.zshrc
```

## Usage

```
pdf-rotate-left ${file}
pdf-split ${file}
```
