from рабочий_поток import WorkThreading
from time import sleep

if __name__ == '__main__':
    print(f'Основной поток начал выполнение')

    thread1 = WorkThreading(1, '\t', 5, 4)
    thread2 = WorkThreading(2, '\t\t', 5, 2)
    thread3 = WorkThreading(3, '\t\t\t', 5, 3)

    thread1.start()
    thread2.start()
    thread3.start()

    for k in range (5):
        print(f'Основной поток Действие {k + 1}')
        sleep(1)
    print(f'Основной поток завершил выполнение')

    thread1.join()
    thread2.join()
    thread3.join()
