"""Match     match = re.search(regex, string)"""

from string import digits, ascii_letters
import re
import random

res = re.match(r'AV', 'AV_Avia')  # совпадение в начале строки
print(res)
"""fullmatch - обеспечивает полное совпадение строки"""
res = re.fullmatch(r'AV', 'AV_Avia')  # совпадение в начале строки
print(res)
res = re.search(r'AV', 'regAV_AviaAV/AV')  # совпадение в строке
print(res)
res = re.findall(r'AV', 'regAV_AviaAV/AV')
print(res)
res = re.finditer(r'AV', 'regAV_AviaAV/AV')
print(next(res))
res = re.sub(r'что меняем', 'на что меняем', 'где меняем')
res = re.split(r'p', 'PerspectivPe', maxsplit=1, flags=re.IGNORECASE)
print(res)
pattern = re.compile(r'AV')
res = pattern.findall('regAV_AviaAV/AV')
print(res)


# """СПЕЦСИМВОЛЫ
# # \d - любая цифра
# # \D - любое не числовое значение
# #
# # \s - символы пробелов
# # \S - все кроме пробела
# #
# # \w - буква, цифра и нижнее подчеркивание
# # \W - все кроме буквы, цифры и нижнего подчеркивания
#
# . - любой символ кроме переноса строки
# ^ - начало строки
# $ - конец строки
# [abc] - любой символ в скобках
# [^abc] - любой символ кроме тех что в скобках
# a|b - a или b
# (ab) - определяем одним элементом
# # \bслово\b
# """
# result = re.findall(r'[^abc]', 'aligol6573@gmail.com')
# print(result)
#
# """ КВАНТИФИКАТОРЫ
# regex+ - встречается один или более раз
# regex* - встречается ноль или более раз
# regex? - встречается ноль или один раз
# regex{n} - встречается n раз
# regex{n, } - встречается n или более раз
# regex{n, m} - встречается от n до m раз
# """
# regex = re.compile(r'^.+#')
# print(regex.findall('d_r56#'))
# print(regex.findall('\nd_r56#12weerrttyu'))
# regex = re.compile(r'\S+$')
# print(regex.findall('\nd_r56#12weerrttyu '))


def get_password(m):
    # data = set(ascii_letters + digits) - {'0', '1', 'o', 'O', 'l', 'I'}
    # data = ''.join(data)
    data1 = ''.join(re.findall(r'[^01oOlI]', ascii_letters + digits))
    password = random.sample(data1, m)
    # pos = random.sample(range(m), 3)
    # password[pos[0]] = password[pos[0]].lower()
    # password[pos[1]] = password[pos[1]].upper()
    # password[pos[2]] = str(random.randint(2, 9))
    password = ''
    while (not re.search(r'[a-z]', password)
           or not re.search(r'[A-Z]', password)
           or not re.search(r'[2-9]', password)):
        password = ''.join(random.sample(data1, m))

    return password


def main(n, m):
    res = set()
    while len(res) < n:
        res.add(get_password(m))

    with open('passwords.txt', 'w') as f:
        for i, p in enumerate(res, 1):
            f.write(f'{i:2}. {p}\n')


# main(10, 12)

regex = r'^[+0-9]9\d{9,10}'
phone_number = '897832145677'
res = re.fullmatch(regex, phone_number)
if res:
    print(res.group())
else:
    print('неправильный номер ТЛФ')
