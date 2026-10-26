import matplotlib.pyplot as plt


def add(v1, v2):
    x = v1[0] + v2[0]
    y = v1[1] + v2[1]
    return (x, y)


# v1 = (10, 5)
# v2 = (3, 15)
# v = add(v1, v2)
# print(v)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def display_add(self, other):
#         res = self + other
#         x1 = [0, self.x]
#         y1 = [0, self.y]
#         x2 = [0, other.x]
#         y2 = [0, other.y]
#         rx = [0, res.x]
#         ry = [0, res.y]
#
#         plt.plot(x1, y1, x2, y2, rx, ry,'-.g')
#         plt.show()
#
#
#     def __str__(self):
#         return f'V({self.x}, {self.y})'
#
#
# v1 = Vector(10, 5)
# v2 = Vector(3, 15)
# v3 = Vector(2, 4)
# print(v1)
# print(v2 + v1 + v3)
# v1.display_add(v2)

""" S O L I D """
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError('Объект должен быть строкой')
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError('Объект должен быть строкой')
        self.__name = new_age


    name =property(get_name, set_name)

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class University:
    def __init__(self, name_university):
        self.__name_university = name_university

    @property
    def name_university(self):
        return self.__name_university

class Student(Person, University):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        University.__init__(self, university)


    def __str__(self):
        return (f'{self.name} is {self.age} years old: '
                f'{self.name_university} ')




ps1= Person('Mary', 18)
ps2= Person('Pit', 19)
ps3= Person('Dasha', 19)
print(ps1.get_name())
ps1.set_name('Sasha')
print(ps1.name)
ps1.name = 'Mary'
print(ps1.name, ps1.age)
st1 = Student('Dasha', 18, university='MGU')
st2 = Student('Pit', 20, university='MAI')
print(st2)
print(ps2)
print(isinstance(st2, Student))
print(isinstance(st2, Person))
print(isinstance(ps1, Person))

