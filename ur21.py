# Рекурсия


# def elevator(n):
#     if n == 0:
#         print("Вы в падвале")
#         return
#     print("->", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "->", lst[0])
#         return lst[0]
#     else:
#         print(lst, "->", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']


# def count_items(items_list):
#     count = 0
#     for items in items_list:
#         if isinstance(items, list):
#             count += count_items(items)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# print(type(names[1]) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(len(names))


# def coutn_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count

# print(coutn_items(names))

# def union(s):
#     if not s: # пустой список s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\tWorld Hi  "))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

def binary_search(s, item):
    first = 0
    last = len(s) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


lst = [1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(lst, 3))
print(binary_search(lst, 1))
