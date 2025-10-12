# Write a Python program to swap two variables.
try:
    num1 = 2
    num2 = 3

    print(f"Two numbers before swapping: {num1}, {num2}")

    temp = num2
    num2 = num1 
    num1 = temp

    print(f"Two numbers after swapping: {num1}, {num2}")
except Exception as e:
    print(f"ERROR: {e}")