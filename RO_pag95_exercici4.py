#RO_pag95_exercici4.py
from math import *

x =int(input("Ingresa un nombre de dos xifres: "))

xifre_2 = x % 10
xifre_1 = x // 10

suma_xifres = (xifre_2 + xifre_1)

if suma_xifres % 2 == 0:
    missatge = "La suma de las xifres es un nombre parell."
else:
    missatge = "La suma de las xifres es un nombre imparell."

print("missatge: ", missatge)