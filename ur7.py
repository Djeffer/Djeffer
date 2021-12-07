# import math as m
import time
from math import *

# radius = 2
# print(pi * (radius ** 2))

# comb = comb(5, 9)
# print(comb)
# num = sqrt(2)
# print(num)
# num1 = ceil(3.2)
# print(num1)
# num2 = floor(3.2)
# print(num2)

# r = int(input("Введите радиус окружности: "))
# print(round((pi * r * 2), 2))

# num = -5.24
# print("Модуль числа: ", fabs(num))
#
# a = 14
# b = 8
# print("Наибольший делитель: ", gcd(a, b))
#
# mun_list = [0.3, 0.3, 0.3]
# print("Сумма: ", fsum(mun_list))
# print("Сумма: ", sum(mun_list))
# # decimal
# print(degrees(3.12124))
# print(radians(180))
# print(cos(radians(60)))
# print(sin(radians(90)))
# print(tan(radians(0)))

# k = int(input("Катет 1: "))
# k1 = int(input("Катет 2: "))
# print(sqrt((k**2) + (k1**2)))

# f = int(input("Выбор фигуры: \n1 - треугольник \n2 - Прямоугольник \n3 - Круг \n:"))
# if f == 1:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     c = float(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = sqrt((p * (p - a) * (p - b) * (p - c)))
# elif f == 2:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     s = a * b
# elif f == 3:
#     r = float(input("Введите радиус r = "))
#     s = pi * (r ** 2)
# print(round(s, 2))

from time import *
import locale

locale.setlocale(locale.LC_ALL, "ru")


# sec = time()
# print("Секунд с начала эпохи: ", sec)
# local_time = ctime(sec)
# print("Местное время: ", local_time)
# res = localtime(sec)
# print("Локальное время: ", res)
# print("Год: ", res.tm_year)
# print("Месяц: ", res.tm_mon)
# print("День месяца: ", res.tm_mday)
# print("Часы: ", res.tm_hour)  # c 0 до 23
# print("Минуты: ", res.tm_min)  # c 0 до 59
# print("Секунды: ", res.tm_sec)  # c 0 до 61
# print("День недели: ", res.tm_wday)  # c 0 до 6
# print("День года: ", res.tm_yday)  # c 1 до 366
# print("Учет перехода на летнее время: ", res.tm_isdst)  # 0 или 1
#
# print(strftime("Today id %B %d, %Y", localtime(456127887)))
# print(strftime("%m/%d/%Y %H:%M:%S"))

# pause = 0.5
# print("Programa started...")
# sleep(pause)
# print(str(pause) + " seconds.")

# s = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# sleep(local_time)
# print(s)

# start = monotonic()
# sleep(1)
# finish = monotonic()
# res = finish - start
# print("Program time: " + str(res) + " seconds.")

# print(strftime("Сегодня: %B %d, %Y"))
# local_time = ctime(sec)
# print("Местное время: ", local_time)

# def hello(name, word):
#     print("Hello, ", name, ". Say " + word, sep="")
#
#
# hello("Evgeniy", "Hi")
# hello("Anna", "Hello")

def get_sum(a, b):
    print(a + b)


x = 2
y = 3
# res = get_sum(x, y)
# print(res)
print(get_sum(2.6, 4.3))
# get_sum("abc", "def")
# get_sum(str(x), "aaa")

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(10, "+", "-")
# symbol(7, "X", "0")
