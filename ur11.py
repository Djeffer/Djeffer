# Словари

# a = [1, 2, 3, 4]
# c = dict(a)
# b = {"one": 1, "two:": 2}
# print(b)

# d = {}
# print(d)
# print(type(d))
# d1 = dict()
# print(d1)
#
# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)

# user = (
#     ('qwerty@mail.ru', 'Evgeny'),
#     ('uiop@mail.ru', 'Danila'),
#     ('asdfg@mail.ru', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {a: a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4[2])
# d4["2"] = 15
# print(d4)
# d4["5"] = 4**2
# print(d4)

# d5 = {0: 'text1', 'one': 40, (1, 2.3): 'кортеж', 'two': [2, 3, 6, 7], True: 1}
# print(d5)
# print(d5['two'][1])
#
#
# print('one' in d5)
# print('a' in d5)
# print(d5.keys())
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")


# d6 = {'one': 1, 'two': 2, 'thee': 3}
# print(d6["four"])
# key = "four"
# if key in d6:
#     del d6[key]
#
# try:
#     del d6[key]
# except KeyError:
#     print('Элемента с ключем "' + key + '" нет в словаре')
#
# print(d6)


# d6 = {'one': 1, 'two': 2, 'thee': 3}
# for key in d6:
#     print(key, "=", d6[key])

# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# count = 1
# for i in a:
#
#     print()

# d = dict()
# d[1] = input("--> ")
# d[2] = input("--> ")
# d[3] = input("--> ")
# d[4] = input("--> ")
# print(d)
# d2 = int(input("Какой элемент исключить: "))
# del d[d2]
# print(d)

# d6 = {'one': 1, 'two': 2, 'thee': 3}
# print(len(d6))

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны: ", country, ": ", capitals[country])
#     else:
#         print("В базе нет страны с названием: ", country)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-3450', 5, 6400],
# }
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][col], "шт. по ", goods[i][2], "руб", sep="")
# while True:
#     a = int(input("№: "))
#     if a == 0:
#         break
#     col = int(input("Кол-во: "))
#     for i in goods:
#       print(i, ") ", goods[i][0], " - ", goods[i][col], "шт. по ", goods[i][2], "руб", sep="")


# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()  # Удаление
# print(d)
# d2 = d.copy()  # копирование
# print("d2 = ", d2)
# print("d = ", d)
# d2["B"] = 5
# d["E"] = 7
# print("d2 = ", d2)
# print("d = ", d)
# value = d.get("B")  # получение значения по задоному ключу
# print(value)
# new = d.items()  # список пар ключей и значений
# print(new)
# new1 = dict.items(d)
# print(new1)
# a = d.keys()  # список ключей словаря
# print(a)
# item = d.pop("B")
# print(item)
# item = d.popitem()
# print(item)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {i: d[i] for d in [x, y] for i in d}
# z = x.copy()
# z.update(y)
# z = x | y | w
# print(z)

# d = {"A": 1, "B": 2, "C": 3}
# v = list(d.values())  # список значений
# print(v)

x1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
x2 = dict()
x2['name'] = x1.pop('name')
x2['salary'] = x1.pop('salary')
print(x1)
print(x2)