print()
# Strings
print("Strings")
print()
country = 'Colombia'
platzi = 'platzi'
print("     country = 'Colombia'")
print("     platzi = 'platzi'")
print()
# Imprimir un caracter
print("Caracter con el índice: cadena[#]")
print("     print(country[0]) =", country[0])
print("     print(country[1]) =", country[1])
print("     print(country[2]) =", country[2])
print("     print(country[3]) =", country[3])
print("     print(country[4]) =", country[4])
print("     print(country[5]) =", country[5])
print("     print(country[6]) =", country[6])
print("     print(country[7]) =", country[7])
print()
print("     print(country[-1]) =", country[-1])
print("     print(country[-2]) =", country[-2])
print("     print(country[-3]) =", country[-3])
print("     print(country[-4]) =", country[-4])
print("     print(country[-5]) =", country[-5])
print("     print(country[-6]) =", country[-6])
print("     print(country[-7]) =", country[-7])
print("     print(country[-8]) =", country[-8])
print()
# len()
print("Longitud de la cadena: len()")
print("     print(len(country)) =", len(country))
print()
# id()
print("Posición en memoria: id()")
second_letter = country[0]
print("     second_letter = country[1]")
print("     print(second_letter) =", second_letter)
print("     print(id(second_letter)) =", id(second_letter))
print()
# Mayúsculas: upper()
print("Convertir a mayúsculas: upper()")
print("     print(platzi.upper()) =", platzi.upper())
print()
# Encontrar: find()
print("Encontrar texto: find()")
print("     print(platzi.find('la')) =", platzi.find('la'))
print()
# Empieza con un texto: startswith()
print("Encontrar si empieza con un texto: startswith()")
print("     print(platzi.startswith('p')) =", platzi.startswith('p'))
print("     print(platzi.startswith('x')) =", platzi.startswith('x'))
print()
# Global (Muestra los métodos de un objeto): dir()
print("Global (Muestra los métodos de un objeto): dir()")
print("     print(dir(platzi)) =", dir(platzi))
print()
# Global (docstrings, comentarios o ayuda que posee una función): help()
print("Global (docstrings, comentarios o ayuda que posee una función): help()")
print()
def my_function():
    """Este es un texto de ayuda de cómo utilizar esta función"""
    pass

print('     def my_function():')
print('         """Este es un texto de ayuda de cómo utilizar esta función"""')
print('         pass')
print()
print('     help(my_function) =')
print()
help(my_function)
# Slices: rebanadas
print("Slices: Rebanadas")
print()
fruit = 'banana'
print("     fruit = 'banana'")
print()
print("     print(fruit[0]) =", fruit[0])
print("     print(fruit[-1]) =", fruit[-1])
print("     print(fruit[0:3]) =", fruit[0:3])
print("     print(fruit[::2]) =", fruit[::2])
print("     print(fruit[3:3]) =", fruit[3:3])
print("     print(fruit[:]) =", fruit[:])
print("     print(fruit[1:-1:2]) =", fruit[1:-1:2])
print()
long_word = 'ferrocarril'
print("     long_word = 'ferrocarril'")
print()
print("     print(long_word[1:4]) =", long_word[1:4])
print("     print(long_word[1:8]) =", long_word[1:8])
print("     print(long_word[::-1]) =", long_word[::-1])
print("     print(long_word[:8:3]) =", long_word[:8:3])
print("     print(long_word[::2]) =", long_word[::2])


print()