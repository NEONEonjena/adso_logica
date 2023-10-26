# Iniciar variables int
print('-' * 50)
print("Iniciar variables int")
print()
age = 12
temperature_mas = 12.12
temperature_menos = -12.12
print("     age = 12")
print("     temperature = 12.12")
print("     temperature_menos = -12.12")
print()

#
print('-' * 50)
print("Expresiones aritméticas")
print()
lives = 12 + 15
print(lives)
lives = lives - 1
print(lives)
lives -= 1 
print(lives)
lives -= 5
print(lives)
lives += 5
print(lives)
number = 45000000000000000.1
print(number)
number_b = 0.000000000000000001
print(number_b)

x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
y_str = format(y, ".2g")
print('str => ', y_str)
print(y_str == str(x))
print('*' * 10)
print(y, x)
tolerance = 0.00001
print(abs(x - y) < tolerance)
