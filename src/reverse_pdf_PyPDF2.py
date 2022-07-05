from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
from tkinter import filedialog
import ntpath
import os
import subprocess, sys

output_pdf = PdfFileWriter()

# grab the location of the file path sent
def path_leaf(path):
    head, tail = ntpath.split(path)
    return head

# graphical file selection
def grab_file_path():
    # use dialog to select file
    file_dialog_window = tk.Tk()
    file_dialog_window.withdraw()  # hides the tk.TK() window
    # use dialog to select file
    grabbed_file_path = filedialog.askopenfilename()
    return grabbed_file_path


# file to be reversed
filePath = grab_file_path()

# open file and read
with open(filePath, 'rb') as readfile:
    input_pdf = PdfFileReader(readfile)

    # reverse order one page at time
    for page in reversed(input_pdf.pages):
        output_pdf.addPage(page)

    # graphical way to get where to select file starting at input file location
    dirOfFileToBeSaved = path_leaf(filePath)
    locationOfFileToBeSaved=filedialog.asksaveasfilename(initialdir=dirOfFileToBeSaved, initialfile='name of reversed file.pdf',title="Select or type file name and location", filetypes=[("pdf files", "*.pdf")])
    # write the file created
    with open(locationOfFileToBeSaved, "wb") as writefile:
        output_pdf.write(writefile)

print("Reversed file : " + locationOfFileToBeSaved)

## Uncomment below to open the file when done in the default application for the operating system.
# opener = "open" if sys.platform == "darwin" else "xdg-open"
# subprocess.call([opener, locationOfFileToBeSaved])

## Alternatively
# os.system('{} {}'.format("open" if sys.platform == "darwin" else "xdg-open",locationOfFileToBeSaved))

## Alternatively
# os.system(f'{"open" if sys.platform == "darwin" else "xdg-open"} {locationOfFileToBeSaved}')