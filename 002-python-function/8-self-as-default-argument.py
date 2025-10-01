"""
Why Python Uses 'Self' as Default Argument

In Python, when defining methods inside a class, first parameter is always self. It is not a keyword, but a naming convention that plays a key role in Python’s object-oriented programming.

The self parameter represents instance of the class itself, allowing you to access and modify its attributes and methods.

"""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def display(self):
        return self.color, self.brand
    
car1 = Car("Toyota", "Red")
print(car1.display())

"""
Explanation:
self in __init__ assigns values (brand and model) to the specific instance (car1).
self in display refers to the same instance (car1) to access attributes.
Python automatically passes car1 as the first argument to display().
"""

"Circle Class for Area Calculation"
import math
class Circle:
    def __init__(self, r):
        self.r = r 

    def calculate_area(self):
        return math.pi * self.r ** 2
    
c1 = Circle(5)

print(f"The Area of Circle: {round(c1.calculate_area(), 2)}")

"""
Explanation:
self.r = r assigns 5 as the radius of the circle instance ins.
Inside area(), self.r ensures radius belongs to that specific circle (Python automatically provides self).
This way, even if we create multiple circles with different radii, each object uses its own value of self.r.
"""