import time
import random
from math import sqrt


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'на входе функции {func.__name__} - {args}\n {kwargs}')
        result = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__} - {result}')
        return result
    return wrapper


def time_run(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        duration = round(end - start, 2)
        print(f'Функция {func.__name__} работает {duration} сек.')
    return wrapper


def decor(func):
    def wrapper():
        print('BEFORE')
        func()
        print('AFTER')
    return wrapper


@decor
def proba():
    print('PROBA')

@time_run
def etalon(n, m, z):
    print('ETALON')
    time.sleep(n + m + z)

@in_out
def summatr(n, m):
    return n + m


if __name__ == '__main__':

    # proba()
    # etalon(3, 1, 1 )
    res = sqrt(summatr(random.randint(1,1000), random.randint(1,1000)) /.33)
    print(res)