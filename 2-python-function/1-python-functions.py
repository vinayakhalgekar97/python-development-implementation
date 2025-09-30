"""Python Functions"""

"""Function Declaration

The syntax to declare a function is:
def function_name(parameters):
    # statement
    return expression
"""

"""
Defining a Function
    
    def function_name(parameters):
        # function body

Explanation:
def: Starts the function definition.
function_name: Name of the function.
parameters: Inputs passed to the function (inside ()), optional.
Indented code: The function body that runs when called.
"""

def add(a, b):
    c = a + b
    return c

"Calling a Function"
print(add(1, 2))

"""Function Arguments"""


"Types of Function Arguments"
"1. Default Arguments"
def minus(a, b=1000):
    return b - a

print(minus(4))
print(minus(4,100))

"2. Keyword Arguments"
def full_name(firstname, lastname):
    return f"My name is {firstname} {lastname}"

print(full_name(firstname="Vinayak", lastname="Halgekar"))

"3. Positional Arguments"
print(full_name("Vinayak", "Halgekar"))

"4. Arbitrary Arguments: " "REFER 2-python-args-kwargs.py"
