# RO_pag182_exercici21.py
from math import *

def triangular_for(n):
    fx = fx + 1
    for i in range(1,n+1):
        fx += i
        print (f"n = {i} i f(x) = {fx}")
    return fx

def suma_f(n):
    fx = 0
    suma = 0
    for i in range(1,n+1):
        fx = fx + i
        suma += fx
    return suma_f

sortida = False
while not sortida:
    print("Menu:")
    print(" 1 Nombres triangulars")
    print(" 2 Suma nombres triangulars")
    r = int(input("Tria una de les dues opcions: "))
    if r == 1:
        n = int(input("n : "))
        triangular_for(n)
    elif r == 2:
        n  = int(Input("n = "))
        s = suma_f(n)
        print (s)