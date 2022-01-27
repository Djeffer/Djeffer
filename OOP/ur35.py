# from abc import ABC, abstractmethod
#
#
# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'{self.last_name} {self.first_name} {self.age}')
#
#
# class Student(Human):
#     def __init__(self, spec, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f'{self.speciality} {self.group} {self.rating}', end=' ')
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, spec, experience, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         print(f'{self.speciality} {self.experience}', end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, spec, group, rating, last_name, first_name, age):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         print(f'{self.topic}', end=' ')
#         super().info()
#
#
# group = [
#     Student('Батодалаев', "Даши", 16, "ГК", "Web_011", 5),
#     Student('Загидуллин', "Линар", 32, "РПО", "PD_011", 5),
#     Graduate('Шугани', "Сергей", 15, "РПО", "PD_011", 5, 'Защита персональных данных'),
#     Teacher('Даньшин', "Андрей", 38, "Астрофизика", 110),
#     Student('Маркин', "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher('Башкиров', "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#
# p = Point(1, 2)
# print(len(p))
# print(dir(Point))
import math


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)

# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print('pt =', pt.__sizeof__())
# print('pt2 =', pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'x', 'y', 'z'
#
#
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.z)
# print(pt3.__dict__)

# Функторы

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()

# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Аргумент должен быть строкой!')
#         return args[0].strip(self.__chars)
#
#
# s1 = StripsChars("?:;!. ")
# print(s1('  ?Hello World!  '))
#
#
# def strip_str(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Аргумент должен быть строкой!')
#         return string.strip(chars)
#
#
# s2 = StripsChars("?:;!. ")
# print(s2('  ?Hello World!  '))

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('перед вызовом функции')
#         self.func()
#         print('после вызова функции')
#
#
# @MyDecorator
# def function():
#     print('func')
#
#
# function()

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print('перед вызовом функции')
#         res = self.func(a, b)
#         print('после вызова функции')
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))

class MyDecorator:
    def __init__(self, agr):
        self.name = agr

    def __call__(self, func):
        def wrap(a, b):
            print('перед вызовом функции')
            print(self.name)
            func(a, b)
            print('после вызова функции')

        return wrap


@MyDecorator('test2')
def function(a, b):
    print(a, b)


function(2, 5)
