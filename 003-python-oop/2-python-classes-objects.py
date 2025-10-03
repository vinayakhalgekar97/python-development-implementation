"""
1. Class
Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have. 

* Classes are created by keyword class.

* Attributes are the variables that belong to a class.

* Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute

* Using __init__() Function: In Python, class has __init__() function which automatically initializes object attributes when an object is created. The __init__() method is the constructor in Python.

* Self Parameter: self parameter is a reference to the current instance of class. It allows us to access the attributes and methods of the object.

* __str__() Method: __str__ method in Python allows us to define a custom string representation of an object. By default, when we print an object or convert it to a string using str(), Python uses the default implementation, which returns a string like <__main__.ClassName object at 0x00000123>.

===== Class and Instance Variables in Python =====
* Class Variables: These are variables that are shared across all instances of a class. It is defined at class level, outside any methods. All objects of class share same value for a class variable unless explicitly overridden in an object.
* Instance Variables: Variables that are unique to each instance (object) of a class. These are defined within __init__() method or other instance methods. Each object maintains its own copy of instance variables, independent of other objects.
"""
# Define a class
class Dog:
    species = "Canine" # Class Variable

    def __init__(self, name, age, color, height_cm):
        # Instance Variables
        self.name = name 
        self.age = age 
        self.color = color 
        self.height_cm = height_cm

    def __str__(self):
        return f"A Dog (Species: {self.species}) is created with name: {self.name}, age: {self.age}, color: {self.color} and height(cm): {self.height_cm}"

# Creating an object
dog1 = Dog("Tommy", 12, "White", 75)
dog2 = Dog("Tweety", 2, "Yellow", 15)
print(dog1)
print(dog2)

# Accessing instance variables
print("Accessing instance variables, Dog 1", dog1.name, dog1.age, dog1.color, dog1.height_cm)
print("Accessing instance variables, Dog 2", dog2.name, dog2.age, dog2.color, dog2.height_cm)

# Accessing class variable
print("Accessing class variable, Dog 1: ", dog1.species)
print("Accessing class variable, Dog 2: ", dog2.species)

# Updating instance variable
dog1.name = "Jerry"
print("Updating instance variable, Dog 1: ", dog1.name)
print("Updating instance variable, Dog 2: ", dog2.name)

# Updating class variable
Dog.species = "Feline"
print("Updating class variable, Dog 1: ", dog1.species)
print("Updating class variable, Dog 2: ", dog2.species)

"Additional Important Concepts in Python Classes and Objects"

"1. Getter and Setter Methods"