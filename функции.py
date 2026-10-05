# def summator(a=10, b=4):
#     # print(a + b)
#     return a * b
#
#
# def printing(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     # return sum(args)


# n = 45
# cc = 'qwerty'
# n = summator(2, 3)
# # n = summator(2)
# print('функция', n)
# print(summator(2))  # позиционные аргументы
# print(summator())
# print(summator(b=8))  # Ключевые аргументы

# print(printing())
# print(printing(1, 3, nn=16, y=45))
# printing('Name1', 'Name2', 'Name3')
# printing('Name1', 'Name2')


def sumr(a, y):
    global x
    # z = 12
    x += 1
    print('x =', x, y, 'z =', z)
    return a


# z = 1000
# x = 5000
# res = sumr(10, 20)
# print(res)
# print('X =', x, 'Z =', z)

def is_eval(n: int) -> bool:
    """Определят четность числа.
    is_eval(2) -> True
    is_eval(3) -> False
    """
    return n % 2 == 0
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False


def choice_eval(x: int, y: int) -> None:
    """Выбирает четные числа из последовательности."""
    for i in range(x, y + 1):
        if is_eval(i):
            print(i, end=' ')


# choice_eval(100, 140)


# for n in range(100, 200):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=' ')


# nn = 100
# rez = nn
# res = is_eval(3)
# print(res)
# def num2(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)
#
#
# def num1(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)

# def num(x, n: int) -> None:
#     if n > x:
#         num(x, n - 1)
#     print(n)
#
# num(4,15)

"""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1
n! = n * (n-1)!

"""


def fact(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# print(fact(6))


def name(nm):
    cnt = 0
    def surname(snm):
        nonlocal cnt
        # global cnt
        cnt += 1
        print(cnt, nm, snm)

    return surname

cnt = 1000
sur = name('Mary')
sur1 = name('Dasha')
sur('Petrova')
sur('Андреева')
sur('Sidorova')
sur1('Андреева')
sur1('Sidorova')
