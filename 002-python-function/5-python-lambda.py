"""
Python Lambda Functions: Lambda Functions are anonymous functions means that the function is without a name.

SYNTAX: lambda arguments: expression
lambda: The keyword to define the function.
arguments: A comma-separated list of input parameters (like in a regular function).
expression: A single expression that is evaluated and returned.
"""
add = lambda a,b: a+b
even_odd_checker = lambda x: f"{x} is even number" if x % 2 == 0 else f"{x} is an odd number"

print(add(22,22))
print(even_odd_checker(2))
print(even_odd_checker(3))