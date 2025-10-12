# with open("./upload/writedemo.txt", "w", encoding="utf-8") as file:
#     file.write("Hello World") 

"Overwrite an existing file"
# with open("./upload/writedemo.txt", "w", encoding="utf-8") as file:
#     file.write("Hello, World\nVinayak Halgekar")

"Append to an existing file"
# with open("./upload/writedemo.txt", "a", encoding="utf-8") as file:
#     file.write("\nPython Programming\n")

"Create only if it does not exist"
# try:
#     with open("./upload/writedemo.txt", "x", encoding="utf-8") as file:
#         file.write("Python Programming\n")
# except FileExistsError as e:
#     print(f"ERROR: {e}")

"Writing multiple lines"
content = ["Vinayak\n", "Shashikant\n", "Halgekar\n"]
with open("./upload/writedemo.txt", "w", encoding="utf-8") as file:
    file.writelines(content)