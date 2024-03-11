# RO_pag147_exercici14.py
from math import *

diners = float(input("Ingresa una quantitat de diners: "))
articles = {454, 785, 1000, 2347}
articles_comprar = 0
a = 0
    
for n in articles:
    if n <= diners :
        a += 1
        articles_comprar = diners / n // 1
        print (f"Podem comprar {articles_comprar} articles.")
        
    else:
        print ("No ho pots comprar.")

print (f"En total pots comprar {a} articles")     