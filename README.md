# python script to reverse the order of the PDF pages

## Script that can be used in Apple's Automator as an App(preferred)
As long as Apple continues to provide a System Python that has Cocoa bridge support, the Python script [reverse_apple.py](reverse_apple.py) will rapidly reverse the pages in one or more PDF (without modifying the original) and write *file.pdf* out as *file_rev.pdf* in the original filesystem location. It can be incorporated into a single Automator Run Shell Script action saved as either a drag/drop application on the Desktop, or as a Quick Action, so you can select one or more PDF in the Finder and with a right-click, choose Quick Actions -> Reverse PDF Pages.

## Another script
Note [reverse_pdf.py](reverse_pdf.py) script slightly reduces the size of the reversed pdf file compared to the original file size when tested.
