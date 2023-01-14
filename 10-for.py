'''
for element in range(1,21):
    print(element)
'''

my_list = ['Raph', 'Raphael', 'Rapha', 'Raphy', 'Raphiel']
for name in my_list:
    print(name)

my_tuple = ('Gandalf', 'Aragorn', 'Legolas', 'Gimli', 'Frodo')
for name in my_tuple:
    print(name)

my_dictionary = {
    'id': 1,
    'article': 'Stone',
    'price': 100,
    'stock': 10
}
# for key in my_dictionary:
#     print(key, ': ', my_dictionary[key])

for key, value in my_dictionary.items():
    print(key, ': ', value)

# Iterar una lista de diccionarios
students = [
    {
        'id': 1,
        'name': 'Raph',
        'last_name': 'Ortiz',
        'age': 38
    },
    {
        'id': 2,
        'name': 'Oscar',
        'last_name': 'Naranjo',
        'age': 30
    },
    {
        'id': 3,
        'name': 'Bernardo',
        'last_name': 'Carrillo',
        'age': 21
    }
]

for student in students:
    print('Student name: ', student['name'])