# RO_pag83_exercici3.py
from math import *

a =int(input("Primer nombre de tres xifres = "))
b =int(input("Segon nombre de tres xifres = "))

resultat = (a % 100 // 10) + (b % 100 // 10)
print("La suma de les xifres centrals és:", resultat)