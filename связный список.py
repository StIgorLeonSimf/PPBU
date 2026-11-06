from typing import Optional


class Box:
    def __init__(self, name=None):
        self.name: str = name
        self.next: Optional[Box] = None  # next получает значение соответствующего
        # типа данных(Box)  либо None

    def __repr__(self):
        return f'{self.name} -> {self.next}'


class LinkedList:
    def __init__(self):
        self.head: Optional[Box] = None
        self.tail: Optional[Box] = None
        self.size: int = 0


    def append(self, name):
        new_box = Box(name)
        if self.head is None:
            self.head = new_box
            self.tail = new_box
            self.size += 1
            return

        self.tail.next = new_box
        # print(self.tail.next)
        self.tail = new_box
        self.size += 1
        return

    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            self.size -= 1
            return popped.name

    def in_box(self, name):
        current = self.head
        while current.next or current.name == name:
            if current.name == name:
                return True
            current = current.next
        return False

    def insert(self, name: str, ind: int) -> None:
        if ind < 0 or ind > self.size:
            raise IndexError('Индекс вне диапазона')
        new_box = Box(name)

        cnt = 0
        current = self.head
        prev = None
        while current.next:
            if cnt == ind:
                prev.next = new_box
                new_box.next = current
            cnt += 1
            prev = current
            current = current.next
        if self.size - 1 == ind:
            prev.next = new_box
            new_box.next = current

    def __repr__(self):
        return f'{self.head}'


llist = LinkedList()
llist.append('Барсик')
llist.append('Атос')
llist.append('Маркиза')
llist.append('Мурчик')
print(llist)
# print(llist.pop())
print(llist.in_box('Атос'))
llist.insert('Alisa', 2)
print(llist)

