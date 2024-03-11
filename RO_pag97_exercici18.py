# RO_pag97_exercici18.py
from math import *

pes =float(input("Ingresa el pes en kg: "))
altura =float(input("Ingresa l'altura en m: "))

imc = pes / pow(altura,2)

if imc < 20:
    print ("Aquesta persona està desnutrida.")
elif imc >=20 and imc <25 :
    print ("Aquesta persona està en estat normal.")
elif imc >=25  and imc < 30 :
    print ("Aquesta persona està en estat de sobrepes.")
elif imc >=30 and imc < 35 :
    print ("Aquesta persona té obesitat de grau 1.")
elif imc >=35 and imc < 40 :
    print ("Aquesta persona té obesitat de grau 2.")
elif imc > 40 :
    print ("Aquesta persona té obesitat de grau 3.")