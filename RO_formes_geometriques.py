#RO_formes_geomètriques
from math import *

def quadrat(a):
    area = a**2
    perimetre = 4 * a
    print (area)
    print (p)
    
def triangle(a, b, c, h):
    area = a*h/2
    perimetre = a+b+c
    print (area)
    print (perimetre)
    
def rectangle(a, b):
    area = b * a
    perimetre = 2 * (b+a)
    print (area)
    print (perimetre)
    
def paralelogram(a, b, h):
    area = b * h
    perimetre = 2 * (b+a)
    print (area)
    print (perimetre)
    
def rombe(D, d, a):
    area = D*d/2
    perimetre = 4 * a
    print (area)
    print (perimetre)
    
def cometa(D, d, b, a):
    area = D*d/2
    perimetre = 2 * (b+a)
    print (area)
    print (perimetre)
    
def trapeci(B, b, h, c, a):
    area = (B+b)*h/2
    perimetre = B+b+a+c
    print (area)
    print (perimetre)
    
def cercle(r):
    area = 3,1416 * r**2
    perimetre = 2 * 3,1416 * r
    print (area)
    print (perimetre)
    
def poligon_regular(a, b, n, P):
    area = P*a/2
    perimetre = n * b
    print (area)
    print (perimetre)
    
def corona_circular(R, r):
    area = 3,1416 * (R**2 - r**2)
    print (area)
    
def sector_circular(R, n):
    area = 3,1416 * R**2 * n/ 360
    print (area)


Salida=False
while not Salida:
    print ("")
    print ("A continuació tens la llista de les següents formes geomètriques. ")
    print ("Escull la figura que vulguis per a calcular la seva àrea, volum o perímetre: ")
    print ("1.Quadrat ")
    print ("2.Triangle ")
    print ("3.Rectangle ")
    print ("4.Paralelogram ")
    print ("5.Rombe ")
    print ("6.Cometa ")
    print ("7.Trapeci ")
    print ("8.Cercle ")
    print ("9.Poligon regular ")
    print ("10.Corona circular ")
    print ("11.Sector circular ")
    print ("12.Sortir ") 
    opcio = int(input("ESCULLEIX UNA OPCIÓ: "))
    
    if opcio == 1: #Quadrat
        a = float(input("Costat a: "))
        quadrat(a)
    elif opcio == 2: #triangle
        a = float(input("Costat a: "))
        b = float(input("Costat b: "))
        c = float(input("Costat c: "))
        h = float(input("Altura h: "))
        triangle(a, b, c, h)
    elif opcio == 3: #Rectangle
        a = float(input("Costat a: "))
        b = float(input("Costat b: "))
        rectangle(a, b)
    elif opcio == 4: #Paralelogram
        a = float(input("Costat a: "))
        b = float(input("Costat b: "))
        h = float(input("Altura h: "))
        paralelogram(a, b, h) 
    elif opcio == 5: #Rombe
        D = float(input("Diagonal gran D: "))
        d = float(input("Diagonal petita d: "))
        a = float(input("Costat a: "))
        rombe(D, d, a)
    elif opcio == 6: #Cometa
        D = float(input("Diagonal gran D: "))
        d = float(input("Diagonal petita d: "))
        b = float(input("Costat gran b: "))
        a = float(input("Costat petit a: "))
        cometa(D, d, b, a) 
    elif opcio == 7: #Trapeci
        B = float(input("Costat B: "))
        b = float(input("Costat b: "))
        h = float(input("Altura h: "))
        c = float(input("Costat c: "))
        a = float(input("Costat a: "))
        trapeci(B, b, h, c, a) 
    elif opcio == 8: #Cercle
        r = float(input("Radi r: "))
        cercle(r)
    elif opcio == 9: #Poligon regular
        a = float(input("Apotema a: "))
        b = float(input("Costat b: "))
        n = float(input("Nombre de costats n: "))
        P = float(input("Perímetre P: "))
        poligon_regular(a, b, n, P)
    elif opcio == 10: #Corona circular
        R = float(input("Radi gran R: "))
        r =float(input("Radi petit r: "))
    elif opcio == 11: #Sector circular
        R = float(input("Radi R: "))
        n = float(input("Angle d'obertura del sector n: "))
    elif opcio == 12: #Sortir
        Salida = True
        print("Nosssss  vemossss")
    