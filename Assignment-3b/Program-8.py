from abc import ABC, abstractmethod
import math

class IShape(ABC):
    @abstractmethod
    def calculateArea(self):
        pass

    @abstractmethod
    def calculatePerimeter(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width

    def calculatePerimeter(self):
        return 2 * (self.length + self.width)


class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius * self.radius

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    rect = Rectangle(length=10, width=5)
    print("Rectangle:")
    print("Area:", rect.calculateArea())
    print("Perimeter:", rect.calculatePerimeter())

    print()

    circle = Circle(radius=7)
    print("Circle:")
    print("Area:", circle.calculateArea())
    print("Perimeter:", circle.calculatePerimeter())
