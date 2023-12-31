numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(type(numbers))
print(strings)
print(type(strings))
'''
# CRUD: No se puede hacer (inmutables -> solo de lectura)
numbers.append(1)
print(numbers)
'''
print(strings)
print(strings.index('zule'))
print(strings.count('nico'))
my_list = list(strings)
print(my_list)
print(type(my_list))
my_list[1] = 'juli'
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

print()
# Tuplas
print(40*"*", "Tuplas", 40*"*")
print()
a = 1, 2, 3
print("     a = 1, 2, 3")
print("     print(a) =", a)
print("     print(type(a)) =", type(a))
print()
a = (1, 2, 3)
print("     a = (1, 2, 3)")
print("     print(a) =", a)
print("     print(type(a)) =", type(a))
print()
print("     a[0] =", a[0])
print("     a[1] =", a[1])
print("     a[2] =", a[2])
print()
# count()  : Cuenta valores repetidos
print("count()  : Cuenta valores repetidos")
print()
a = (1, 1, 1, 2, 3, 4)
print("     a = (1, 1, 1, 2, 3, 4)")
print("     print(a.count(1)) =", a.count(1))
print()
# index()  : Muestra el índice del primer valor repetido
print("index()  : Muestra el índice del primer valor repetido")
print()
print("     print(a.index(1)) =", a.index(1))
print("     print(a.index(3)) =", a.index(3))
print()
# Conjuntos
print(39*"*", "Conjuntos", 38*"*")
print()
a = set([1, 2, 3])
b = {3, 4, 5}
print("     a = set([1, 2, 3])")
print("     b = {3, 4, 5}")
print("     print(type(a)) =", type(a))
print("     print(type(b)) =", type(b))
print()
print("add()            : Agrega valor si no existe")
print()
a.add(3)
print("     a.add(3)")
print("     print(a) =", a)
print()
a.add(20)
print("     a.add(20)")
print("     print(a) =", a)
print()
print("intersection()   : Intersección")
print()
print("     print(a.intersection(b)) =", a.intersection(b))
print()
print("union()          : Unión")
print()
print("     print(a.union(b)) =", a.union(b))
print()
print("difference()     : Diferencia")
print()
print("     print(a.difference(b)) =", a.difference(b))
print("     print(b.difference(a)) =", b.difference(a))
print()
print("revome()         : Eliminar elemento")
print()
a.remove(20)
print("     a.remove(20)")
print("     print(a) =", a)
print()


print()
