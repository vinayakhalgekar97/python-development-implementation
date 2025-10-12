"""
Reading a File in Python: Reading from a file in Python means accessing and retrieving contents of a file, whether it be text, binary data or formats like CSV and JSON.

Basic File Reading: Basic file reading involves opening a file, reading its contents, and closing it properly to free up system resources.
Steps:
* Open the file: open("filename", "mode") opens the file in a specified mode (e.g., read mode "r").
* Read content: Using read(), readline() or readlines() methods.
* Close the file: close() ensures system resources are released."""
# Open the file in read mode
# file = open("./upload/index.txt", "r")

# Read the entire content of the file
# content = file.read()
# print(content)

# Close the file
# file.close()

"Best Practice: Using with statement: Instead of manually closing files, we can use the with statement. It ensures the file is automatically closed when the block ends."
# with open("./upload/index.txt", "r") as file:
#     content = file.read()
#     print(content)

"""
Reading a File Line by Line 
We may want to read a file line by line, especially for large files where reading the entire content at once is not practical. It is done with following two methods:
* for line in file: Iterates over each line in the file.
* line.strip(): Removes any leading or trailing whitespace, including newline characters.
"""
"Example 1: Using a Loop to Read Line by Line"
# with open("./upload/index.txt", "r") as file:
#     for line in file:
#         print(line.strip())

"Example 2: Using readline()"
with open("./upload/index.txt", "r") as file:
    while True:
        content = file.readline()
        if not content:
            break
        print(content.strip())