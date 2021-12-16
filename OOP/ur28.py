# class Point:
#     __slots__ = ['__x', '__y', 'z']
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property  # геттер
#     def coords_x(self):
#         print('Вызов __get_coords_x')
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             raise ValueError('Неверный формат данных')
#
#     @coords_x.deleter
#     def coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# del p1.coords_x
# p1.coords_x = 7
# print(p1.coords_x)
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(f'{w.kg} кг ==> {w.to_pounds()} фунтов')
# w.kg = 41
# print(f'{w.kg} кг ==> {w.to_pounds()} фунтов')
# w.kg = 'десять'

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
# # def get_count():
# #     return Point.count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())
# print(get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))

# class Numbers:
#     def __init__(self):
#
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         if b > a and b > c and b > d:
#             return b
#         if c > a and c > b and c > d:
#             return c
#         if d > a and d > b and d > c:
#             return d
#
#     @staticmethod
#     def sred(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(x):
#         f = 1
#         for i in range(1, x + 1):
#             f *= i
#         return
#
#
# # print(Numbers.max(1, 2, 3, 4))
# # print(Numbers.min(1, 2, 3, 4))
# # print(Numbers.cred(1, 2, 3, 4))
# print(Numbers.factorial(4))

# class Date:
#     def __init__(self, day=0, mouth=0, year=0):
#         self.day = day
#         self.mouth = mouth
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
#     def string_to_db(self):
#         return f'{self.year}-{self.mouth}-{self.day}'
#
#
# dates = [
#     '30.12.2021',
#     '30-12-2021',
#     '01.01.2011',
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date =Date.from_string(d)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print('Неправельная дата или формат строки с датой')

# d = '16.12.2021'
# day, month, year = map(int, d.split('.'))
# print(day, month, year)
# date = Date(day, month, year)
# d = Date()
# date = d.from_string('16.12.2021')
# print(date.string_to_db())
# d1 = Date()
# date1 = d1.from_string('03.12.2021')
# print(date1.string_to_db())
# date2 = Date.from_string("15.10.2021")
# print(date2.string_to_db())


class Ploshad:
    count = 0

    @staticmethod
    def rectangle_geron(a, b, c):
        perimeter = (a + b + c) / 2
        return (perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c)) ** 0.5

    @staticmethod
    def osnovanie_visota(a, h):
        return 0.5 * h * a

    @staticmethod
    def ploshad_sq(a):
        return a ** 2

    @staticmethod
    def ploshad_tr(a, b):
        Ploshad.count += 1
        return a * b


print(Ploshad.rectangle_geron(3, 4, 5))
print(Ploshad.osnovanie_visota(6, 7))
print(Ploshad.ploshad_sq(7))
print(Ploshad.ploshad_tr(2, 6))
try_t = Ploshad()
print(try_t.rectangle_geron(1, 2, 3))
print(Ploshad.count)
