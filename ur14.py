# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))

# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst)
# c = next(b)
# print(c)

# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))

# my_dict = {'one': 'first'}
#
#
# def db(**kwargs):
#     my_dict.update(**kwargs)
#     return my_dict
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# print('my_dict = ', db(name='Bob', age=31, weight=61, eyes='grey'))