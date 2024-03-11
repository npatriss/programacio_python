# RO_pag98_exercici23.py
from math import *

calificacio1 = float(input("Ingresa la primera calificació: "))
calificacio2 = float(input("Ingresa la segona calificació: "))
calificacio3 = float(input("Ingresa la tercera calificació: "))

calificacions_ordenades = sorted([calificacio1, calificacio2, calificacio3])

print("Calificacions ordenades en forma ascendent:", calificacions_ordenades)