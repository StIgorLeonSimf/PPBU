# s = ' 12f3d4g5'

# ls = []
# for letter in s:
#     if letter in '0123456789':
#         ls.append(letter)
# ls = (letter for letter in s if letter  in '0123456789')
# print(ls)
# print(''.join((letter for letter in s if letter  in '0123456789')))
from fraction import add, sub, mult, div
import pytest


@pytest.mark.parametrize('n1,d1, n2, d2, res',
                         [
                             (1, 1, 1, 1, (2, 1)),
                             (2, 1, 1, 2, (5, 2)),
                             (1, 2, 2, 1, (5, 2)),


                         ])
def test_add(n1, d1, n2, d2, res):
    assert add(n1, d1, n2, d2) == res


def test_sub():
    assert sub(1, 1, 1, 1) == (0, 1)
    assert sub(2, 1, 1, 2) == (3, 2)

# test_add()
