# Python Variables

# Assigning Values to Variables

# Basic Assignment
name = "Vinayak Shashikant Halgekar"
age = 27
city = "Bengaluru"

# Dynamic Typing
x = 3.0
x = "Now a string"
print(x, type(x))

# Multiple Assignments

# Assigning the Same Value
a = b = c = 100
print(a, b, c)

# Assigning Different Values
name, age, city = "Vinayak Shashikant Halgekar", 27, "Bengaluru"
print(name, age, city)

# Type Casting a Variable: Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

# Basic Casting Functions
# int() - Converts compatible values to an integer.
# float() - Transforms values into floating-point numbers.
# str() - Converts any data type into a string.
num1 = "10"
num2 = "10.234"
num3 = 300
print(int(num1))
print(float(num2))
print(str(num3))

# Getting the Type of Variable
# In Python, we can determine the type of a variable using the type() function. This built-in function returns the type of the object passed to it.
print(type(num1))
print(type(num2))
print(type(num3))