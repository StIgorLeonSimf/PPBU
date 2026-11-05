class Card:
    balance: float = 1000000
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self._count = 0

    @property
    def count(self) -> int:
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @staticmethod
    def debit():
        Card.balance += 1

    def credit(self):
        if Card.balance > 0:
            Card.balance -= 1
            self.count += 1
            return True
        else:
            print(f'На карте № {self.number} не достаточно средств')

