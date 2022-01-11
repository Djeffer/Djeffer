# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_w(weight)
#         self. verity_ps(ps)
#
#         self.fio = fio.split()
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = " ".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом от 18 до 100 лет.")
#
#     @classmethod
#     def verify_w(cls, w):
#         if not isinstance(w, (int, float)) or w < 25:
#             raise TypeError("Вес должен быть числом от 25 кг и выше")
#
#     @classmethod
#     def verity_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспортные данные должны быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     # @property
#     # def fio(self):
#     #     return self.__fio
#     #
#     # @fio.setter
#     # def fio(self, fio):
#     #     self.verify_fio(fio)
#     #     self.__fio = fio
#
#     # @property
#     # def old(self):
#     #     return self.__old
#     #
#     # @old.setter
#     # def old(self, old):
#     #     self.verify_fio(old)
#     #     self.__old = old
#     #
#     # @property
#     # def weight(self):
#     #     return self.__weight
#     #
#     # @weight.setter
#     # def weight(self, weight):
#     #     self.verify_w(weight)
#     #     self.__weight = weight
#     #
#     # @property
#     # def ps(self):
#     #     return self.password
#     #
#     # @ps.setter
#     # def ps(self, ps):
#     #     self.verity_ps(ps)
#     #     self.password = ps
#
#
# p1 = UserDate("Иванов Иван Иванович", 26, '1234 123456', 80.8)
# p1.weight = 60
# p1.old = 40
# print(p1.__init__)
from math import *


class Table:

    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length = length
        else:
            self._radius = radius

    def set_radius(self, radius):
        self._radius = radius

    def set_sides(self, width=None, length=None):
        if length in None:
            self._width = self._length = width
        else:
            self._width = width
            self._length = length

    def calc_area(self):
        raise NotImplementedError("В дочерним классе должен быть определен метод calc_area")


class Sq_table(Table):
    def calc_area(self):
        return self._width * self._length


class Round_table(Table):
    def calc_area(self):
        return pi * self._radius ** 2


t = Sq_table(20, 10)
t.set_sides(2)
print(t.__dict__)
print(t.calc_area())

t1 = Round_table(radius=10)
print(t1.__dict__)
print(t1.calc_area())

t2 = Round_table(radius=12)
print(t2.__dict__)
print(t2.calc_area())
t2.set_radius(60)
print(t2.__dict__)
print(t2.calc_area())
