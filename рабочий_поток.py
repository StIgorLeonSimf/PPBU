from threading import Thread
from time import sleep


class WorkThreading(Thread):
    def __init__(self, num, tab, val, dur):
        super().__init__()
        self.num = num
        self.tab = tab
        self.val = val
        self.dur = dur

    def run(self):
        print(f'Поток № {self.num} начал выполнение')
        for k in range(self.val):
            print(f'{self.tab} Поток № {self.num} => Действие {k + 1}')
            sleep(self.dur)
        print(f'Поток № {self.num} завершил работу')