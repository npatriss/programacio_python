# RO_pag146_exercici2.py
from math import *

n = int(input("Objectes a la bodega:"))
x = 0
grup1 = 0
grup2 = 0
grup3 = 0
while x != n :
    x = x + 1
    pes = float(input(f"Pes {x}:"))
    if pes < 10:
        grup1 += 1
    elif pes >= 10 and pes <= 20:
        grup2 += 1
    elif pes > 20 :
        grup3 += 1
        
print(grup1,"objectes pesen menys que 10 kg")
print(grup2,"objectes pesen entre 10 i 20 kg")
print(grup3,"objectes pesen més de 20 kg")