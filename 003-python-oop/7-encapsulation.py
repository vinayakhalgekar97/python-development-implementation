"Encapsulation in Python: Encapsulation means hiding internal details of a class and only exposing what’s necessary. It helps to protect important data from being changed directly and keeps the code secure and organized."

"""Access Specifiers: Access specifiers define how class members (variables and methods) can be accessed from outside the class. They help in implementing encapsulation by controlling the visibility of data. There are three types of access specifiers: Public, Private and Protected."""

"1. Public Members: Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name)."
class Employee:
    def __init__(self, name):
        self.name = name 

    def display_name(self):
        return self.name
    
employee = Employee("Vinayak Halgekar")
print(employee.name)

"2. Protected members: Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name)."
class Employee:
    def __init__(self, name, age):
        self.name = name # Public Attribute
        self._age = age # Protected Attribute

class SubEmployee(Employee):
    def display_age(self):
        return f"{self.name} is {self._age} years old."
    
sub_employee = SubEmployee("Vinayak Halgekar", 27)
print(sub_employee.display_age())

"""3. Private members: Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data.
In Python, private members are defined with a double underscore prefix (e.g., self.__salary). Python applies name mangling by internally renaming them (e.g., __salary becomes _ClassName__salary) to prevent direct access."""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name # Public Attribute
        self._age = age # Protected Attribute
        self.__salary = salary # Private Attribute

    def show_salary(self):
        return f"Salary: {self.__salary}"
    
employee = Employee("Vinayak", 27, 79000)
print(employee.show_salary()) # Accessing private correctly
# print(employee.__salary)  # Error: Not accessible directly

"""
Declaring Protected and Private Methods
In Python, you can control method access levels using naming conventions:
* Use a single underscore (_) before a method name to indicate it is protected meant to be used within class or its subclasses.
* Use a double underscore (__) to define a private method accessible only within class due to name mangling.
"""
class BankAccount:
    def __init__(self):
        self.balance = 1000

    def _show_balance(self):
        return f"Your balance is {self.balance}"
    
    def __update_balance(self, amount):
        self.balance += amount

    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
            return self._show_balance()
        else:
            return "Invalid Amount..."
        
amount = float(input("Enter the amount you want to deposit: "))
bank_account = BankAccount()
print(bank_account.deposit(amount))

"""
Getter and Setter Methods
In Python, getter and setter methods are used to access and modify private attributes safely. Instead of accessing private data directly, these methods provide controlled access, allowing you to:
* Read data using a getter method.
* Update data using a setter method with optional validation or restrictions.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            return self.__salary
        else:
            return "Invalid Salary Amount..."

employee = Employee("Vinayak Halgekar", 90000)
print(employee.get_salary()) # Access salary using getter
print(employee.set_salary(20000)) # Update salary using setter