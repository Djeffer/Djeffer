import os.path

# print(os.path.split(r'E:\Python\Python\pythonUr\one.txt'))  # разбивает путь на картеж(head, tail)
# print(os.path.dirname(r'E:\Python\Python\pythonUr\one.txt'))  # возвращает имя дириктории
# print(os.path.basename(r'E:\Python\Python\pythonUr\one.txt'))  # возвращает имя файла
# print(os.path.join(r'E:\Python', 'Python', 'pythonUr', 'one.txt'))  # соеденияет один или несколько компонентов
# # с учетом OS

# dirs = [r'Work\F1', 'Work\F2\F21']
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir2, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir2, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
# def print_tree(root, topdown):
#     print(f'Обход {root} {"Сверху вниз" if topdown else "Снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print('=' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# print(os.path.exists(r'E:\Python\Python\pythonUr\Work\w.txt'))  # проверяет путь на существование
# print(os.path.getctime(r'E:\Python\Python\pythonUr\Work\w.txt'))  # возвращвкет последение доступа к файлу
# print(os.path.getatime(r'E:\Python\Python\pythonUr\Work\w.txt'))  # возвращвкет последение изменение файла
# print(os.path.getsize(r'E:\Python\Python\pythonUr\Work\w.txt'))  # возвращвкет размер файла в байтах

import time

path = r'E:\Python\Python\pythonUr\Work\w.txt'
size = os.path.getsize(path)
kb = size / 1024
atime = os.path.getatime(path)
mtime = os.path.getmtime(path)
print('Размер: ', kb, 'KB')
print("Дата последнего испаользования: ", time.strftime('%d.%m.%Y, %H:%M:%S'))