# m_list = [1, 2, 3, 4, 5]
# print(m_list)
# print("______________________________________")
# for i in m_list:
#     print(i**2, end=" ")
# print("\n______________________________________")
# for i in range(len(m_list)):
#     m_list[i] += 5
#     print(m_list)
#     print(m_list[i], end="")

# a = [input("-> ") for i in range(int(input(" n = ")))]


# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Колличество четных элементов: ", k)
# print("Сумма элементов: ", s)

# summa = k = 0
# a = [input("-> ") for i in range(int(input(" n = ")))]
# for i in range(len(a)):
#     if a[i] != 0:
#         summa += a[i]
#         k += 1
# print(summa/k)

# Срезы - получение какой-то части списка, которая в свою очередь тоже является списком!

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[8] = [20]
# s[8:9] = [20]
# print(s)
# print(s[0:7])
# print(s[::-1])
# print(s[1::2])
# print(s[:1])
# print(s[6:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:-6:-1])
# print(s[2:5])

## Списки и методы

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # Добавляет элемент в конец списка
# print(s)
# s1 = []
# s1.extend([1, 2, 3])  # Добавляет множество элементов
# print(s1)
# s1.extend('add')  # Добавляет множество элементов
# print(s1)
# s.insert(1, 100)  # Добавляет элемент в список в заданную позицию
# print(s)

# old = []
# for x in range(1, 11):
#     old.append([x ** 2])
# print(old)

# s2 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s2.append(x)
# print(s2)

# s = []
# n = int(input("Кол-во элементов: "))  # ????

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c =[]
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)

# s[7:] = []
# print(s)
# s.remove(0)  # Удаляем элемент из списка с  заданным значением, если элементов несколько, то удалится только самый первый

# s[3:5] = []
# print(s)
#
# last = s.pop()  # возвращает элемент на указанный позицииб удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
#
# # s.clear()  # удаляет из списка все имеющиеся в нгем значения
# # print(s)
#
# del s[1]
# print(s)

# s2 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s2.append(x)
# k = int(input("Введите индекс: "))
# del s2[k]
# print(s2)

# s = []
# s.extend([3, 1, 3, 20, 3, 4, 3, 50, 3])
# print(s)
# num = s.count(3)  # Считает кол-во значений "3" в списке
# print(num)
#
# ind = s.index(3, 3)  # Возвращает положение первого индекса
# print(ind)
#
# s_copy = s.copy()  # Возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print("a = ", a)
# print("b = ", b)
#
# s.append(120)
# print(s)
# print(s_copy)
#
# s.reverse()  # Перестраивает элементы в обратном порядке
# print(s)
#
# s.sort(reverse=True)  # сортирует список от меньшего к большему,  если (reverse=True) - от большего к меньшему
# print(s)
#
# sorted_s = sorted(s, reverse=True)
# print(sorted_s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)

# s2 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s2.append(x)
# k = int(input("Введите индекс: "))
# del s2[k]
# s2.sort(reverse=True)
# print(s2)

# import random
# from random import random, randint, randrange
#
# print(random())  # [0.0, 1.0]
# print(randint(0, 9))
# print(randrange(0, 10, 2))

import random as r

print(r.randint(0, 5))
print(r.randrange(0, 10, 2))

cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
print(r.choice(cities))

s = [55, 66, 77, 88, 99, 66, 45, 78, 90]
# print(r.choice(s))
print(r.sample(s, 5))
print(r.choices(s, k=5))
r.shuffle(s)
print(s)
print(round(r.uniform(10.5, 25.5), 2))

mas = [r.randint(0, 100) for i in range(10)]
print(mas)

