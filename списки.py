"""list"""
import copy

"""Список - упорядоченный набор объектов"""

"""     0   1   2   3   4  """
num = [22, 33, 44, 55, 99]
"""    -5  -4  -3  -2  -1   """

# print(num[0])
# print(num[2])
# print(num[1:-2])
# print(num[::2])
# print(num[2:])
# print(num[2::-1])
# print(num[::-1])
# num = [1, 2, [32, 4]]
# nn = num
# nn = num[:]
# nn = num.copy()
# nn = copy.deepcopy(num)
# num[1] = 3333
# num[-1][1] = 400
# print(num, id(num))
# print(nn, id(nn))
# print(nn is num)
x = 100
y = 100
# print( id(x) ,id(y))
num = [22, 100, 44, 100, 99]

print(num)
num.append(100)  # добавить в конец списка O(1) костантная
print(num)
num.insert(0, 300)  # O(n) линейная
print(num)
# num.extend([1, 2])
num += [100, 2]
# num = num + [1, 2]
print(num)

n = num.pop()
nn = num.pop(0)
print(n, nn)
print(num)
# while 100 in num:
#     num.remove(100)
# print(num)
print(num.index(100))
print(num.count(100))
# num.clear()
# print(num)
num = [22, 33, 44, 55, 99, 11]
nmn = [2, 3, 4, 5, 9, 1]
# for i in range(len(num)):
#     print(i, num[i], end='   ')
# print()
# cnt = 0
# for i in num:
#     print(cnt, i, end='   ')
#     cnt += 1
# print()
#
# for i in enumerate(num):
#     print(i[0], i[1],  end='   ')
# print()
#
# for r, i in enumerate(num):
#     print(r, i,  end='   ')
# print()
names = ['Dasha', 'Masha', 'Sasha', 'Glasha', 'Andryusha']
# names.reverse()
# names.sort(reverse=True)
# names.sort()
# for k, i in enumerate(names, 1):
#     print(f'{k}. {i}')
#
# for k, i,  in zip(names, num, nmn):
#     print(k, i)
#
# for k, i in zip(nmn, num):
#     print(i - k)

#
# arr = [0] * 10
# for i in range(len(arr)):
#     arr[i] = i + 1
# print(arr)
ls = []
for i in range(10):
    if i > 1:
        if (i + 1) % 2 == 0:
            ls.append(i + 1)
        else:
            ls.append(i)
print(ls)
print(5 if len(ls) < 7 else 125)
ls = [i + 1 if (i + 1) % 2 == 0 else i for i in range(10) if i > 1]
print(ls)
""" кортеж (Tuple) """
"""Кортеж- упорядоченный набор неизменяемых объектов"""

# tp = (22, 33, 44, 99)
# k, i, *z = 7, 5, 9, 10, 1, 32, 56, 100,
# print(k, i, z)
# tp = ('login', 'password')
# print(tp, id(tp))
# buf = list(tp)
# buf[-1] = 'new_password'
# tp = tuple(buf)
# print(tp, id(tp))
#
# """левый циклический сдвиг"""
# l = [22, 33, 44, 55, 99]
# temp = l[0]
# n = len(l)
# for i in range(n - 1):
#     l[i] = l[i + 1]
# l[-1] = temp
# print(l)
# temp = l.pop(0)
# l.append(temp)
# print(l)
#
# x = 10
# y = 15
# print(x, y)
# z = x
# x = y
# y = z
# print(x, y)
# x, y = y, x
# print(x, y)
names = ('Dasha', 'Masha', 'Sasha', 'Glasha', 'Andryusha')
age = (22, 33, 44, 55, 11)
persones = [('Dasha', 22), ('Masha', 33)]
for r, (n, a) in enumerate(zip(names, age), 1):
    print(f'{r}. {n} - {a}')