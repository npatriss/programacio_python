# RO_pag71_exercici2.py

from math import *

diagonal = float(input("diagonal en cm="))
alfa = float(input("angle ="))

alfa_rad = alfa * (pi / 180) # pas a rad
base = diagonal * cos(alfa_rad)
altura = diagonal * sin(alfa_rad)

area = (altura * base ) / 2
print ("Area del triangle = " , area)

