try:
    n = int(input('> '))
    if n == 100:
        raise TypeError('Число 100 запрещено к использованию')
    print(n)

except (ValueError, ZeroDivisionError):
    print('Please enter a number')
except NameError:
    print('Please enter a name')
except Exception as err:
    print(err)
else:
    print('Когда нет ошибки')
finally:
    print('Всегда')