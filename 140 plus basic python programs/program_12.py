# Write a Python Program to Check if a Number is Odd or Even.
try:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
except TypeError as e:
    print(f"ERROR: {e}")