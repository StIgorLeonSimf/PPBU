import time
import asyncio


async def f1(n: int):
    print(n * 10)
    await asyncio.sleep(3)
    print(f' Функция F1 закончила работу')


async def f2(n: int):
    print(n ** 2)
    await asyncio.sleep(2)
    print(f' Функция F2 закончила работу')


async def main():
    # f1(5)
    # f2(10)
    # task1 = asyncio.create_task(f1(5))
    # task2 = asyncio.create_task(f2(10))
    # await task1
    # await task2
    await asyncio.gather(f1(5), f2(10))


if __name__ == '__main__':
    start = time.time()
    # main()
    asyncio.run(main())
    stop = time.time()
    print(f'Время выполнения: {stop - start:.2f} сек.')
