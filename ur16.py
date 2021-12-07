# d = {'c': 4, 'a': 10, 'b': 15}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
# ]
# # d_players = list(players.items())
# # print(d_players)
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res1 = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res1)
# res2 = sorted(players, key=lambda item: item['raiting'])
# print(res2)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# b = a[3](5, 12)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print('Monday'),
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday')
# }
#
# d[2]()
# import math
#
#
# s = {
#     'Circle': (lambda r: math.pi*r*r),
#     'Rectangle': (lambda a, b: a*b),
#     'Trapezoid': (lambda a, b, h: (a+b)*h/2.0)
# }
#
# print('Площадь окружности радиуса 2: ', s['Circle'](2))
# print('Площадь прямоугольника 10, 13: ', s['Rectangle'](10, 13))
# print('Площадь трапеции для a=7, b=5, h=3: ', s['Trapezoid'](7, 5, 3))

# True if услоывие else False

# maximus = lambda a, b: a if a > b else b
# print(maximus(15, 13))
# print(maximus(5, 13))


# m = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(m(9, 8, 5))

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# lst2 = list(map(mul, lst))
# print(lst2)
#
# lst3 = list(map((lambda t: t*2), lst))
# print(lst3)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)

# l = [1.8878, 3.454545787, 2.47897, 3.6454, 4.121215]
# res = list(map(round, l, range(1, 7)))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), l1, l2))
# print(res)

# l1 = 'hello'
# res = list(map(lambda x: x * 3, l1))
# print(res)


# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter((lambda s: len(s) == 3), t))
# print(t2)

# l = [ 8, 15, 7, 3, 11, 23, 187, -5, 20, 17 ]
# l2 = list(filter(lambda s: (s > 75), l))
# print("L2 = ", l2)
import random as r

# l = [r.randint(1, 40) for i in range(10)]
# l2 = list(filter(lambda s: (s >= 10) and (s <= 20), l))
# print(l2)

# a = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: not s % 15, a)))

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)

# a = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], a))
# print(m)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# """Тройные двойные кавычки"""
# '''Три одинарные кавычки'''
import math


def cylinder(r, h):
    """
    Вычислчет площадь цилиндра.

    Вычисляет площадь цилиндра на основе заданой высоты и радиуса основания
    :param r: положительное число, радиус основания цилиндра
    :param h: положительное число, высота цилиндра
    :return: положительное число, площадь цилиндра
    """
    return 2 * math.pi * r * (r + h)


print(cylinder(3, 6))
print(cylinder.__doc__)
print(max.__doc__)
