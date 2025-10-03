"""
User-defined Exceptions in Python with Examples

User-defined exceptions are created by defining a new class that inherits from Python's built-in Exception class or one of its subclasses.

Steps to Create and Use User-Defined Exceptions:
Follow these steps to create and use User-Defined Exceptions in Python:
* Define a New Exception Class: Create a new class that inherits from Exception or any of its subclasses.
* Raise the Exception: Use the raise statement to raise the user-defined exception when a specific condition occurs.
* Handle the Exception: Use try-except blocks to handle the user-defined exception.
"""
class InvalidAgeError(Exception):
    def __init__(self, age, msg="Age must be between 0 and 120"):
        self.age = age 
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f'{self.age} -> {self.msg}'
    
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(age)
    else:
        return f"Your age: {age}"
    
try:
    set_age(123)
except Exception as e:
    print(e)
    print(e.args[0])

"""Real-World Example: Invalid Email Error"""
class InvalidEmailError(Exception):
    def __init__(self, email, msg="An email address must contain an '@' symbol."):
        self.email = email
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.email} -> {self.msg}"
    
def set_email(email):
    if "@" not in email:
        raise InvalidEmailError(email)
    else:
        return email
    
try:
    print(set_email("vinayak.halgekargmail.com"))
except Exception as e:
    print(e)