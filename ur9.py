# Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# # Упаковка кортежа
# a1 = (5,)
# print(a1)
# c = tuple((1, 2, 3))
# print(type(c))
# print(c)
#
# t1 = tuple("hello")
# print(t1)

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])
#
# s1 = tuple([int(input("-->"))for i in range(5)])
# print(s1)

# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)

from random import *

# mas = ([randint(0, 13) for i in range(10)])
# print(mas)

# tpr = tuple([2 ** i for i in range(1, 13)])
# print(tpr)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
# print(t3.count("l"))
# print(t3.index("l"))
#
# if "l" in t3:
#     print(t3.index("l"))
# else:
#     print("Такого нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             f = tpl.index(el)
#             s = tpl.index(el, f + 1)
#             return tpl[f:s + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 5, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tpl(a, b):
#     mas = tuple([randint(a, b) for i in range(10)])
#     return mas
#
#
# x1 = tpl(0, 5)
# print(x1)
# x2 = tpl(-5, 0)
# print(x2)
# x3 = x1 + x2
# print(x3)
# print("0 =", x3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))

# lst = [1, 2, 3, 3, 2]
# lst2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]

# def func(lst):
#     list_num = []
#     unique = set(lst)
#
#     for num in unique:
#         list_num.append(num)
#
#     return list_num
#
#
# print(func(lst))
# print(func(lst2))

#  распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)

contries = (
    ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
    ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
)

print(contries)
for country in contries:
    countryName, countryPopulation, cities = country
    print("\n Страна: ", countryName, "насиление = ", countryPopulation)
    for city in cities:
        cityName, cityPopulation = city
        print("\t Город: ", cityName, "насиление = ", cityPopulation)

