import copy
print()
# Listas
print("Listas")
print()
print("Listas literales")
print()
countries = ['Mexico','Venezuela','Colombia','Argentina']
ages = [12,18,24,34,50]
receta = ['Ensalada',2,'Lechuga',5,'Tomates']
print("     countries = ['Mexico','Venezuela','Colombia','Argentina']")
print("     ages = [12,18,24,34,50]")
print("     receta = ['Ensalada',2,'Lechuga',5,'Tomates']")
print()
print("     print(countries) =", countries)
print("     print(ages) =", ages)
print("     print(receta) =", receta)
print()
# Cambiar valor de una lista
print("Cambiar valor de una lista")
print()
countries[0] = 'Ecuador'
print("     countries[0] = 'Ecuador'")
print("     print(countries) =", countries)
print()
# Clonar una lista
print("Clonar una lista")
print()
global_countries = countries
countries[0] = 'Guatemala'
print("     global_countries = countries")
print("     countries[0] = 'Guatemala'")
print()
print("     print(countries) =", countries)
print("     print(global_countries) =", global_countries)
print()
# Copiar una lista
print("Copiar una lista")
print()
print("     import copy. Importar librería copy al principio del archivo")
print()
global_countries = None
global_countries = copy.copy(countries)
countries[0] = 'Honduras'
print("     global_countries = None")
print("     global_countries = copy.copy(countries)")
print("     countries[0] = 'Honduras'")
print()
print("     print(countries) =", countries)
print("     print(global_countries) =", global_countries)
print()
# Imprimir una lista
print("Imprimir una lista")
print()
print("     for country in countries:")
print("         print(country)")
print()
for country in countries:
    print("     ", country)

print()