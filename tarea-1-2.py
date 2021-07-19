"""
Ejercicio 2
===========
"""
try:
    n1 = float(input('Enter the first number: '))
    n2 = float(input('Enter the second number: '))
    op = str(input('Enter the operator (+,-,*,/): '))
    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        res = n1 / n2
    else:
        print('Invalid operator selected')
    print('The final result is {}'.format(res))
except ValueError:
    print('Invalid numbers selected!')