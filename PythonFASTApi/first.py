# pip install fastapi uvicorn
# uvicorn app.main:app --reload
# uvicorn app.main:app --reload --port8001
import asyncio
from sqlalchemy import create_engine

import multiprocessing
import time
import random


def producer(queue, n_items):
    for i in range(n_items):
        item = random.randint(1, 100)
        queue.put(item)
        print(f'Производитель создал: {item} ')
        time.sleep(random.uniform(0.1, .5))
    queue.put(None)


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        result = item ** 2
        print(f'Получено: {item} -> {result}')
        time.sleep(random.uniform(0.2, .6))
    print('Пользователь завершил работу')


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p_producer = multiprocessing.Process(target=producer, args=(queue, 10))
    p_consumer = multiprocessing.Process(target=consumer, args=(queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()




# async def func1():
#     print("func1")
#     await asyncio.sleep(1)
#     print("func1 completed")
#
# async def func2():
#     print("func2")
#     await asyncio.sleep(1)
#     print("func2 completed")
#
#
# async def main():
#     # task1 = asyncio.create_task(func1())
#     # task2 = asyncio.create_task(func2())
#     # await task1
#     # await task2
#     await asyncio.gather(func1(), func2())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())