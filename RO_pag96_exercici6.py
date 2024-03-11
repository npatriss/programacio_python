# RO_pag96_exercici6.py
from math import *

cantitat_Kw =float(input("Ingresa la cantitat de Kw: "))
Preu_Kw =float(input("Ingresa el preu del Kw: "))

preu_sense_increment = cantitat_Kw * Preu_Kw
if cantitat_Kw > 700 :
    preu_amb_increment = preu_sense_increment * 1.05
    print ("El valor total a pagar és = ", preu_amb_increment)
else :
    print("El preu total a pagar és = ", preu_sense_increment)
    