from typing import List

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


    def __str__(self):
        return f'{self.__name} - {self.__age}'

    def __repr__(self):
        return f'{self.__name}, {self.__age}'


class Flat:
    def __init__(self, number):
        self.__number = number
        self.__persons: List[Person] = []

    @property
    def number(self):
        return self.__number

    @property
    def persons(self):
        return self.__persons

    def add_person(self, *persons):
        for person in persons:
            if not isinstance(person, Person):
                raise TypeError("Объект должен быть класса Person")
            self.__persons.append(person)

    def display(self):
        mx = len(max(self.__persons, key=lambda person: len(person.name)).name)
        print(self)
        for i, person in enumerate(self.__persons, 1):
            print(f'\t\t\t{i}. {person.name:{mx}} - {person.age}')

    def __str__(self):
        return f'\n\t\tКвартира № {self.__number}'


class Floor:
    def __init__(self, numb):
        self.__numb = numb
        self.__flats: List[Flat] = []

    @property
    def numb(self):
        return self.__numb

    @property
    def flats(self):
        return self.__flats

    def add_flat(self, *flats):
        for flat in flats:
            if not isinstance(flat, Flat):
                raise TypeError("Объект должен быть класса Flat")
            self.__flats.append(flat)

    def display(self):
        print(self)
        i = 1
        for flat in self.flats:
            print(flat)
            for person in flat.persons:
                print(f'\t\t\t{i}. {person.name:20} - {person.age}')
                i += 1

    def __str__(self):
        return  f'\tЭтаж № {self.__numb}'





p1 = Person('Klava Koka', 30)
p2 = Person('John Lenon', 34)
p3 = Person('Ibragim ibn Huttab', 50)
p4 = Person('Stas Michailov', 40)

fl44 = Flat(44)
fl45 = Flat(45)

f4 = Floor(4)
f4.add_flat(fl44, fl45)


fl44.add_person(p1, p4)
fl45.add_person(p2, p3)
f4.display()
