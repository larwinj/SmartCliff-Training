import math

class Shape:
    def __init__(self, name):
        self.name = name


class Rectangle(Shape):
    def __init__(self):
        super().__init__("Rectangle")
        self.length = 0
        self.breadth = 0

    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

    def getPerimeter(self):
        return 2 * (self.length + self.breadth)


class Triangle(Shape):
    def __init__(self):
        super().__init__("Triangle")
        self.a, self.b, self.c = 3, 4, 5

    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def getPerimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    rect = Rectangle()
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    rect.setDim(length, breadth)
    print(f"\n{rect.name}:")
    print("Area:", rect.getArea())
    print("Perimeter:", rect.getPerimeter())

    tri = Triangle()
    print(f"\n{tri.name} (with sides 3, 4, 5):")
    print("Area:", tri.getArea())
    print("Perimeter:", tri.getPerimeter())
