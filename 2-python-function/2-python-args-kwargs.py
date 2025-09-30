"*args and **kwargs in Python: In Python, *args and **kwargs are used to allow functions to accept an arbitrary number of arguments."

"""
Symbols for Handling Variable Arguments: 
    *args: Non-keyword (positional) arguments
    **kwargs: Keyword arguments
"""

"1. Non-Keyword Arguments (*args)"
"""The special syntax *args allows us to pass any number of positional (non-keyword) arguments to a function. These arguments are collected into a tuple, which means we can loop through them or use them with built-in functions."""
def sum(*args):
    print(sum(args))

sum(1,2,3,4,5,6)