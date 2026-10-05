from functools import reduce

l = [22, 33, 44]


#
#
def gen():  # функция генератор
    i = 0
    while i < 3:
        i += 1
        yield i


#
#
# res = gen()
# print(res)
# print('1', next(res))
# print(2, next(res))
# print('3', next(res))
# for i in res:
#     print(i)
#
# for i in res:
#     print(i)
res = (i for i in gen())  # выражение генератор


# print(list(res))
#
def power(n):
    return n * n


l = [22, 33, 44]
l1 = [2, 3, 4]
# res = map(str, l)
# res = map(power, l)
# res = map(lambda n: n * n, l)
res = map(lambda n, m: n - m, l, l1)
# res = map(lambda n, m: n > m, l, l1)
print(list(res))
# res1 = (i * i for i in l)
# print(list(res1))

res = filter(lambda n: n % 2 != 0, l)
print(list(res))

city = ('У', 'ф', 'а', '-', 4, 5)
# print(''.join(city))
def prim(x, y):
    print(x, y)
    print(str(x) + str(y))
    return str(x) + str(y)

res = reduce(lambda x, y: str(y) + str(x), city)
# res = reduce(prim, city)
print(res)

print(sum(l))
l = range(1, 6)
res = reduce(lambda x, y: x * y, l)
print(res)