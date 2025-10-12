# Write a Python program to do arithmetical operations addition and division.
error = False

def add(num1, num2):
    return num1 + num2

def div(num1, num2):
    return num1 / num2

try:
    operation = input("Select an operation - '+' for addition or '/' for division: ")
    if operation == "+":
        num1 = input("Enter first number: ")
        num2 = int(input("Enter second number: "))
        result = add(num1=num1, num2=num2)
    elif operation == "/":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = round(div(num1=num1, num2=num2), 2)
    else:
        error = True
except (ZeroDivisionError, TypeError) as e:
    print(f"ERROR: {e}")
else:
    if not error:
        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Please select valid operation")
finally:
    print("ARITHMETIC OPERATIONS COMPLETED...")