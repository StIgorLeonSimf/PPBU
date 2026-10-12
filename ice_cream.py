# with open('ice-cream.csv', 'r', encoding='utf-8') as file:
#     ls = file.readlines()
#     for index, line in enumerate(ls):
#         pass
import math

result = {}
for i in open('ice-cream.csv', 'r', encoding='utf-8'):
    ls = i.strip().split(';')
    for topping in set(ls):
        if topping.startswith('t'):
            continue
        # if topping not in result:
        #     result[topping] = 1
        # else:
        #     result[topping] += 1
        result[topping] = result.get(topping, 0) + 1
mx = 0
name_max = ''
mn = math.inf
name_min = ''
for topping, count in result.items():
    if count > mx:
        mx = count
        name_max = topping
    if count < mn:
        mn = count
        name_min = topping
mx = max(result.items(), key=lambda x: x[1])[0]
mn = min(result.items(), key=lambda x: x[1])[0]

print(name_max, name_min)
print(mx, mn)