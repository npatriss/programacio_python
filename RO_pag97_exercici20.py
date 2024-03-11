# RO_pag97_exercici20.py
from math import *

llargada= float(input("Ingresa la llargada del bloc rectangular: "))
altura=float(input("Ingrese l'altura del bloc rectangular: "))
ample=float(input("Ingresa l'ample del bloc rectangular: "))


area_cara_longitud = llargada * altura
area_cara_ancho = ample * altura

if area_cara_longitud > area_cara_ancho:
    print (f"El área de la cara de mayor dimensión es l'àrea de la cara de la longitud {area_cara_longitud}cm")
else:
    print (f"El área de la cara de mayor dimensión es l'àrea de la cara de l'ample {area_cara_ancho}cm")