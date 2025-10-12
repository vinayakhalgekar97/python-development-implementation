# Write a Python Program to Check if a Number is Positive, Negative or Zero.
try:
    number = int(input("Enter a number: "))
    if number > 0:
        print(f"{number} is a positive number...")
    elif number == 0:
        print(f"{number} is a 0th value...")
    else:
        print(f"{number} is a negative number...")
except TypeError as e:
    print(f"ERROR: {e}")