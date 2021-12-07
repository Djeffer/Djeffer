# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# print(f.read(3))
# print(f.tell())  # 3
# print(f.seek(1))  # 1
# print(f.read())
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:
#     print(f.write('0123456789\ndsdfklsjdf'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])

# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# with open(file_name, 'w') as f:
#     f.write((get_line(lst)))
#
# print("Done!")


# with open(file_name, 'r') as f:
#     file_lst = f.read().split()
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))

# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open('text.txt', "r", encoding='utf-8') as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("text.txt"))


# with open("input.txt", "r") as f:
#     lst = f.read().split()
#     m = max(len(i) for i in lst)
#     print([i for i in lst if len(i) == m])


# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
#
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line, end="")

# os
# os.path

import os

# print('Текущая директория', os.getcwd())  # возвращает текущую директорию (там где наш документ *.py)
# print(os.listdir('..'))  # возвращает список дирикторий и файлов, находящие в текущей или в по указаному пути дириктории
# os.mkdir('ur23')  # Создает дирикторию по указаному пути
# os.makedirs('ur23/ur23-1')  # Создает конечную дирикторию по указаному пути и так же промежуточные папки, если их не было
# os.remove('res_1.txt')  # Удаление файлов
# os.rename('ur23', 'test')  # переименовывает файл или папку.
# os.rename('test/ts.txt', 'one.txt')  # Перенос файла в папку и переменовать его
# os.renames('one.txt', 'test1/ts.txt')  # созадет папку
# os.renames('test1/ts.txt', 'one.txt')  # удаляет папку
# os.rmdir('test')  # Удаление пустых папок, если она не пустая будет ошибка

# Возвращает имена объектов в дереве дириктории, обходя это дерево сверху вниз (topdown=True) или снизу вверх
# (topdown=False)
# for root, dirs, files in os.walk('ur23', topdown=True):
#     print('Root:', root)
#     print('Subdirs:', dirs)
#     print('Files:', files)

# for root, dirs, files in os.walk("Work", topdown=True):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f'Дириктория {root} удалина')

