# RO_pag95_exercici2.py
from math import *

radi=int(input("radi = "))
altura=int(input("altura = "))

if altura > radi :
    volum = 3.1416 * pow(radi, 2) * altura
    print ("Volum del cilindre = ", volum)

else :
    print ("error")