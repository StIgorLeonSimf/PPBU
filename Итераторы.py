ls = [22, 33, 44, 55]
itr = iter(ls)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# for i in itr:
#     print(i)

class Car:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def __iter__(self):
        self.cnt = 0
        return self

    def __next__(self):
        obj = (self.name, self.price, self.color)
        if self.cnt < len(obj):
            res = obj[self.cnt]
            self.cnt += 1
            return res
        raise StopIteration ('Объектов больше нет' )



car1 = ['Volga', 20000, 'black']
car2 = Car("UAZ", 15000, 'green')
# cars = [car1, car2]
# for car in cars:
#     for item in car:
#         print(item, end=', ')
#     print()
itr = iter(car2)
print(next(itr), car2.cnt)
print(next(itr), car2.cnt)
print(next(itr), car2.cnt)
print(next(itr), car2.cnt)