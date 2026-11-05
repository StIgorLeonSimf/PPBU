from threading import Thread
import time


def f1(n: int):
    print(n * 10)
    time.sleep(3)
    print(f' Функция F1 закончила работу')


def f2(n: int):
    print(n ** 2)
    time.sleep(2)
    print(f' Функция F2 закончила работу')


if __name__ == '__main__':
    start = time.time()
    thread1 = Thread(target=f1, args=(50,))
    thread2 = Thread(target=f2, args=(6,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    stop = time.time()
    print(f'{stop - start:.2f} s')


