#RO_pag98_exercici22.py
from math import *

x=float(input("Ingresa el número x: "))
a=float(input("Ingresa el número a: "))
b=float(input("Ingresa el número b: "))

if a < b and x != a and x != b:
    if x < a:
        print(f"El número {x} está antes de {a}.")
    elif a < x < b:
        print(f"El número {x} está entre {a} y {b}.")
    else:
        print(f"El número {x} está después de {b}.")
else:
    print("Asegúrate de que a < b y x ≠ a, x ≠ b.")
