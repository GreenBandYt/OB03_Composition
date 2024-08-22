class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area_name(self):
        return "Круга"

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def area_name(self):
        return "Прямоугольника"
class Square(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width * self.width
    def area_name(self):
        return "Квадрата"

def printArea(shape):
    print(f'Площадь {shape.area_name()} равна {shape.area()}')


c = Circle(5)
printArea(c)

r = Rectangle(10, 5)
printArea(r)

s = Square(7)
printArea(s)
