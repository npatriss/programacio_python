#RO_pag96_exercici14.py
from math import *

#Dades
llarg_bloc_rectangular= int(input("Ingresa la llargada del bloc rectangular: "))
ample_bloc_rectangular= int(input("Ingresa l'amplada del bloc rectangular: "))
altura_bloc_rectangular= int(input("Ingresa l'altura del bloc rectangular: "))
diametre_forat= float(input("Ingresa el diàmetre del forat: "))

#Calculem diagonals
Diagonal1 =sqrt(llarg_bloc_rectangular**2 + ample_bloc_rectangular**2)
Diagonal2 =sqrt(llarg_bloc_rectangular**2 + altura_bloc_rectangular**2)
Diagonal3 =sqrt(ample_bloc_rectangular**2 + altura_bloc_rectangular**2)

# Comprovem si alguna diagonal és menor al diàmetre del forat
if Diagonal1 < diametre_forat or Diagonal2 < diametre_forat or Diagonal3 < diametre_forat:
    print("Si que pasa pel forat")
else:
    print("No pasa pel forat")
