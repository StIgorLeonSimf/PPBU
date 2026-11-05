from models import Card
from threads import Transaction

print(f'Начальный баланс карты {Card.balance}')
card1 = Card('1234', 'Иван Иванов')
card2 = Card('9876', 'Даша Дашина')

trans1 = Transaction(550000, card1)
trans2 = Transaction(550000, card2)

trans1.start()
trans2.start()
trans1.join()
trans2.join()

print(f'Конечный баланс: {Card.balance}')
print(f'Число операций: {trans1.card.count + trans2.card.count}\n ')
print(f'Дисбаланс: {1000000 - trans1.card.count - trans2.card.count}')