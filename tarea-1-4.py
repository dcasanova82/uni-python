"""
Ejercicio 4
===========
"""
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lc = [i[-1] for i in x]
print('Last column of the matrix: {}'.format(lc))

vts = [(j[round(len(j)/2)-1]**2)*2 for j in x]
print('Vector of twice the sware of the middle column: {}'.format(vts))