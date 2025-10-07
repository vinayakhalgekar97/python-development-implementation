"Inheritance in Python: Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class)."

"""
super() Function: super() function is used to call the parent class's methods. In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.
"""

class Animal:
    def __init__(self, name):
        self.name = name 

    def info(self):
        return f"Animal name: {self.name}"
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def details(self):
        return f"{self.name}, is a, {self.breed}"
    
dog = Dog("Tommy", "Golden Retriever")
print(dog.info())
print(dog.details())

"""
Explanation:
* class Animal: Defines the parent class.
* info(): Prints the name of the animal.
* class Dog(Animal): Defines Dog as a child of Animal class.
* d.info(): Calls parent method info() and d.sound(): Calls child method.
* The super() function is used inside __init__() method of Dog to call the constructor of Animal and initialize inherited attribute (name).
* This ensures that parent class functionality is reused without needing to rewrite the code in the child class.
"""

"Types of Python Inheritance"
"1. Single Inheritance: In single inheritance, a child class inherits from just one parent class."
class Person:
    def __init__(self, name):
        self.name = name 

class Employee(Person):
    def show_role(self):
        return f"{self.name} is an employee."
    
employee = Employee("Vinayak Halgekar")
print(employee.show_role())

"2. Multiple Inheritance: In multiple inheritance, a child class can inherit from more than one parent class."
class Person:
    def __init__(self, name):
        self.name = name 

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job): # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        return f"{self.name}, earns, {self.salary}"

employee1 = Employee("Vinayak Halgekar", 100000)
print(employee1.details())

"3. Multilevel Inheritance: In multilevel inheritance, a class is derived from another derived class (like a chain)."
class Person:
    def __init__(self, name):
        self.name = name 

class Employee(Person):
    def show_role(self):
        return f"{self.name} is an employee."
    
class Manager(Employee):  
    def department(self, dept):
        return f"{self.name}, manages, {dept}, department"

mgr = Manager("Joy")
print(mgr.show_role())
print(mgr.department("HR"))

"4. Hierarchical Inheritance: In hierarchical inheritance, multiple child classes inherit from the same parent class."
class Person:
    def __init__(self, name):
        self.name = name 

class Employee(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def role(self):
        return f"{self.name} is an employee."

class Intern(Person):
    def __init__(self, name):
        super().__init__(name)

    def role(self):
        return f"{self.name} is an intern."

emp = Employee("David")
print(emp.role())
intern = Intern("Eva")
print(intern.role())

"5. Hybrid Inheritance: Hybrid inheritance is a combination of more than one type of inheritance."
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee.__init__(self, name)
        Project.__init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Sophia", "AI Development")
print(lead.role())
print(lead.details())