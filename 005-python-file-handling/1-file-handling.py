"""
File handling refers to how Python allows you to create, read, write, and manipulate files on your system.

In most programs, you need to:
* Read data from files (e.g., input files, logs)
* Write data to files (e.g., reports, backups)
* Append new information
* Modify or delete file"""

"""
Opening a File: To open a file, we can use open() function, which requires file-path and mode as arguments:
Syntax: file = open('filename.txt', 'mode')
* filename.txt: name (or path) of the file to be opened.
* mode: mode in which you want to open the file (read, write, append, etc.).
Note: If you don't specify the mode, Python uses 'r' (read mode) by default.

Closing a File: The file.close() method closes the file and releases the system resources. If the file was opened in write or append mode, closing ensures that all changes are properly saved.
"""
