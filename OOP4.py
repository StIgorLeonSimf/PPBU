from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calc_square(self):
        pass

    def display(self):
        print(self.name)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Прямоугольник')
        self.width = width
        self.height = height

    def calc_square(self):
        return self.width * self.height

    def display(self):
        super().display()
        print(f'Высота: {self.height} ед.\n'
              f'Ширина: {self.width} ед.\n'
              f'Площадь: {self.calc_square()} кв.ед.')

# print(__name__)
if __name__ == '__main__':
    r = Rectangle(4, 2)
    r.display()