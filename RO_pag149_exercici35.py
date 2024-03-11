#RO_pag149_exercici35.py

a = int(input("Ingresa un valor (a) entre 1 i 1000"))
b = int(input("Ingresa un valor (b) entre 1 i 1000"))

for a in range (1,1000):
    for b in range (b, b+1):
        x = 1000 - a
        y = 1000 - b
        suma = x + y
        resta = 1000 - suma
        producte1 = resta * 1000
        producte2 = x * y
        resultat = producte1 + producte2