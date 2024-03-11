# RO_pag97_exercici21.py
from math import *

a11 =float(input(" Primer valor matriu = "))
a12 =float(input("Segon valor matriu = "))
a21 =float(input("Tercer valor matriu = "))

a22 = (a21 * a12) / a11
det_matriu = (a11 * a22) -(a21 * a12)

print(f"{a22} és el nombre que falta de la matriu, {det_matriu} si és 0 vol dir que està be")