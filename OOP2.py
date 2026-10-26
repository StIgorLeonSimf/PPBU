class PlayMixin:
    def play(self, channel=1):
        match channel:
            case 1: print('Играет "Beatles"')
            case 2: print('Играет "ABBA"')
            case 3: print('Новости')


class Car(PlayMixin):
    def __init__(self, make='Volga'):
        self.__make = make

    @property
    def make(self):
        return self.__make

    @staticmethod
    def ride():
        print('Едет по дороге')

    # def play(self):
    #     print('Играет "Beatles"')


class Boat(PlayMixin):
    @staticmethod
    def swim():
        print('Ходит по воде')

    # def play(self):
    #     print('Играет "ABBA"')


class Amphibian(Car, Boat):
    def display(self):
        print('Амфибия: ')


class Toyota(Car):
    # MAKE = 'Toyota'
    def __init__(self, model):
        super().__init__('Toyota')
        self.__model = model

    def __str__(self):
        # return f'Автомобиль {Toyota.MAKE} {self.__model} '
        return f'Автомобиль {self.make} {self.__model} '


class Card:
    amount = 1000000
    def __init__(self, numb, owner):
        self.numb = numb
        self.owner = owner

    def credit(self, sm):
        if Card.amount > sm:
            print('Получено', sm)
            Card.amount -= sm
            print('Остаток', Card.amount)
        else:
            print('Средств не достаточно')


car = Car()
car.ride()
car.play(2)
am = Amphibian()
am.display()
am.play(1)
am.ride()
am.swim()
t1 = Toyota('Corolla')
t1.play(3)
t1.ride()
print(t1)
employee = Card(12345,'Emp')
employee1 = Card(54321,'Emp1')

employee1.credit(900000)
employee.amount = 500000
employee.credit(200000)
