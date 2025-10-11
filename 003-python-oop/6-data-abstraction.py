"""
Data Abstraction in Python: Data abstraction means showing only the essential features and hiding the complex internal details. 

Technically, in Python abstraction is used to hide the implementation details from the user and expose only necessary parts, making the code simpler and easier to interact with.

Abstract Base Class: In Python, an Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. It cannot be instantiated directly and serves as a blueprint for other classes.

Abstract classes are created using abc module and @abstractmethod decorator, allowing developers to enforce method implementation in subclasses while hiding complex internal logic.
"""
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello"
    
class Kannada(Greet):
    def say_hello(self):
        return "Namaskara"
    
english = English()
print(english.say_hello())

kannada = Kannada()
print(kannada.say_hello())

"""
Explanation:
* Greet is an abstract class with a method say_hello() that has no implementation.
* English implements this method and returns a greeting.
* Kannada implements this method and returns a greeting.
* This keeps structure fixed while letting subclasses define their own behavior.
"""

"""
Components of Abstraction: Abstraction in Python is made up of key components like abstract methods, concrete methods, abstract properties and class instantiation rules.

Abstract Method: Abstract methods are method declarations without a body defined inside an abstract class. They act as placeholders that force subclasses to provide their own specific implementation, ensuring consistent structure across derived classes.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here
"""
Concrete Method: Concrete methods are fully implemented methods within an abstract class. Subclasses can inherit and use them directly, promoting code reuse without needing to redefine common functionality.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, to be implemented by subclasses

    def move(self):
        return "Moving"  # Concrete method with implementation

"Abstract Properties: Abstract properties work like abstract methods but are used for properties. These properties are declared with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties."
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass  # Abstract property, must be implemented by subclasses

class Dog(Animal):
    @property
    def species(self):
        return "Canine"

# Instantiate the concrete subclass
dog = Dog()
print(dog.species)

"Abstract Class Instantiation: Abstract classes cannot be instantiated directly. This is because they contain one or more abstract methods or properties that lack implementations. Attempting to instantiate an abstract class results in a TypeError."