my_dict = {}
print(type(my_dict))
my_dict = {
    'avion': "bla bla bla",
    'name': "Nicolás",
    'last_name': "Molina Monroy",
    'age': 87
}
print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('unvalor'))
print('avion' in my_dict)
print('otroqueno' in my_dict)

person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age': 99,
}
print(person)

# Actualización
person['name'] = 'Santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)
# Eliminar
del person['last_name']
person.pop('age')
print(person)
# items, keys, values
print('items')
print(person.items())
print('keys')
print(person.keys())
print('values')
print(person.values())
