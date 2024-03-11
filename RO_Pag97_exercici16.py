# RO_pag97_exercici16.py
from math import *

genere = int(input("Si aquesta persona es de gènere femení introdueix un 1, si es de generè masculí introdueix un 2: "))
edat =int(input("Introdueix l'edat de la persona: "))

if genere == 1:
    numero_de_pulsacions = (220-edat)/10
    print ("El número de pulsacions per cada 10 segons d'exercici d'aquesta persona de gènere femení son: ", numero_de_pulsacions)

elif genere == 2:
    numero_de_pulsacions2 = (210-edat)/10
    print ("El número de pulsacions per cada 10 segons d'exercici d'aquesta persona de gènere masculí son: ", numero_de_pulsacions2)