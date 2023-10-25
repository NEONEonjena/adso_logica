# Definir una función
print("\nDefinir una función")
print()
print("     def funcion (parámetros):")
print("         return valor")

# Alcance de las variables: globales y locales
print("\nAlcance de las variables: globales y locales")
print()
# x = 10  # variable global


# def funcion():
#     # global x
#     x = 5  # variable local
#     return x


# print(funcion())  # imprime 5
# print(x)  # imprime 5

# print

print("*" * 28, "Casos en Funciones", "*" * 28)

# Caso 01. Función SIN parámetros y SIN retorno de valor
print("\nCaso 01. Función SIN parámetros y SIN retorno de valor")
print()

num1 = 5
num2 = 10


def funcion_caso_01():
    res = num1 + num2    
    print('     = La suma de', num1, 'más', num2, 'es', res)


print("     num1 = 5")
print("     num2 = 10")
print()
print("     def funcion_caso_01():")
print("         res = num1 + num2")
print("         print('La suma de', num1, 'más', num2, 'es', res)")
print()
print("     funcion_caso_01()")
funcion_caso_01()

# Caso 02. Función CON parámetros y SIN retorno de valor
print("-" * 76)
print("\nCaso 02. Función CON parámetros y SIN retorno de valor")
print()


def funcion_caso_02(num1, num2):
    res = num1 + num2
    print('     = La suma de', num1, 'más', num2, 'es', res)


print("     def funcion_caso_02(num1, num2):")
print("         res = num1 + num2")
print("         print('La suma de', num1, 'más', num2, 'es', res)")
print()
print("     funcion_caso_02(5, 10)")
funcion_caso_02(5, 10)

# Caso 03. Función SIN parámetros y CON retorno de valor
print("-" * 76)
print("\nCaso 03. Función SIN parámetros y CON retorno de valor")
print()

num1 = 5
num2 = 10


def funcion_caso_03():    
    res = num1 + num2
    return res


print("     num1 = 5")
print("     num2 = 10")
print()
print("     def funcion_caso_03():")
print("         res = num1 + num2")
print("         return res")
print()
print("     print('La suma de', num1, 'más', num2, 'es', funcion_caso_03())")
print('     = La suma de', num1, 'más', num2, 'es', funcion_caso_03())

# Caso 04. Función CON parámetros y CON retorno de valor
print("-" * 76)
print("\nCaso 04. Función CON parámetros y CON retorno de valor")
print()


def funcion_caso_04(num1,num2):
    res = num1 + num2
    return res


print("     def funcion_caso_04(num1, num2):")
print("         res = num1 + num2")
print("         return res")
print()
print("     print('La suma de', num1, 'más', num2, 'es', funcion_caso_04(5, 10))")
print('     = La suma de', num1, 'más', num2, 'es', funcion_caso_04(5, 10))
print("-" * 76)
print()