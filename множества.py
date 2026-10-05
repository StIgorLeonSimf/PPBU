# n = 9
# m = 100
#
# print('первая переменная - "', n, '", '
#                                   'Вторая переменная - "', m, '", '
#                                                               'm/n = "', m // n,'"', sep='')
# print('первая переменная - "%d", Вторая переменная - "%d", m/n = "%d"'%(n, m, m//n))
# print('первая переменная - "{}", Вторая переменная - "{}", m/n = "{}"'
#       .format(n, m, m//n))
# nn = f'первая переменная - "{n}",\nВторая переменная - "{m}",\nm/n = "{round(m / n, 2)}"'
# nn = f'первая переменная - "{n}",\nВторая переменная - "{m}",\nm/n = "{m / n:.2f}"'
# print(nn)

""" Множество (set) неупорядоченный
набор уникальных объектов
(любые неизменяемые типы данных)
"""
ls = [22, 22, 22, 33, 33]
st = set(ls)
print(st)
st.clear()
st = {22, 33, 44}
print(st)

st.add(100)
st.update({2, 3})
print(st)
n = st.pop()
st.remove(3)
st.discard(2)
print(n)
print(st)

# print(st)
# for i in st:
#     print(i)

st1 = {3, 4, 33}
st2 = {3, 4, 44}

# res = st1.union(st2)  # объединение множеств
res = st1 | st2

res = st1.intersection(st2)  # пересечение  множеств
res = st1 & st2

res = st1.difference(st2)  # Вычитание множеств
res = st2 - st1
print(res)

res = st1.symmetric_difference(st2)
res = st1 ^ st2
print(res)
st1 = {3, 4, 33}
st2 = {3, 4, 44}
st3 = {3, 4}
print(st3.issubset(st2))
print(st1.issuperset(st3))