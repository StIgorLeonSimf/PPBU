import multiprocessing
import time
import random


def producer(queue, n_items):
    """Производитель, генерирует числа"""
    for i in range(n_items):
        item = random.randint(1, 100)
        queue.put(item)
        print(f'Производитель создал: {item} ')
        time.sleep(random.uniform(.1, .5))
    queue.put(None)


def consumer(queue):
    """Потребитель"""
    while True:
        item = queue.get()
        if item is None:
            break
        result = item ** 2
        print(f'Получен -> {item}, изготовлен -> {result}')
        time.sleep(random.uniform(.2, .6))
    print('Пользователь работу закончил!')


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p_producer = multiprocessing.Process(target=producer, args=(queue, 10))
    p_consumer = multiprocessing.Process(target=consumer, args=(queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print('Главный процесс завершен')
