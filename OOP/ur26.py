# Класс - тип, описывающий устройство объектов
# Свойства = переменные
# Методы = функции
# атрибуты = свойства + методы
# class Point:
#     """Класс для предоставления координат точек"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# Point.set_coords(p1, 3, 8)

# print(type(p1))
# print(type(p1) == Point)
# print(isinstance(p1, Point))


# print(p1.__dict__)
# print(p1.x, p1.y, Point.x)
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y, Point.x)
# print(p1.__dict__)
# print(Point.__dict__)
# setattr(p1, "z", 7)
# print(getattr(p1, "z", "False"))
# print(hasattr(p1, "x"))
# print(hasattr(p1, "z"))
# delattr(p1, 'z')

# print(p2.__dict__)
# print(p2.x, p2.y)
# Point.x = 100
# print(p1.x, p1.y)
# print(id(Point))
# print(id(p1))

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '7-000-000-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'Street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождение: {self.birthday}\n'
#               f'Номер телефона: {self.phone}\nСтрана: {self.country}\n'
#               f'Город: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, name, birthday, phone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         """устанвливает имя"""
#         self.name = name
#
#     def get_name(self):
#         """Получаем имя"""
#         return self.name
#
#     def set_birthday(self, birthday):
#         """устанвливает дату рождение"""
#         self.birthday = birthday
#
#     def get_birthday(self):
#         """Получаем дату рождение"""
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', '7-900-900-90-90', 'Россия', 'Москва', 'Чистопрудный бульварб 1А')
# h1.print_info()
# h1.set_name('Ирина')
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday("12.12.2021")
# print(h1.get_birthday())
# h1.print_info()


# class car:
#     name = 'name'
#     year = '0000'
#     car_work = 'car_work'
#     engine_power = 'engine_power'
#     color = 'color'
#     price = 'price'
#
#     def print_info(self):
#         print(' Данные автомобиля '.center(40, '*'))
#         print(f'Название модели: {self.name}\nГод выпуска: {self.year}\n'
#               f'Производитель: {self.car_work}\nМощность двигателя: {self.engine_power}\n'
#               f'Цвет машины: {self.color}\nЦена: {self.price}')
#         print('=' * 40)
#
#     def input_info(self, name, year, car_work, engine_power, color, price):
#         self.name = name
#         self.year = year
#         self.car_work = car_work
#         self.engine_power = engine_power
#         self.color = color
#         self.price = price
#
#     def set_name(self, name):
#         """Принимаем имя"""
#         self.name = name
#
#     def get_name(self):
#         """Устанавлеваем имя"""
#         return self.name
#
#     def set_year(self, year):
#         """Принимаем год"""
#         self.year = year
#
#     def get_year(self):
#         """Устанавлеваем год"""
#         return self.year
#
#     def set_car_work(self, car_work):
#         """Принимаем производителя"""
#         self.car_work = car_work
#
#     def get_car_work(self):
#         """Устанавлеваем производителя"""
#         return self.car_work
#
#     def set_engine_power(self, engine_power):
#         """Принимаем можность"""
#         self.car_work = engine_power
#
#     def get_engine_power(self):
#         """Устанавлеваем мощность"""
#         return self.engine_power
#
#
# h1 = car()
# h1.input_info('X7 M50i', '2021', 'BMW', '530 л.с', 'white', '10790000')
# h1.print_info()

class Person:
    """Переменная для класификации сотрудника"""
    skill = 10

    def print_info(self, name, surname):
        self.name = name
        self.surname = surname
        print(f'Данные сотрудника: {self.name} {self.surname}')

    def add_skill(self, k):
        self.skill += k
        print(f'Квалификация {self.name}: {self.skill}')


p1 = Person()
p1.print_info('Viktor', 'Reznik')
p1.add_skill(3)
p2 = Person()
p2.print_info('Anna', 'Dolgih')
p2.add_skill(2)