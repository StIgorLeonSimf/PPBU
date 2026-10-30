"""Match     match = re.search(regex, string)"""


import re

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
regex = re.compile(r'^.+#')
print(regex.findall('d_r56#'))
print(regex.findall('\nd_r56#12weerrttyu'))
regex = re.compile(r'\S+$')
print(regex.findall('\nd_r56#12weerrttyu '))