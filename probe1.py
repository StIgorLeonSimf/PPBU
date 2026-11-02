f = [1, 2, 6, 7, 8]
temp = f[1]
for i in range(1, 4):
    f[i] = f[i+1]
f[4] = temp
print(f)