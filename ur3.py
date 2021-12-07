# day = int(input("Введите день недели(цифрами):"))
# if 1 <= day <= 5:  ##(day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели нет!")


# month = int(input("Введите номер месяца(цифрами):"))
# if month == 1 or month == 2 or month == 12:
#     print('Зима')
# elif month == 3 or month == 4 or month == 5:
#     print('Весна')
# elif month == 6 or month == 7 or month == 8:
#     print('Лето')
# elif month == 9 or month == 10 or month == 11:
#     print('Осень')
# else:
#     print('Такого дня недели нет!')

# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "a < b"))

# try:
#     n = int(input("Введите делимое число: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except ValueError:
#     print("Что то пошло не так!")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль!")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы!")


# n = input("Введите первое число словом: ")
# m = input("Введите второе число словом: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 0
# while i <= 20:
#     print("i = ", i)
#     i += 2

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое.")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")

# n = input("Введите начало диапозона: ")
# m = input("Введите конец диапозона: ")
# sum = 0
# while n < m:
#     if n % 2 != 0:
#         sum += n
#     n += 1
# print("Сумма нечетных чисел: ", sum)

# i = 0
# while True:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число: "))
#     if not  n > 0:
#         break


# s = 1
# while True:
#     a = int(input("Введите число: "))
#     if not a != 0:
#         break
# s += a
# print(s)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i = ", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j = ", j)
#         j += 1
#     i += 1

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, "*", j, "=", i * j, "\t\t", end="")
        j += 1
    print()
    i += 1
