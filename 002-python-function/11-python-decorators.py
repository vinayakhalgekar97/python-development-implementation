"""
Decorators in Python

In Python, decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.

A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.
"""

def decorator(function_name):
    def wrapper(*args, **kwargs):
        result = function_name(*args, **kwargs)
        return result
    return wrapper

@decorator
def greet():
    return "Hello World!!!!"

print(greet())

"""
Explanation of Parameters
decorator_name(func): This is the decorator function. It takes another function (func) as input.

**wrapper(*args, kwargs): A nested function that wraps func. *args collects positional arguments, **kwargs collects keyword arguments, so wrapper works with any function.

@decorator_name: Syntax sugar for add = decorator_name(add).
"""

"""
Higher-Order Functions: Higher-order functions are functions that take one or more functions as arguments, return a function as a result or do both.

Key Properties of Higher-Order Functions
Taking functions as arguments: A higher-order function can accept other functions as parameters.
Returning functions: A higher-order function can return a new function that can be called later.
"""