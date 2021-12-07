# def outer_func():
#     def inner_func():
#         print("Hello, world!")
#     inner_func()
#
#
# outer_func()

# def fun1():
#     a = 6
#
#     def fun(b):
#         a = 4
#         print("Сумма внутренней функции а: ", a + b)
#
#     fun(4)
#     print("Значение внешней переменной а: ", a)
#
#
# fun1()

# x = 25

# def fn():
#     global t
#     a = 30
#     t = a
#     print('global: ', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal: ', a)
#         return
#
#     inner()
#     return
#
#
# fn()
#
# z = x + t
# print(z)


# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1
#             x1 = 55
#
#         fn3()
#         print('fn2.x1= ', x1)
#
#     fn2()
#     print('fn1.x1= ', x1)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print('result = ', result)


# def outer(a1, b1, a2, b2):
#     # a = 0
#     # b = 0
#     def inner():
#         # nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         return [a, b]
#
#     return inner()
#
#
# result = outer(2, 3, -1, 4)
# print('result = ', result)

# s = 0
#
#
# def fn(a, b, c):
#     def fn2(i, j):
#         return i * j
#
#     global s
#     s = 2 * fn2(a, b) + fn2(a, c) + fn2(c, b)
#     return s
#
#
# print(fn(2, 4, 6))
# print('s = ', s)
# print(fn(5, 8, 2))
# print('s = ', s)
# print(fn(1, 6, 8))
# print('s = ', s)


# s = 0
#
#
# def fn(a, b, c):
#     def fn2(i, j):
#         nonlocal s
#         s += i * j
#
#     fn2(a, b)
#     fn2(a, c)
#     fn2(c, b)
#     return 2 * s
#
#
# print(fn(2, 4, 6))
# print('s = ', s)
# print(fn(5, 8, 2))
# print('s = ', s)
# print(fn(1, 6, 8))
# print('s = ', s)

# closure ()
# def inc(n):
#     def inner_inc(x):
#         return n + x
#     return inner_inc
#
#
# a = inc(12)
# print(a(5))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_class_filter(lower, upper):
#     def class_students(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_students
#
#
# a = make_class_filter(80, 100)
# b = make_class_filter(70, 80)
# c = make_class_filter(50, 70)
# d = make_class_filter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj = func(5, 2)
# print(obj.add())
#
# obj1 = func(5, 2)
# print(obj1.sub())
#
# obj2 = func(5, 2)
# print(obj1.mul())


# print((lambda x, y: x + y)(1, 2))

# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: (x ** 2) + (y ** 2))(2, 5))


# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# print(summ(10, 20, 30))


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5))
# print(func1('a', 'b', 'c', 'd'))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(0))
# print(f(3))

print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))
