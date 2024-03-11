#RO_pag96_exercici12.py
from math import *

cantitat_de_articles= int(input("Inresa el nombre de cantitat d'articles: "))
preu_unitari_original= float(input("Ingresa el preu unitari original: "))

if cantitat_de_articles <= 5:
    descompte = 0
    
elif 5 < cantitat_de_articles < 10:
    descompte = 0.05
    
else :
    descompte = 0.08
    
Preu_total = cantitat_de_articles * preu_unitari_original * (1-descompte)

print(f"El valor total a pagar és: {Preu_total}€")