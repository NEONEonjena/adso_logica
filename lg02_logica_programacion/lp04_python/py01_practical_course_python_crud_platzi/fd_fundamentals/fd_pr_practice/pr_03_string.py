# Iniciar variables string
print("\nIniciar variables string")
print()
name = 'Albeiro'
last_name = 'Ramos'
print("     name = 'Albeiro'")
print("     last_name = 'Ramos'")
print("     print(name) =", name)
print("     print(last_name) =", last_name)

# Concatenar strings : +
print("\nConcatenar strings : +")
print()
full_name = name + ' ' + last_name
template = 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name
print("     full_name = name + ' ' + last_name")
print("     template = 'Hola, mi nombre es ' + name + ' y mi apellido es ' + last_name")
print("     print(full_name) =", full_name)
print("     print(template) =", template)

# Concatenar strings    : format()
print("\nConcatenar strings : f {}")
print()
template = f'Hola, mi nombre es {name} y mi apellido es {last_name}'
print("     template = f'Hola, mi nombre es {name} y mi apellido es {last_name}'")
print("     print(template) =", template)

# Concatenar strings    : format()
print("\nConcatenar strings : format()")
print()
template = 'Hola, mi nombre es {} y mi apellido es {}'.format(name, last_name)
print("     template = 'Hola, mi nombre es {} y mi apellido es {}'.format(name, last_name)")
print("     print(template) =", template)

print()