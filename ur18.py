# s = "hello, WORLD! I am learning Python. 123@№"
# #
# print(s.capitalize())  # Первый символ переобразовает вверхний регистр, все остальные преобразуются в нижний регистр - 1
# print(s.lower())  # Все символы преобразуются в нижний регистр - 2
# print(s.upper())  # Все символы преобразуются в вверхний регистр - 3
# print(s.swapcase())  # Меняет регистр символа в противоположный - 4
# print(s.title())  # Первую букву слова переобразует в заглавную - 5
#
# print(s.count("I"))  # Взвращает количество вхождений подстроки в строку - 6
# print(s.lower().count("i"))  # Комбинация 2 и 6
# print(s.count("l", 0, 15))
# print(s.find("l", 3))  # Возвращает первый индекс, который соответствует элементу, начиная с начала строки

# s = input("Введите два слова через пробел: ")
# a = s[s.find(' ') + 1:] + " " + s[:s.find(' ')]
# print(a)

# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# print(s.index("Python"))  # Возвращает первый индексб который сщщтветсвует элементуб начиная с начиная с начала строки
# print(s.index("cPython"))  # Возвращает ValueError если совпадения не найдено

# s = "Дана ст(рока символов ,среди которых есть одна открыв)ающаяся"
# print(s[s.find('(') + 1:s.find(')')])

# s = "hello, WORLD! I am learning Python. 123@№"
#
# print(s.rfind("l", 3, 16))
# print(s.rindex("l"))

# s = 'aaaaaafaaaaaafaaaaaaaaafaaaafaaaa'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print("None")

# s = "hello, WORLD! I am learning Python. 123@№"
# # print(s.endswith("hello", 0, 5))  # Определяет заканчивается строка заданой подстрокой
#
# print('abc123'.isalnum())  # Определяет состоит ли строка из букв и цифр (возвращает буливое значение True|False)
# print('AAC%njk'.isalnum())  # Определяет состоит ли строка из букв и цифр, не присуствует служебные символы
# print('45645'.isdigit())  # Определяет состтоит ли строка из цифр (возвращает буливое значение True|False)
# print('asd'.isidentifier())  # является ли строка допустимым индентификатором
#
# print('abc'.islower())  # определяет, является ли буквенные символы строки строчными
# print(' '.isspace())  # определяет состоит лт строка из пробельных символов
#
# print("Hello".istitle())  # определияет начинается ли строка с заглавной буквы
# print("HELLO".isupper())  # определяет состоит ли строка с заглавных букв
#
# print('py'.center(10))  # выравнивает строку по центру
# print('https://www.python.org'.lstrip('/:pths'))  # обрезает заданные символы с левой стороны
# print('https://www.python.org'.rstrip('/:pths'))  # обрезает заданные символы с правой стороны

# s = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# print(s.replace("Nuthon", "Python"))


# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s[:s.find('о') + 1] + s[s.find('о') + 1:s.rfind('о')].replace('о', 'О') + s[s.rfind('о'):])

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # объеденили список в строку
# print("..".join(['1', '99']))
# print(":".join("Hello"))

# print("Строка разделенная пробелами".split())

# a = input("--> "). split()
# print(a)

# Иванов Иван Иванович
s = input("Введите ФИО: ")


def ren(inp):
    arr = inp.split(" ")
    return arr[0] + " " + arr[1][0] + ". " + arr[2][0]+"."


print(ren(s))
