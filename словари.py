"""dict
неупорядоченный набор пар ключ:значение в которых ключ уникален
"""

d = {}

d = {'Pb': 'свинец', 'Au': 'Золото'}

print(d['Pb'])
print(d.get('Au', 'my items'))

d['Pb'] = 'Свинец'
print(d)
d['Fe'] = 'Железо'
print(d)
d.setdefault(1, 1000)
print(d)
d.update({3: 33, 1: 11})

n = d.pop('Fe')
nn = d.popitem()

print(n, nn)
# d.clear()
print(d)
print(len(d))

print(d.keys())
print(list(d))
for i in d:  ## d.keys()
    print(i)

print(list(d.values()))
for v in d.values():
    print(v)

print(list(d.items()))
for k, v in d.items():
    print(k, v)

lst = [('Pb1', 'Свинец1'), ('Au1', 'Золото1'), (11, 111)]
dd = dict(lst)
print(dd)
lst = [11, 22, 33]
dd = dict.fromkeys(lst, 100)
print(dd)

dd = {i: i**2 for i in range(10, 20)}
print(dd)
dd = {}
for i in range(10, 20):
    dd[i] = i**2
print(dd)
