# Python String

# Creating a String
middle_name = ' Shashikant ' # single quote
name = "Vinayak Halgekar" # double quote

# Multi-line Strings
description = '''
I am Python Developer.
at MNC.'''
description = """
I am Python Developer.
at MNC."""

# Accessing characters in String
print(name[0])
print(name[2])
print(name[-1])
# Note: Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.

# String Slicing: The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
print(name[0:3]) 
print(name[0:])
print(name[::-1]) # reverse a string

# String Iteration
for name_char in name:
    print(name_char)

# String Immutability
# Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.
# name[0] = "R" # not allowed since it is Immutability

# Updating a String
# As strings are immutable, “updates” create new strings using slicing or methods such as replace().
print(name.replace(" ", " Shashikant "))

# Deleting a String
# In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.
# del name

# Common String Methods
# len(): returns the total number of characters in a string(including spaces and punctuation).
print(len(name))
print(name.upper())
print(name.lower())

print(middle_name)
print(middle_name.strip())

print(name.replace(" Shashikant ", " "))

# Concatenating and Repeating Strings

# Strings can be combined by using + operator.
company_name = "TATA" + " CONSULTANCY" + " SERVICES"
print(company_name)

# We can repeat a string multiple times using * operator.
print((name + " ") * 3)

# String Membership Testing
print("Vinayak" in name)
print("Vinayak" not in name)