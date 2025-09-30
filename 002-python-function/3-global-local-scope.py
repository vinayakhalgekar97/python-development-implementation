"Global and Local Variables in Python"

"Local Variables: Local variables are created inside a function and exist only during its execution. They cannot be accessed from outside the function."
def count():
    i = 10
    return f"Inside function: {i*2}"

print(count())

"Global Variables: Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions."
i = 200
def count_again():
    i = 100
    return f"Inside function again: {i*5}"

print(count_again())
print("Outside function:", i)

"If a variable is defined both globally and locally with the same name, the local variable shadows the global variable inside the function. Changes to the local variable do not affect the global variable unless you explicitly declare the variable as global."

"""
Modifying Global Variables Inside a Function

By default, one cannot modify a global variable inside a function without declaring it as global. If you try, Python will raise an error because it treats variable as local. To modify a global variable use the global keyword.
"""
j = 1000
def modify_global():
    global i
    i = 2000
    return f"INSIDE FUNCTION: {i}"

print(modify_global())
print("Outside function:", i)