# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ':', a[x][y])

# a = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694, },
#     'Tom': {'N': 4832, 'S': 6786, 'E': 3056, 'W': 3056, },
#     'Anne': {'N': 3056, 'S': 3056, 'E': 3056, 'W': 3056, },
#     'Fiona': {'N': 3056, 'S': 3056, 'E': 3056, 'W': 3056, },
# }
#
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ':', a[x][y])
# n = input("Имя: ")
# p = input("Регион: ")
#
# print(a[n][p])
# s = int(input("Новое значение: "))
# a[n][p] = s
# print(a[n])

# a = {'один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4}
# d = {key: value for key, value in a.items() if value <= 2}
# print(d)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)

# value = input('--> ')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}
# print(d)

# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))
# # try:
#     print(m[(2, 0)])
# except KeyError:
#     print(0)

############################ SciPy ############################

# list()
# a = {1: 'rectangle', 2: 'triangle', 3: 'circle'}
#
# value = list(a.values())  # список значений словаря
# print(value)
# k = list(a.keys())  # список ключей словаря
# print(k)
# par = list(a.items())  # список пар (ключ: значение)
# print(par)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# a = ['dec', 'jan', 'feb']
# b = [12, 1, 2]
# d = {k: v for (k, v) in zip(b, a)}
# # d = dict(zip(a, b))
# print(d)

# print(list(zip(range(5), range(100))))

# ls = [1, 3, 2, 4]
# n = ['a', 'c', 'b', 'd']
#
# a = list(zip(ls, n))
# print(a)
# a.sort()
# print(a)
# a = list(zip(n, ls))
# print(a)
# a.sort()
# print(dict(a))

# month = ['Jan', 'Feb', 'Mar']
# total = [52000.00, 51000.00, 48000.00]
# production = [46800.00, 45900.00, 43200.00]
#
# for t, p, m  in zip(total, production, month):
#     profit = t - p
#     print(m, profit)