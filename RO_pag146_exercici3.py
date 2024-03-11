# RO_pag146_exercici3.py
from math import *

x =float(input("Ingresa el valor de x: "))

suma = 0
terme_actual = 12
cantitat_termes = 0

while suma <= x:
    suma += terme_actual
    cantitat_termes += 1
    terme_actual += 10

print(f"La cantitat de termes necessaris es: {cantitat_termes}")
