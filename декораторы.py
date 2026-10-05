import time


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


if __name__ == '__main__':

    # proba()
    etalon(3, 1, 1 )
