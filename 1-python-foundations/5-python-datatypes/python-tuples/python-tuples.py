'''Python Tuples'''

"""A tuple in Python is an immutable ordered collection of elements.

    Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
    Tuples can hold elements of different data types.
    The main characteristics of tuples are being ordered, heterogeneous and immutable."""

'''Creating a Tuple'''
names = ("Vinayak", "Virat", "Abhishek", "Surya", "Rohit", "Yash")
print(names)

even_numbers = [2, 4, 6]
print(tuple(even_numbers))

# print(tuple('Vinayak'))

# for name in names:
#     print(name)

"""Python Tuple Basic Operations.
Below are the Python tuple operations.
Accessing of Python Tuples
Concatenation of Tuples
Slicing of Tuple
Deleting a Tuple"""

"""Accessing of Tuples"""
print(names[0])
print(names[1])
print(names[-1])

# unpack values of Tuple
x, y, z = tuple(even_numbers)
print(x, y, z)

"""Concatenation of Tuples"""
result = names + tuple(even_numbers)
print(result)

"""Slicing of Tuple"""
print(result[2:6])
print(result[::-1]) # reverse a tuple

"""Tuple Unpacking with Asterisk (*)"""
"""In Python, the " * " operator can be used in tuple unpacking to grab multiple items into a list. This is useful when you want to extract just a few specific elements and collect the rest together."""
# a, *b, c = names
# print(a,b,c)
"""Explanation:
a gets the first item.
c gets the last item.
*b collects everything in between into a list."""