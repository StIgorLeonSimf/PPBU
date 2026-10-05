# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     if i == 7:
#         continue
#     print(i, end=' ')
# print()
#
# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     if i == 17:
#         break
#     print(i, end=' ')
# else:
#     print('\nOK')


# n = int(input('> '))
# sm = 0
# cnt = 0
# while n != 0:
#     sm += n
#     cnt += 1
#     n = int(input('> '))
#
# print(f'Сумма - {sm}\n'
#       f'Кол-во - {cnt}')

""" s = 3 + 2 + 1
    k = 1  + 1  + 1
123  % 10  = 3
    // 10  = 12 % 10 = 2
                //10 = 1  % 10 = 1
                          // 10 = 0


"""
n = int(input('> '))
nn = n
sm = 0
cnt = 0
while n > 0:
    rem = n % 10
    sm += rem
    cnt += 1
    n //= 10
print(f'В числе "{nn}" {cnt} ц. суммой {sm}')