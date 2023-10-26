# Variables
print('-' * 200)
print("Variables")
print()
_user_code = 'user_01'
user_name = 'Albeiro'
user_lastname = 'Ramos'
user_age = 40
user_height = 1.72
user_blood_gr = 'O'
user_blood_tp = '+'
user_is_activate = True
print("     _user_code = 'user_01'")
print("     user_name = 'Albeiro'")
print("     user_lastname = 'Ramos'")
print("     user_age = 40")
print("     user_height = 1.72")
print("     user_blood_gr = 'O'")
print("     user_blood_tp = '+'")
print("     user_is_activate = True")
print()

# Concatenar    : print( , )
print('-' * 200)
print("Concatenar    : print( , )")
print()
print("print('Mi código de usuario es', _user_code,'. Soy', user_name, user_lastname, ', tengo', user_age, 'años ,', 'mi altura es de', + user_height, 'mts , mi tipo de sangre es', user_blood_gr, user_blood_tp, ', aparezco activo en el sistema, es decir, como', user_is_activate)")
print('\nMi código de usuario es', _user_code,'. Soy', user_name, user_lastname, ', tengo', user_age, 'años ,', 'mi altura es de', user_height, 'mts , mi tipo de sangre es', user_blood_gr, user_blood_tp, ', aparezco activo en el sistema, es decir, como', user_is_activate)
print()

# Concatenar    : +
print('-' * 200)
print("Concatenar    : +")
print()
template = 'Mi código de usuario es ' + _user_code + '. Soy ' + user_name + ' ' + user_lastname + ', tengo ' + str(user_age) + ' años,'
print("     template = _user_code + '. ' + 'Hola, mi nombre es ' + user_name + ' y mi apellido es ' + user_lastname")
print("     print(template) =", template)
print()

# Concatenar strings : f {}
print('-' * 200)
print("Concatenar strings : f {}")
print()
template = f'{_user_code}. Hola, mi nombre es {user_name} y mi apellido es {user_lastname}'
print("     template = f'{_user_code}. Hola, mi nombre es {name} y mi apellido es {user_lastname}'")
print("     print(template) =", template)
print()

# Concatenar strings    : format()
print('-' * 200)
print("Concatenar strings : format()")
print()
template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(_user_code, user_name, user_lastname)
print("     template = '{}. Hola, mi nombre es {} y mi apellido es {}'.format(_user_code, user_name, user_lastname)")
print("     print(template) =", template)
print()
print('-' * 200)
print()