# Iniciar variables
print('-' * 100)
print("Iniciar variables")
print()
character = '1'
name = 'Albeiro'
last_name = 'Ramos'
print("     character = '1'")
print("     name = 'Albeiro'")
print("     last_name = 'Ramos'")
print()

# Concatenar strings : +
print('-' * 100)
print("Concatenar strings : +")
print()
template = character + '. ' + 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name
print("     template = character + '. ' + 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name")
print("     print(template) =", template)
print()

# Concatenar strings : f {}
print('-' * 100)
print("Concatenar strings : f {}")
print()
template = f'{character}. Hola, mi nombre es {name} y mi apellido es {last_name}'
print("     template = f'{character}. Hola, mi nombre es {name} y mi apellido es {last_name}'")
print("     print(template) =", template)
print()

# Concatenar strings    : format()
print('-' * 100)
print("Concatenar strings : format()")
print()
template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(character, name, last_name)
print("     template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(character, name, last_name)")
print("     print(template) =", template)
print()
print('-' * 100)
print()