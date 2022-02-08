# import math
# from math import pi
#
# print(math.pi)
# from geometry import ur37_1, ur37_2, ur37_3
#
#
# def main():
#     r1 = ur37_1.Rectangle(1, 2)
#     r2 = ur37_1.Rectangle(3, 4)
#
#     s1 = ur37_2.Square(10)
#     s2 = ur37_2.Square(20)
#
#     t1 = ur37_3.Triangle(1, 2, 3)
#     t2 = ur37_3.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == "__main__":
#     main()

from car import electrocar

e = electrocar.ElectroCar('Tesla', 'S', 2018, 55000)
e.show_car()
e.description_battery()
