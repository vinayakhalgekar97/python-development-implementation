# Write a Python program to swap two variables without temp variable.
try:
    num1 = 2
    num2 = 3

    print(f"Two numbers before swapping: {num1}, {num2}")

    num1, num2 = num2, num1
    
    print(f"Two numbers after swapping: {num1}, {num2}")
except Exception as e:
    print(f"ERROR: {e}")