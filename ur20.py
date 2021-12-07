import re

# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))


# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master'))
# print(validate_name('Python_master_master'))

# жадные (greedy) - захватывает максимально возможное число символов
# ? - ленивые (lazy) - захватывает минимальное возможное число символов
# (где можно проставлять знак - *?, +?, ??){n,m}?, {, m}?, {n,}?

# text = '<body>Пример жадного соотвествия регулярных вырожений</body>'
# print(re.findall('<.*?', text))
# print(re.search('<.*?>', text).group())

# s = '<p>Изображение <img src="bg.jpg"> - фон страницы</p>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))

# s = 'Python (в русском языке встречаются названия питон[16] или пайтон[17] - высокоуровневый язык программирования)'
# reg = r'\[.*?]'
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий отлично учатся!'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5, QW"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I))
# print(re.search(reg, s, re.I).group())

# s = '5 + 7*2 - 4'
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# 28-08-2021
# s = input("Введите дату в формате dd-mm-YYYY: ", 28-08-2021)
# reg = r'([0-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-([0-9][0-9][0-9][0-9])'
# print(re.findall(reg, s))

# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# # reg = r'Людовик(?=VI)\w+'
# reg = r'\w+(?<!Людовик)VI'
# print(re.findall(reg, s, re.I))

# s = "1X, Text ABC 123 A1B2C3"
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s))
#
# s1 = "text from #START# till #END#"
# reg1 = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg1, s1))
#
# s2 = "12_34__56"
# reg2 = r'\d+(?=_(?!_))'
# print(re.findall(reg2, s2))

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счета.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print("Срока: ", m[0])
# print("Цифры: ", m[1])
# print("Буквы: ", m[2])

# s = 'Самолет прилетает 10/23/2021.  Будем Вас рады видеть после 10/24/2021'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'google.com and google.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

def is_roman_number(num):
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$"
    if re.search(pattern, num):
        return True
    return False


print(is_roman_number("MMDCCLXXIII"))
print(is_roman_number("CCCMMMVIIVV"))
print(is_roman_number("CVI"))