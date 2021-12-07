# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19))  # двоичная система
# print(oct(19))  # восмиричная система
# print(hex(19))  # шестнадцатеричная система
#
# print(0b1010)
# print(0o12)
# print(0xFF)
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * -3)
#
# print(e in "I am learn Python")
# print(e in "I am learn Java")
#
# s = 'Hello'
# print(s[-1])
# print(s[::-1])

# s = 'abcdefgh'
# print(s[slice(2, 5)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, 2)])

# s = 'python'
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования."
# str2 = change_char(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Hello")
# print('I\'m learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])

# name = "Дмитрий"
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# import math
# print(f"Значение числа pi: {math.pi:.2f}")
#
# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}')


# planets = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f'Мыживем на планете {planets[2]}')
#
# planet = {"name": "Земля", "radius": 6378000}
# print(f"Планета {planet['name']}. Радиус {planet['radius']/1000} км.")
#
# print(f"13 / 3 = {round(13/3)}")

# name = "друг"
# prof = "программист"
# lang = "Python"
#
# message = (
#     f"Привет {name}. "
#     f"Ты {prof}. "
#     f"На языке {lang}."
# )
#
# print(message)

# a = 74
# print(f"{{{a}}}")

# s = '''Hello'''
# print(s)

# s = 5
# print('Мне ' + str(s) + " лет")

# s = '5'
# s1 = '2'
# print(min(s, s1))
# print(max(s, s1))

# s = 'Hello'
# s1 = 'hel'
# print(min(s, s1))
# print(max(s, s1))

# print(ord('a'))  # 97
# print(ord('#'))  # 35
#
# print(ord('к'))
#
# while True:
#     n = input("--> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# mystr = "Test string for me"
# arr = [ord(x) for x in mystr]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in (input("--> "))[:4]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print()
# arr.sort(reverse=True)
# print(arr)


a = 122
b = 97
if a > b:
    for i in range(b, a + 1):
        print(chr(i), end=" ")
else:
    for i in range(a, b + 1):
        print(chr(i), end=" ")
