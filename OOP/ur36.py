# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)
#             return res ** self.arg
#         return wrapper
#
#
# @Power(3)
# def multuple(a, b):
#     return a * b
#
#
# print("Результат: ", multuple(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self. surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))

# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет.")
#         print(text, end=" ")
#         return klass(text)
#
#
# @Message.register('Telegram')
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
#
# @Message.register('WhatsApp')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
# @Message.register('VK')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(VK)")
#
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create('WhatsApp', "new text")
# m2.send()
# m3 = Message.create("VK", "text text")
# m3.send()


# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#

# p = Person('Ivan', "Nikolaev")

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#
# p = Person('Ivan', "Nikolaev")
# print(p.name.get())
# p.name.set("Igor")
# print(p.name.get())

####Дескриптор (__get__(), __set__(), __delete__(), __set_name__())

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть  строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Ivan', "Nikolaev")
# print(p.name)
# p.name = 'Igor'
# print(p.name)
# print(p.surname)


# non-data descriptor (дескриптор не данных). Тoлько __get__
# data descriptor - дескриптор данных.


# Метоклассы

# a = 5
# print(type(a))
# print(type(int))


# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())


# MyList = type(
#     'Mylist',
#     (list, ),
#     dict(get_length=lambda self: len(self))
# )
#
# lst = MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())


class MyMetaClass(type):
    def __new__(mcs, name, bases, attr):
        print('Создание нового объекта', name)
        return super(MyMetaClass, mcs).__new__(mcs, name, bases, attr)

    def __init__(cls, name, bases, attr):
        print('Иницилизация класса', name)
        super(MyMetaClass, cls).__init__(name, bases, attr)


class Student(metaclass=MyMetaClass):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


s = Student('Anna')
print(s.get_name())