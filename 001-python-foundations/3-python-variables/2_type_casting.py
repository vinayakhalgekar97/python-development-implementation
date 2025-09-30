# Type Casting in Python
# Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users.
# There can be two types of Type Casting in Python: Python Implicit Type Conversion and Python Explicit Type Conversion

# Python Implicit Type Conversion: In this, method, Python converts the datatype into another datatype automatically. Users don't have to involve in this process. 
a = 7
print(f"The value of a = {a} and type = {type(a)}")

b = 7.0
print(f"The value of a = {b} and type = {type(b)}")

print(f"a+b = {a+b} and type={type(a+b)}")
print(f"a-b = {a-b} and type={type(a-b)}")
print(f"a*b = {a*b} and type={type(a*b)}")
print(f"a/b = {a/b} and type={type(a/b)}")

# Explicit Type Conversion: In this method, Python needs user involvement to convert the variable data type into the required data type. 
# Mainly type casting can be done with these data type functions:
# int(): Python Int() function take float or string as an argument and returns int type object.
# float(): Python float() function take int or string as an argument and return float type object.
# str(): Python str() function takes float or int as an argument and returns string type object.

# Python Convert Int to Float
a = 5
n = float(a)
print(n, type(n))

# Python Convert Float to Int 
a = 5.4
n = int(a)
print(n, type(n))

# Python Convert int to String 
a = 5
n = str(a)
print(n, type(n))

# Python Convert String to float
a = "5.9"
n = float(a)
print(n, type(n))

# Note: Here, we are Converting string to int datatype in Python with int() function. If the given string is not number, then it will throw an error.
# name = "Vinayak" + 29
# print(name)

# Note: If we try to directly add an integer and a string, Python will throw an error because they are different data types. 
# Note: We should first convert the string into an integer and then add
a = '33'
b = 22 + int(a)
print(b)