"""
Ejercicio 3
===========
"""
try:
    n = int(input('Enter a valid integer number: '))
    f1 = []
    x = n
    i = 0
    while x > 0:
        if x == n:
            f1.append(x * (x - 1))
        else:
            f1.append(f1[i-1] * (x - 1))
        i += 1
        x -= 1
    f2 = []
    for j in range(n):
        if j == 0:   
            f2.append(1)
        else:
            f2.append(f2[j-1] * (j + 1))
    print('The factoral using a while loop is: {}'.format(f1[n-2]))
    print('The factoral using a for loop is: {}'.format(f2[n-1]))
except ValueError:
    print('Invalid input not an integer!')