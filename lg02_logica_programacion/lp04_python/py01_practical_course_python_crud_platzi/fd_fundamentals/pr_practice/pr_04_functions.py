# Definir una función
print("\nDefinir una función")
def suma_de_dos_numeros(x, y):
    return x + y
print("     def suma_de_dos_numeros(x,y):")
print("         return x + y")
print()
print("     print(suma_de_dos_numeros(10, 15)) =", suma_de_dos_numeros(10, 15))
print("     print(type(suma_de_dos_numeros)) =", type(suma_de_dos_numeros))

# Asignar valor de función a una variable
print("\nAsignar valor de una función a una variable")
suma_total = suma_de_dos_numeros(10, 15)
print("     suma_total = suma_de_dos_numeros(10, 15)")
print("     print(suma_total) =", suma_total)
print("     print(type(suma_total)) =", type(suma_total))
print()