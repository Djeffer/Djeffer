# Множество - set()  выводит уникальное значение.

# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
# a = set('hello')
# print(a)
# c = ["red", "green", "green", "blue", "purple"]
# col = set(c)
# print(col)

# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6]
# num = list({i for i in numbers if i % 2 == 0})
# print(num)


# def to_set(a):
#     b = set(a)
#     return b, len(b)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# c = {"red", "green", "green", "blue", "purple"}
# print("green" in c)
# print("green" not in c)

# pr = {2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {i for i in r1 if "a" not in i}
# print(a)

# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r1 if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3, 4, 5}
# a.add(6)  # добавление одного элемента
# print(a)
# a.remove(6)  # удаление одного элемента
# print(a)
# b = 2
# if b in a:
#     a.remove(b)
# print(a)
# a.discard(1)  # удаление без генерации исключения, если элемент отсутствует
# print(a)
# a.pop()  # удаление первого элемента
# print(a)
# a.clear()  # удаление всех элементов
# print(a)

# a = {0, 1, 2, 3}
# # b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b  # union() одинаково
# # a.update(b)
# # a |= b
# # c = a.intersection(b)
# # c = a & b
# # a &= b
# c = a.copy()
# print(c)
# # print(a)

# a1 = {1, 2}
# a2 = {3}
# a3 = {4, 5}
# a4 = {3, 2, 6}
# a5 = {6}
# a6 = {7, 8}
# a7 = {9, 8}
# ob = a1 | a2 | a3 | a4 | a5 | a6 | a7
# print(ob)
# print("Уникальные: ", len(ob))
# print("Min: ", min(ob))
# print("Max: ", max(ob))

# a = "Hello"
# b = "How are you"
# c = set(a) & set(b)
# for i in c:
#     print(i, end=" ")

# draw = {"Марина", "Женя", "Света"}
# mus = {"Костя", "Женя", "Илья"}
#
# one = draw ^ mus
# two = draw & mus
# draw = draw - two
#
# print("Only one hobby: ", one)
# print("Both hobbies: ", two)
# print("Drawing: ", draw)

# тип frozenset
# s = frozenset({i**2 % 4 for i in range(10)})
# print(s)
# print(len(s))
# print(2 in s)

# r = set('ABCD')
# b = {frozenset({i+j for j in r.difference({i})}) for i in r}  # проверка исключение дублей
# print(b)

def superset(s1, s2):
    if s1 > s2:
        print("Объект", s1, "является чистым супермножеством")
    elif s1 == s2:
        print("Множетсва равны")
    elif s1 < s2:
        print("Объект", s2, "является чистым супермножеством")
    else:
        print("супермножества не обнаружено")


set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)
