# RO_pag146_exercici1.py
from math import *

n = int(input("Nombre de paquets:"))
pes1 = float(input("Pes 1:"))
valor_minim = pes1
valor_maxim = pes1
x = 1
suma = 0

while x != n :
    d = float(input(f"Pes {x +1}:"))
    x = x + 1
    suma += d 
    if d >= valor_maxim:
        valor_maxim = d
    elif d <= valor_minim:
        valor_minim = d
        
suma = pes1 + suma
mitjana = suma / (n)

print("La mitjana és",mitjana)
print("El valor màxim és",valor_maxim)
print("El valor mínim és",valor_minim)