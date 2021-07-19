"""
Ejecicio 1
==========
Asumimos que el usuario solo ingresa números válidos
"""
try:
    n = float(input('Enter a valid number (Type quit to end the program): '))
    if (n > 0):
        print('You have supplied a positive number')
    else:
        print('You have supplied a negative number')
except ValueError:
    print('Ese no es un número válido')
