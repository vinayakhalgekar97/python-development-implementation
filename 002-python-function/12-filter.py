"""
filter() in python: filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition. It works by applying a function to each element and keeping only those for which function returns True.

Syntax
    filter(function, iterable)

Parameters:
function: tests each element and if return, True - Keep the element, if False - Discard the element
iterable: Any iterable (list, tuple, set, etc.).

Return Value: A filter object (an iterator), which can be converted into a list, tuple, set, etc.
"""

numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)