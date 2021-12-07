# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     print(" " * i + "*")
#     i += 1

# for element in collections:
#     print(element)

# for i in 'Hello':
#     print(i)
#
# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue':
#     print(j, 'color:', color)
#     j += 1
#
# for i in 'one', 'two', 1, 2, 20, 3:
#     print(i)

# for i in range(n):
#     Тело цикла

# range(start, stop, step)

# for i in range(9, -1, -1):
#     print(i, end=" ")

# num = int(input("Введите целое число: "))
# for i in range(1, num):
#     if num % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break
# else:
#     print("\nDone!")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("------")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высота прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end=" ")
#     print()

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высота прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if (i == 0 or i == h - 1) or (j == 0 or j == w - 1):
#             print('*', end=" ")
#         else:
#             print(' ', end=" ")
#     print()

# [результирующие вырожение |  цикл | опциональнальные условия]
# print([i * 2 for i in "Hello"])
# print([i ** 3 for i in range(30) if i % 2 == 0])
# num = [i ** 3 for i in range(30) if i % 2 == 0]
# print(num)

a = 12
c = 0
v = 0
for i in range(1000):
    b = int(input("Введите число от 1 до 100: "))
    if a > b:
        print("Загаданное число больше")
        c += 1
    elif a < b:
        print("Загаданое число меньше")
        v += 1
    else:
        f = c + v
        print("Вы угадали с ", f, "раза")
        break
    i += 1

