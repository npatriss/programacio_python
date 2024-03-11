# RO_pag95_exercici5.py
from math import *

nombre =float(input("Ingresa un nombre: "))

if nombre.is_integer() and nombre % 7 == 0:
    print("El nombre es enter y multiple de 7.")
else:
    print("El nombre no es enter o no es multiple de 7.")