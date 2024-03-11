# RO_pag83_exercici4.py
from math import *

a =int(input("Número enter de 3 xifres = "))

if 100 <= a <= 999:
    nombre_invertit = int(str(a)[::-1])

    print(f"Número invertit: {nombre_invertit}")
else:
    print("Siusplau, Introdueix un número de tres xifres.")