"*args and **kwargs in Python: In Python, *args and **kwargs are used to allow functions to accept an arbitrary number of arguments."

"""
Symbols for Handling Variable Arguments: 
    *args: Non-keyword (positional) arguments
    **kwargs: Keyword arguments
"""

"1. Non-Keyword Arguments (*args)"
"""The special syntax *args allows us to pass any number of positional (non-keyword) arguments to a function. These arguments are collected into a tuple, which means we can loop through them or use them with built-in functions."""
def add(*args):
    return args

print(add(1,2,3,4,5,6))

"2. Keyword Arguments (**kwargs)"
"""
The special syntax **kwargs allows us to pass any number of keyword arguments (arguments in the form key=value). These arguments are collected into a dictionary, where:
    Keys = argument names
    Values = argument values
"""
def details(**kwargs):
    return kwargs

print(details(fname="Vinayak", lname="Halgekar", age=27, profession="Software Developer", city="Madgoan"))

"Using both *args and **kwargs"
def student_info(*args, **kwargs):
    return f"""{args}\n{kwargs}"""

print(student_info(100,200,300, fname="Vinayak"))