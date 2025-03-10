from math  import *

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def calc_circle_area(self):
        return pi * self.radius**2

    def calc_circle_perimeter(self):
        return 2*pi*self.radius

inpt = float(input("enter the radius of the circle: "))
circle = Circle(inpt)

area=circle.calc_circle_area()
permiter=circle.calc_circle_perimeter()

print(area)
print(permiter)
