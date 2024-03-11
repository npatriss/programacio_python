# RO_pag96_exercici7.py
from math import *

temperatura =float(input("Ingresa un valor de temperatura: "))
codi =float(input("Ingresa un número de codi escollit entre 1 i 2: "))

if codi != 1 and 2 :
    print ("Error")

elif codi == 1 :
    temperatura_c = 5/9*(temperatura-32)
    print ("La temperatura c = ", temperatura_c)

else:
    temperatura_f = 32+9*temperatura/5
    print ("La temperatura f = ", temperatura_f)

