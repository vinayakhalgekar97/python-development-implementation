"""
Polymorphism in Python: Polymorphism means "many forms". It refers to the ability of an entity (like a function or object) to perform different actions based on the context.
Technically, in Python, polymorphism allows same method, function or operator to behave differently depending on object it is working with. This makes code more flexible and reusable.

Types of Polymorphism: Polymorphism in Python refers to ability of the same method or operation to behave differently based on object or context. It mainly includes compile-time and runtime polymorphism.

Compile-time polymorphism means deciding which method or operation to run during compilation, usually through method or operator overloading. Compile-time polymorphism: Achieved via method overloading (not directly supported in Python, but can be simulated).

Runtime polymorphism means that the behavior of a method is decided while program is running, based on the object calling it.
In Python, this happens through Method Overriding a child class provides its own version of a method already defined in the parent class. Since Python is dynamic, it supports this, allowing same method call to behave differently for different object types.
"""

"Compile-time polymorphism"
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()

print(c.add(1,2,3,4))
print(c.add(1,2,3,4,5,6,7,8,9,10))

"Runtime Polymorphism"
class Animal:
    def speak(self):
        return "Some Sound"
    
class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())

"Polymorphism in Built-in Functions: Python’s built-in functions like len() and max() are polymorphic they work with different data types and return results based on type of object passed."
print(len("Hello"))
print(len([1,2,3,4,5,6,7,8,9,10]))

print(max(1,2,3,4,5,6))
print(max("a", "b", "c"))

"Polymorphism in Functions: In Python, polymorphism lets functions accept different object types as long as they support needed behavior. Using duck typing, Python focuses on whether an object has right method not its type allowing flexible and reusable code."
class Pen:
    def use(self):
        return "Writing"

class Eraser:
    def use(self):
        return "Erasing"

def perform_task(tool):
    print(tool.use())

perform_task(Pen())
perform_task(Eraser())

"""Polymorphism in Operators: In Python, same operator (+) can perform different tasks depending on operand types. This is known as operator overloading. This flexibility is a key aspect of polymorphism in Python. """
print(5 + 10)  # Integer addition
print("Hello " + "World!")  # String concatenation
print([1, 2] + [3, 4])  # List concatenation