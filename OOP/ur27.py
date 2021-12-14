# __МагическийМетод__

# Специальные методы
# конструктор __new__
# иницилизатор __init__
# деструктор __del__

# class Point:
#     count = 0
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("Конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         # print("Иницилизатор")
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#     # def __del__(self):
#     #     print("Удаление экземпляра: ", self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point(2, 3)
# print(Point.count)
# p3 = Point(2, 3)
# print(p3.count)
#
# # Point.__init__(p1, 20, 50)
# # print(p1.__dict__)
# # p2 = Point()
# # print(p2.__dict__)
# # p3 = Point(2)
# # print(p3.__dict__)


# def ininstance(z, int):
#     pass
#
#
# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def check_val(z):
#         if ininstance(z, int) or ininstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# p1.set_coords(2.6, 3.7)
# print(p1.__dict__)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Иницилизация робота: ", self.name)
#         Robot.k += 1
#
#     def sey_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним роботом.")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.sey_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.sey_hi()
# droid3 = Robot("PO")
# droid3.sey_hi()
# droid4 = Robot("P4")
# droid4.sey_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
#
# print("Числоность роботов:", Robot.k)
import math


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def check_val(z):
#         if ininstance(z, int) or ininstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)

# Инкапсуляция
# x - public (определяет элемент как общедоступный. обратиться к данной переменной или функции можно как в рамках
# класса, так и путем создания экземпляра класса.)
# _x - protected (определяет элемент как закрытый для доступа, обратиться к данной переменной или функции можно только в
# рамках нашего класса.)
# __x - private (определяет элемент как закрытый для доступа, обратиться к данной переменной или функции можно только в
# рамках нашего класса, а так же в классе наследнике.)


# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def print_rectangle(self):
#         return ('*' * self.__width + '\n') * self.__length
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print("Длина прямоугольника", rec1.get_length())
# print("Ширина прямоугольника", rec1.get_width())
# print('Площадь', rec1.square())
# print('Периметр', rec1.perimetr())
# print('Гипотенуза', round(rec1.hypo(), 2))
# print(rec1.print_rectangle())


class Point:
    WIDTH = 5
    z = 100

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # def __getattr__(self, name):
    #     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"
    # def __getattribute__(self, item):
    #     if item == "_Point__x":
    #         return "Закрытая переменная"
    #     else:
    #         return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("Нельзя менять значение")
        else:
            self.__dict__[key] = value

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coords(self, x, y):
        if Point.check_val(x) and Point.check_val(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def set_coords_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")

    def set_coords_y(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coords(self):
        return self.__x, self.__y

    def get_coords_x(self):
        return self.__x

    def get_coords_y(self):
        return self.__y

    def area(self):
        return (self.__x * self.__y) + self.z


p1 = Point(5, 10)
# # print(p1.__x)
# print(p1._Point__x)
# print(p1.get_coords())
# p1.get_coords(2, 3)
# print(p1.get_coords())
# p1.z = 200
Point.WIDTH = 10
print(p1.area())
