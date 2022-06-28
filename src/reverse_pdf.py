#!/usr/bin/python

""" 
This script reverse the pages of a PDF document and save it to a new file.
Dependancy :
 - "PDFRW"
Usage :
- `pip install pdfrw`
- `python reverse.py file.pdf`
"""
from pdfrw import PdfReader, PdfWriter
import sys
import os

def reverse(pdf_file):
	writ = PdfWriter()
	read = PdfReader(pdf_file)

	for page in reversed(read.pages):
		writ.addpage(page)

	writ.write('reversed_%s' % pdf_file)



if __name__ == "__main__":
	if(len(sys.argv) == 1):
		print("Usage `python reverse.py mypdffile.pdf`")
		exit(0)
	pdf = sys.argv[1]
	if os.path.isfile(pdf): 
		reverse(pdf)
		print("Reversed file '%s'" % pdf)
	else:
		print("File not found")