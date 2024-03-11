# RO_pag96_exercici11.py
from math import *

a1 = float(input("Ingresa la coordenada a del PRIMER PUNT: "))
b1 = float(input("Ingresa la coordenada b del PRIMER PUNT: "))

c1 = float(input("Ingresa la coordenada c del SEGON PUNT: "))
d1 = float(input("Ingresa la coordenada d del SEGON PUNT: "))

distancia1 = sqrt(a1**2 + b1**2)
distancia2 = sqrt(c1**2 + d1**2)

if distancia1 < distancia2 :
    print("Resultat = PUNT 1")

elif distancia2 < distancia1 :
    print("Resultat = PUNT 2")
    
else :
    print("Els dos punts estàn a la mateixa distància del punt origen.")
    