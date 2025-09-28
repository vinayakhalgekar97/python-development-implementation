# Input and Output in Python

# Taking input in Python
# Python input() function is used to take input from the user. By default, it returns the user input in form of a string.

name = input("Enter your name: ")

# Printing Output using print() in Python
# print() function allows the programmer to display text, variables, expressions on the console.
print(f"Hello, {name}!!!")

# Printing Variables
# We can use the print() function to print single and multiple variables. We can print multiple variables by separating them with commas.
age = 27
city = "Madgoan"
print(name, age, city) # Printing multiple variables

# Take Multiple Input in Python
boys, girls = input("Enter the numbers of boys and girls: ").split()
print(boys, girls)
# Note: Python String split() method splits a string into a list of strings after breaking the given string by the specified separator.

# How to Change the Type of Input in Python
# By default, input() function returns the user input in form of a string. If any user wants to take user input as int or float, we need to typecast it.

# Print Numbers in Python
x = int(input("Enter a int number: "))
print(x)

# Print Float/Decimal Number in Python
y = float(input("Enter a float number: "))
print(y)

# Find DataType of Input in Python
# type() determines the type of the object in Python.
print(type(name))
print(type(x))
print(type(y))

d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}

print(type(d))
print(type(e))
print(type(f))