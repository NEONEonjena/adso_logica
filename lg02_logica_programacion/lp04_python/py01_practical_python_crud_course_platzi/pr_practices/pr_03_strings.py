# Iniciar variables string
print("\nIniciar variables string")
print()
character = '1'
name = 'Albeiro'
last_name = 'Ramos'
print("     character = '1'")
print("     name = 'Albeiro'")
print("     last_name = 'Ramos'")

# Concatenar strings : ,
print("\nConcatenar strings : ,")
print()
print("     print(character, '. Hola, mi nombre es', name, 'y mi apellido es', last_name)")
print("     =", character, '. Hola, mi nombre es', name, 'y mi apellido es', last_name)

# Concatenar strings : +
print("\nConcatenar strings : +")
print()
template = character + '. ' + 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name
print("     template = character + '. ' + 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name")
print("     print(template) =", template)

# Concatenar strings    : format()
print("\nConcatenar strings : f {}")
print()
template = f'{character}. Hola, mi nombre es {name} y mi apellido es {last_name}'
print("     template = f'{character}. Hola, mi nombre es {name} y mi apellido es {last_name}'")
print("     print(template) =", template)

# Concatenar strings    : format()
print("\nConcatenar strings : format()")
print()
template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(character, name, last_name)
print("     template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(character, name, last_name)")
print("     print(template) =", template)

print()