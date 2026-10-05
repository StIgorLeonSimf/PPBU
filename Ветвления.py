"""Операции сравнения"""
""" >, <, >=, <=, ==, != """

"""
(), not, and, or
True and True and True(False) ... = True(False)
False or False(True) ....         = False(True)
"""
#
# a = 46
# b = 36
# c = a > b
# print(c)
# z = a > b and a >= b and a != b
# z1 = a < b or a <= b or a == b
# print(z, z1)
# if a > b:
#     print('A > B')
#     print('A больше B')
#     print('A > B')
# else:
#     if a < b:
#         print('A < B')
#     else:
#         print('A == B')
#
#
# print('END')

# if a > b:
#     print('A > B')
# elif a < b:
#     print('A < B')
# else:
#     print('A == B')
#
# print('END')

# h = float(input('Введите время суток: '))
# if h >= 4 and h < 12:
#     print('Morning')
# elif 12 <= h < 17:
#     print('Day')
# elif h >= 17 and h < 24:
#     print('Evening')
# elif h >= 0 and h < 4 or h == 24:
#     print('Night')
# else:
#     print('Время введено не корректно!')

color = input('Цвет светофора: ')
match color:
    case 'red' | 'no':
        print('STOP')
    case 'green':
        print('GO')
    case 'yellow':
        print('Ready')
    case _:
        print('цвет', color)
