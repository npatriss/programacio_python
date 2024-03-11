# RO_pag181_exercici13.py
from math import *

def polar(x, y):
    r = sqrt(x**2 + y**2)
    t = atan2(y, x)
    return r, t

def cartesiana(r, t):
    x = r * cos(t)
    y = r * sin(t)
    return x, y

def principal():
    while True:
        print("Menú:")
        print("1- Convertir a polars")
        print("2- Convertir a cartesians")
        print("3- Sortir")

        opcio = input("Escull una opció: ")

        if opcio == '1':
            x = float(input("Ingresa la coordenada x: "))
            y = float(input("Ingresa la coordenada y: "))
            r, t = polar(x, y)
            print(f"Coordenades polars: r = {r}, t = {t}")
        elif opcio == '2':
            r = float(input("Ingresa la coordenada r: "))
            t = float(input("Ingresa la coordenada t en radians: "))
            x, y = cartesiana(r, t)
            print(f"Coordenadas cartesianas: x = {x}, y = {y}")
        elif opcio == '3':
            print("Adeu!!")
            break
        else:
            print("Opció no vàlida. Siusplau, escull de nou un numero entre el 1 i el 3.")
        

if __name__ == "__main__":
    principal()
    