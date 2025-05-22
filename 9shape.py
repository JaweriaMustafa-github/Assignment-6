# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that 
# implements area().
from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a rectangle object
r1 = Rectangle(4, 6)
print("Area of rectangle : ", r1.area())