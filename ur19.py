import re

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
# reg = 'я'
# print(s.find(reg))  #15
# # find() - в строку будет искать шаблон и возвращать индекс первого вхождения подстроки в строке. Если шаблон не
# # найденб то будет возвращать значение "-1"
# print(reg in s)
#
# print(re.findall(reg, s))  # возвращает списокб содержащий совподение с регулярным вырожением
# print(re.findall("12", s))
# print(re.search(reg, s))  # местоположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# # reg = 'Я'
# print(re.match(reg, s))  # поиск по заданому шаблону вначале строки
# reg = r"\."
# print(re.split(reg, s, 1))  # возвращает список, в который строка разбита по шаблону
# print(re.sub(reg, "!", s))  # заменяет совпадения указаном тексте
# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта.'
# # reg = '[0-9]'
# # print(re.findall(reg, s))
# s = "Ели[-ели]."
# reg = '[А-яа-яё.\[\]-]'
# print(re.findall(reg, s))
#[^abc]  - возвращает совпадение для любого символа, кроме заданых

# s = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапозоне от 00 до 59. 2021-0615Т01:09"
# reg = r'[0-2][0-9][\:][0-5][0-9]'
# print(re.findall(reg, s))


s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
reg = r'\A'
print(re.findall(reg, s))
# \d - одна любая цифра [0-3]
# \w - букваб цифра, символ подчеркивания (_)
# \s - один пробельный символ(включая табуляцию и перенос строки)
# \D - все кроме цифр
# \W - все кроме букв, цифр, символ подчеркивания (_)
# \S - все кроме пробелов
# \A - ищет символ в начале строки
# \Z - ищет символ в конце строки
