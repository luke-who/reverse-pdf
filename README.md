# python script to reverse the order of the PDF pages

## Script that can be used in Apple's Automator as an App(preferred)
As long as Apple continues to provide a System Python that has Cocoa bridge support, the Python script [reverse_apple.py](src/mac/reverse_apple.py) will rapidly reverse the pages in one or more PDF (without modifying the original) and write *file.pdf* out as *file_rev.pdf* in the original filesystem location. 
* Note for this script to work it requires ```pyobjc```, if not already installed:
```
pip3 install pyobjc
```
It can be incorporated into a single Automator Run Shell Script action saved as either a drag/drop application on the Desktop, or as a Quick Action, so you can select one or more PDF in the Finder and with a right-click, choose Quick Actions -> Reverse PDF Pages.
### Automator (Quick Action):
#### Set up
![Automator Quick Action](img/Automator%20Quick%20Action.png "Automator Quick Action")
#### Debugging: Note in macOS Monterey, you will encounter this error
![Automator Quick Action Error](img/shell_error.png "Automator Quick Action Error")
To fix this, create Symlink to python3(installed by homebrew):
```
sudo ln -s /opt/homebrew/opt/python@3.10/bin/python3 /usr/local/bin/python3
```
the symbolic link `/usr/local/bin/python3` will be created and the link/pointer look like this: `/usr/local/bin/python3 -> /opt/homebrew/opt/python@3.10/bin/python3`

To remove the Symlink in the future, just run:
```
sudo rm /usr/local/bin/python3
```
Make sure there's no bug left and save
![Save Quick Action](img/save_quick_action.png "Save Quick Action")
#### Usage in Finder
![Finder Quick Action](img/finder_quick_action_usage.png "Finder Quick Action")

### Automator (Application):

## Another script
* Note [reverse_pdf.py](src/reverse_pdf.py) script slightly reduces the size of the reversed pdf file compared to the original file size when tested.
### Usage
Package requirement:
```
pip install pdfrw
```
then run 
```
python3 reverse_pdf.py file.pdf
```
