class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2

def printArea(shape):
    print(f'Площадь {type(shape).__name__} равна {shape.area()}')


c = Circle(10)
r = Rectangle(10, 20)
sq = Square(7)


printArea(c)
printArea(r)
printArea(sq)
