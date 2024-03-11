#RO_pag97_exercici15.py
from math import *

numero =int(input("Ingresa un número de tres xifres: "))

[numero1,numero2] = divmod(numero, 100)
[numero2,numero3] = divmod(numero2, 10)
multiplicacio = numero1 * numero2
resultat = multiplicacio % 10

if resultat == numero3 :
    print ("Codi vàlid")
    
else :
    print ("Codi invàlid")