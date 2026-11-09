"""Полное описание программы"""

# import seaborn
class Stack:
    limit = 10
    def __init__(self):
        self.stack = []
    def push(self, item):
        if len(self.stack) < Stack.limit:
            self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None


print(__doc__)