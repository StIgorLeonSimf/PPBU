import math

from OOP4 import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Kруг')
        self.radius = radius

    def calc_square(self):
        return math.pi * self.radius ** 2

    def display(self):
        super().display()
        print(f'Радиус: {self.radius} ед.')
        print(f'Площадь: {self.calc_square():.2f} кв.ед.')


c = Circle(2)
c.display()
