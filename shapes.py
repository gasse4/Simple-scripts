import math

class shapes:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class circle(shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class square(shapes):
    def __init__(self, height):
        self.height = height

    def area(self):
        return self.height**2

    def perimeter(self):
        return self.height * 4

radius = float(input("Enter the radius of the circle: "))
Circle = circle(radius)

print(f"The area of the circle is: {Circle.area()}")
print(f"The perimeter of the circle is: {Circle.perimeter()}")

height = float(input("Enter the height of the square: "))
Square = square(height)

print(f"The area of the square is: {Square.area()}")
print(f"The perimeter of the square is: {Square.perimeter()}")
