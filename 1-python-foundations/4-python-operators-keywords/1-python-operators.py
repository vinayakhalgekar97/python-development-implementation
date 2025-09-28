"""Python Operators"""

a = 10
b = 20

# Arithmetic Operators
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Modulo Division: {a%b}")
print(f"Exponentiation: {b**3}")
print(f"Floor Division: {a // b}")

# Comparison Operators
print(10 < 20)
print(10 > 20)
print(10 == 20)
print(10 <= 20)
print(10 >= 20)
print(10 != 20)

# Logical Operators: AND, OR, NOT
c = True
d = False
print(c and d)
print(c or d)
print(not c)

# Bitwise Operators: Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
# Bitwise Operators in Python are as follows:
#     Bitwise NOT
#     Bitwise Shift
#     Bitwise AND
#     Bitwise XOR
#     Bitwise OR

# Assignment Operators
a += 1
print(f"a = {a}")
a -= 2
print(f"a = {a}")
a *= 3
print(f"a = {a}")
a /= 4
print(f"a = {a}")
a %= 5
print(f"a = {a}")
a **= b
print(f"a = {a}")

# Identity Operators: is, is not
print(a is b)
print(a is not b)
x = 5
y = x
print(x is y)

# Membership Operators: in, not in
age = [27, 28, 30, 31, 32]
print(28 in age)
print(28 not in age)

# Ternary Operator
# Syntax :  [on_true] if [expression] else [on_false] 
age = int(input("Enter your age: "))
result = "You are eligible for driving" if age >= 18 else "You are not eligible for driving"
print(result)