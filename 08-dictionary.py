person = {
    'name': 'Raph',
    'last_name': 'Ortiz',
    'age': 38,
    'stack': ['Angular', 'Ionic', 'Python']
}

print(person)

# Update the value of a key
person['name'] = 'Raphael'
person['last_name'] = 'Ortiz Vergara'
person['age'] = 40

# Add a new key
#person.append('.Net')

# Add a new value to the 'last_name' list
person['stack'].append('NodeJS')

# Delete a key
del person['age']
person.pop('stack')

print(person)