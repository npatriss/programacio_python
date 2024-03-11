#RO_pag95_exercici1.py
from math import *

radi=int(input("radi = "))
altura=int(input("altura = "))

if altura > radi :
    volum = 3.1416 * pow(radi, 2) * altura
    print ("Volum del cilindre en cm cubics = ", volum)
    
else :
    area = (2 * 3.1416 * radi * altura) + (2 * 3.1416 * pow(radi, 2))
    print ("Àrea del cilindre en cm quadrats = ", area)