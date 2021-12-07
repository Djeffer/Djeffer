# a =4.5646121212121216
# print(a)
# print(type(a))

# print(6/2)  # 3.0
# print(7/2)  # 3.5
# print(7//2)  # 3

# a = 5
# b = 7
# c = 3
# print("sum:", a + b + c)
# print("pro: ", a*b*c)
# print("srz: ", (a + b + c)//3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num -= 5
# print(num)

# num = 9753
# print("Исходные число: ", num)
# res = num % 10 * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
#
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# print(int(num1) + num2)
# print(num1 + str(num2))

# print(int(3.8))  # Целое число
# print(round(3.895, 2))  # Округление, сколько оставить знаков после запятой

# a = 5 / 3
# print(a)
# print(round(a, 2))
#
# a = "5.2"
# b = 10
# print(float(a) + b)

# a = 1
# b = 2
# print("a:", a, "\nb:", b)

# name = "Evgeniy"
# age = 30
# print("Меня зовут", name, ". Mне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python!")

# name = "Evgeniy"
# age = 30
# grade = 9.2
# print("Is`s %s, %d. Level: %.1f" % (name, age, grade))

# print("This is a {0}. It`s {1}.".format("ball", "red"))


# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}. Ваш город {1}")

# n = input("Введите число: ")
# s = input("Введите степеть: ")
# print("Результат: ", int(n) ** int(s))

# a = int(input("Введите 1-ое число: "))
# b = int(input("Введите 2-ое число: "))
# c = int(input("Введите 3-ое число: "))
# d = int(input("Введите 4-ое число: "))
# enter = (a + b) / (c + d)
# print("Результат: ", round(ent, 2))
#
# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
#
# print(bool("Python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(True))  # True
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# print("Hello" > "Hello")
#
# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(4-3 == 2 and 1 + 3 == 4)

# print(4-3 == 2 or 1 + 3 == 4)

# print(not 9 - 9)

# v1 = (0 or 1) and (0 or 1)
# print(v1)
#
# v2 = 0 or 1 and 0 or 1
# print(v2)
#
# a = 0
# b = 0
# v3 = (a or 1) and (b or 0)
# print(v3)

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >=18:
#     print("Доступ на сайт разрешен!")
# else:
#     print("Доступ на сайт запрещен!")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

a = int(input("Введите 1-ое число: "))
b = int(input("Введите 2-ое число: "))
c = int(input("Введите 3-ое число: "))

if a == b:
    print("Треугольник равнобедренный")
elif a == b or b == c or c == a:
    print("Треугольник равносторонний")
else:
    print("Треугольник разносторонний")



