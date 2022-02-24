# import requests
# import json
#
# response = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num in top_users:
#     if num < max_complete:
#         break
#     users.append(str(user))
#
# max_users = ' and '.join(users)
#
# s = 's' if len(users) > 1 else ''
# print(f'user{s} {max_users} complete {max_complete} TODOs')

# import csv
#
# with open('data.csv') as f:
#     fields_name = ["Имя", "Профессия", "Год рождения"]
#     reader = csv.DictReader(f, fieldnames=fields_name) #delimiter=';'
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f'Файл содержит столбцы: {"; ".join(row)}')
#         print(f'{row["Имя"]} - {row["Профессия"]}. ', end="")
#         print(f'Родился в {row["Год рождения"]} году.')
#         count += 1
#     print(f'Всего в файле {count + 1} строки.')
import csv

# with open('studetn.csv', mode='w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Imia', 'Klass', 'Vozrast'])
#     writer.writerow(['Jenia', '9', '15'])
#     writer.writerow(['Ivan', '5', '12'])
#     writer.writerow(['Sasha', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open('sw_data.csv') as f:
#     print(f.read())

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)
#
# with open('sw_data.csv') as f:
#     print(f.read())

# with open('studetn1.csv', mode='w') as f:
#     names = ['Имя', "Возраст"]
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Анна", "Возраст": "30"})
#     writer.writerow({"Имя": "Евгений", "Возраст": "31"})
#     writer.writerow({"Имя": "Данила", "Возраст": "10"})

data = [{
    'hostname': 'sw1',
    'location': 'London',
    'model': '3750',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw2',
    'location': 'Liverpool',
    'model': '3850',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw3',
    'location': 'Liverpool',
    'model': '3650',
    'vendor': 'Cisco'
}, {
    'hostname': 'sw4',
    'location': 'London',
    'model': '3650',
    'vendor': 'Cisco'
}]

with open('dict.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
    writer.writeheader()
    for row in data:
        writer.writerow(row)

with open('dict.csv') as f:
    print(f.read())
