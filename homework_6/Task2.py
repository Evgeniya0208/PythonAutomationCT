class Rectangle:

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        return round((self.length * self.width), 2)

    def calculate_perimeter(self):
        return round(2 * (self.length + self.width), 2)

my_rectangle = Rectangle(15.2, 17.4)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())