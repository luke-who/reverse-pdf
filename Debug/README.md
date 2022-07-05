# Shell error: Could not find shell usr/local/bin/python3

![Automator Quick Action Error](img/shell_error.png "Automator Quick Action Error")
To fix this, create a Symlink to python3(installed by homebrew):
```
sudo ln -s /opt/homebrew/opt/python@3.10/bin/python3 /usr/local/bin/python3
```
the symbolic link `/usr/local/bin/python3` will be created and the link/pointer look like this: `/usr/local/bin/python3 -> /opt/homebrew/opt/python@3.10/bin/python3`

To remove the Symlink in the future, just run:
```
sudo rm /usr/local/bin/python3
```
