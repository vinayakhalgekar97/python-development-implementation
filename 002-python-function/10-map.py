"""
Python map() function

map() function in Python applies a given function to each element of an iterable (list, tuple, set, etc.) and returns a map object (iterator).

Syntax
    map(function, iterable,..)

Parameters:
function: The function to apply to every element of the iterable.
iterable: One or more iterable objects (list, tuple, etc.) whose elements will be processed.

Note: You can pass multiple iterables if the function accepts multiple arguments.
"""

"Converting map object to a list"
def double_the_value(value):
    return value ** 2

v1 = list(map(double_the_value, [1,2,4,5,6,7,8,9,10]))
print(v1)

"map() with lambda"
v2 = list(map(lambda x: x**2, [1,2,4,5,6,7,8,9,10]))
print(v2)

"map() with multiple iterables"
a1 = [1,2,3]
a2 = [2,3,4]

v3 = list(map(lambda x, y: x+y, a1,a2))
print(v3)

"Converting strings to Uppercase"
names = ['vinayak', 'virat', 'kohli']
v4 = list(map(lambda x: x.upper(), names))

print(v4)

"Extracting first character from strings"
v4 = list(map(lambda x: x[0].upper(), names))
print(v4)