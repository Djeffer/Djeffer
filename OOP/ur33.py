# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.note = self.LaptopSpecifications()
#
#     def print_name(self):
#         print(self.name, end="")
#         self.note.print_laptop()
#
#     class LaptopSpecifications:
#         def __init__(self):
#             self.model = "HP"
#             self.processor = "i7"
#             self.memory = 16
#
#         def print_laptop(self):
#             print(f' => {self.model}, {self.processor}, {self.memory}')
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.print_name()
# s2.print_name()

#Миксины (Mixins)


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fn:
#             fn.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# sub = MySubClass()
# sub.display("Эта строка будет отображаться и записываться в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар продан в 00:00 часов')
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook('HP', 1.5, 350000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())
# n = NoteBook('HP', 0.5, 350000)
# n.print_info()
# n.save_sell_log()

### Перегрузка операндов

class Clock:
    __Day = 86400  #24*60*60 - число секунд в сутках

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целом числом")

        self.__secs = secs % self.__Day

    def get_format_time(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # минуты
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs + other.__secs)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs - other.__secs)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs * other.__secs)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs // other.__secs)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть Clock")

        return Clock(self.__secs % other.__secs)

    def __eq__(self, other):
        return self.__secs == other.__secs
        # if self.__secs == other.__secs:
        #     return True
        # return False

    def __ne__(self, other):
        return not self.__eq__(other)


# c1 = Clock(600)
# c2 = Clock(200)
# print(f'c1: {c1.get_format_time()}')
# c3 = c1 - c2
# print(f'c1 - c2: {c3.get_format_time()}')
# c3 = c1 * c2
# print(f'c1 * c2: {c3.get_format_time()}')
# c3 = c1 // c2
# print(f'c1 // c2: {c3.get_format_time()}')
# c3 = c1 % c2
# print(f'c1 % c2: {c3.get_format_time()}')
# print(c3.get_format_time())
# c4 = c1 + c2 + c3
# print(c4.get_format_time())
c1 = Clock(200)
print(f'c1: {c1.get_format_time()}')
c2 = Clock(200)
print(f'c2: {c2.get_format_time()}')
c3 = Clock(300)
print(f'c3: {c3.get_format_time()}')
if c1 == c2:
    print("Время одинаковое")
if c1 != c3:
    print("Время разное")
