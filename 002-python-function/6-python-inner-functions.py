"Python Inner Functions"

"""
In Python, an inner function (also called a nested function) is a function defined inside another function. They are mainly used for:
Encapsulation: Hiding helper logic from external access.
Code Organization: Grouping related functionality for cleaner code.
Access to Outer Variables: Inner functions can use variables of the enclosing (outer) function.
Closures and Decorators: Supporting advanced features like closures (functions that remember values) and function decorators.
"""

"Scope of variables in inner functions: Inner functions follow Python’s LEGB rule (Local --> Enclosing --> Global --> Built-in). They can access outer function variables, but modifying them requires special keywords like nonlocal."

"Example 1: Local Variable Access"
def display_message_1():
    message = "Hello World!!!!"
    def display_message_2():
        return message
    return f"Example 1: Local Variable Access: {display_message_2()}"

print(display_message_1())

"Example 2: Modifying variables using nonlocal"
def count_number():
    i = 30
    def get_number():
        nonlocal i
        i = 40
        return f"Example 2: Modifying variables using nonlocal => {i}"
    return get_number()

print(count_number())

"Example 3: Closure in inner function"
def math_operation(a, b):
    def add():
        return a + b
    return add

print(math_operation(23,23)())

"""Real World Applications of Inner functions"""

"Example1: Encapsulation of helper functions"
def process_data(data):
    def clean_data():
        return [element.strip() for element in data]
    return clean_data

print(process_data([" Python ", "   Vinayak    "])())

"Example 2: Function wrapper and logging: REFER 11-python-decorators.py" 