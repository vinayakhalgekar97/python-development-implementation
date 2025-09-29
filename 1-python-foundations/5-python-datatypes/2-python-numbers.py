# 1. Numeric: int, float, complex
# int – Integers
a = 10 # integer
b = -25 # negative integer
c = 12345678901234567890  # arbitrarily large integer
print(a, type(a))
print(b, type(b))
print(c, type(c))

# float – Floating Point Numbers
x = 10.5
y = -3.14
z = 2.5e4
print(x, type(x))
print(y, type(y))
print(z, type(z))

# complex – Complex Numbers
c1 = 3 + 4j
c2 = 5j
print(type(c2))
print(c1.real)
print(c1.imag)
print(c1.conjugate())

# Python automatically detects number types; you don’t need to declare them.

# 2. Type Conversion (Casting)
# Note: We can't convert a complex data type number into int data type and float data type numbers.
# Note: We can't apply complex built-in functions on strings.
c3 = 4.5
print(int(c3))
c4 = 5
print(float(c4))
print(complex(c4))

# 9. Booleans as Numbers
# In Python, True is 1 and False is 0.
print(True + True)
print(False * 200)

# 10. Numeric Type Checking
print(isinstance(4, int))
print(isinstance(4.5, float))
print(isinstance(4+5j, complex))
print(isinstance(4, complex))