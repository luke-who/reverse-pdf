#!/usr/bin/python
# coding: utf-8

# write a PDF with its pages reversed into name_rev.pdf
# tested: Python 2.7.10 (10.13.6), Python 2.7.16 (10.14.6, 10.15.1)
# VikingOSX, 2019-01-19, Apple Support Communities, No warranties.

from Foundation import NSURL #this requires "pip3 install pyobjc"
from Quartz.PDFKit import PDFDocument
import os
import sys


def usage():
    print("Usage: {} file1.pdf … filen.pdf".format(__file__))


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    for apdf in sys.argv[1:]:
        pdf_file = os.path.expanduser(apdf)
        if not pdf_file.endswith('.pdf'):
            raise Exception('PDF file type required')

        # build output PDF filename
        bpath, ext = os.path.splitext(pdf_file)
        pdfrev = bpath + '_rev' + ext

        url = NSURL.fileURLWithPath_(pdf_file)
        pdf = PDFDocument.alloc().initWithURL_(url)
        pdf_out = PDFDocument.alloc().init()

        if pdf.pageCount() == 1:
            sys.exit('only one page found')

        # n is sequential page increase, r is the reversed page number
        for n, r in enumerate(reversed(range(0, pdf.pageCount()))):
            pdf_out.insertPage_atIndex_(pdf.pageAtIndex_(r), n)

        pdf_out.writeToFile_(pdfrev)


if __name__ == '__main__':
    sys.exit(main())