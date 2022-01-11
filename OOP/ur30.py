# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Значние ширины должно быть больше нуля")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Значние высоты должно быть больше нуля")
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         # return self.color
#         return self.width * self.height
#         # return self.border_new()
#
#
# rect = Rectangle(10, 20, "green", "1px solid gray")
# print(rect.area())
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.border)
# rect.width = 50
# print(rect.width)
# print(rect.area())


class Liquid:  # жидкость
    def __init__(self, name, density):
        self._name = name
        self._density = density  # плотность жидкости
    def edit_density(self, val):  # изменение плотности
        self._density = val
    def calc_v(self, m):  # вычисление объема жидкости, соответствующего заданной массе
        res = m / self._density
        print(f"Объем {m} кг {self._name} равен {res} m^3/")
        return res

    def calc_m(self, v): # вычисление массы жидкости соотвертствующее заданному объему
        res = v * self._density
        print()
        return res


    def print_info(self):
        print(f"Жидкость {self._name} плотность = {self._density} kg/m^3.")

