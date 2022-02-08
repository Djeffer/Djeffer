# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f"Студент {self.name}: {a[:-2]}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f'Группа: {self.group}\n{a}'
#
#     def add_student(self, new_student):
#         self.students.append(new_student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tmp = {'Students': stud_list}
#             json.dump(tmp['Students'], f, indent=2)
#
#
# st1 = Student("Bodnya", [5, 4, 3, 2, 1])
# st2 = Student("Ivanov", [5, 2, 5, 4, 3])
# st3 = Student("Petrov", [3, 4, 4, 4, 2])
# Student.dump_to_json(st1, 'student.json')
# Student.load_from_file('student.json')
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
# my_group.dump_group('group.json', my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# Group.change_group(my_group, my_group2, 1)
# print(my_group)
# print(my_group2)

# print(st1)
# st1.add_marks(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 5)
# print(st1)
# print(st1.average_mark())
