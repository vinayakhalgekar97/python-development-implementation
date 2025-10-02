"""
Python Exception Handling

Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

Syntax and Usage
    try:
        # Code 
    except SomeException:
        # Code 
    else:
        # Code 
    finally:
        # Code 

try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs.
else: Executes only if no exception occurs in try.
finally: Runs regardless of what happens useful for cleanup tasks like closing files.
"""
try:
    n = 0
    result = 1 / n
except ZeroDivisionError as e:
    print(e)
else:
    print(f"Result: {result}")
finally:
    print("PROGRAM ENDED...")

"Python Catching Exceptions"
"1. Catching Specific Exceptions"
try: 
    n = 0
    result = 1 / n
except ZeroDivisionError:
    print("1. Catching Specific Exceptions: Zero has no inverse!")
except ValueError:
    print("1. Catching Specific Exceptions: Not Valid!")

"2. Catching Multiple Exceptions"
a = ["10", "twenty", 30]  
try:
    total = int(a[0]) + int(a[1])  
except (ValueError, TypeError) as e:
    print("2. Catching Multiple Exceptions", e)
except IndexError:
    print("2. Catching Multiple Exceptions: Index out of range.")

"3. Catch-All Handlers and Their Risks"
try:
    res = "100" / 20
except ArithmeticError:
    print("3. Catch-All Handlers and Their Risks: Arithmetic problem.")
except:
    print("3. Catch-All Handlers and Their Risks: Something went wrong!")

"Raise an Exception"
"""Basic Syntax: raise ExceptionType("Error message")"""
def set_age(age):
    if age < 0:
        raise ValueError("The AGE, you entered is invalid")
    else:
        return 0
    
try:
    set(-5)
except Exception as e:
    print(f"Raised an Exception: {e}")

