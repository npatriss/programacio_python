# RO_pag95_exercici3.py
from math import *

longitud = float(input("Ingresa la longitud del bloc rectangular: "))
ample = float(input("Ingresa el ample del bloc rectangular: "))
altura = float(input("Ingresa la altura del bloc rectangular: "))

diagonal_cara1 = (longitud**2 + ample**2)**0.5
diagonal_cara2 = (longitud**2 + altura**2)**0.5
diagonal_cara3 = (ample**2 + altura**2)**0.5

elif diagonal_cara1 >= diagonal_cara2 and diagonal_cara1 >= diagonal_cara3:
    major_diagonal = diagonal_cara1
    print ("La diagonal més gran és la diagonal de la cara 1 = ", major_diagonal)
elif diagonal_cara2 >= diagonal_cara1 and diagonal_cara2 >= diagonal_cara3:
    major_diagonal = diagonal_cara2
    print ("La diagonal més gran és la diagonal de la cara 2 = ", major_diagonal)
else:
    major_diagonal = diagonal_cara3
    print ("La diagonal més gran és la diagonal de la cara 3 = ", major_diagonal)

