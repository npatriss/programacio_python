#RO_pag180_exercici1.py
from math import *

def conteo(n):
    divisors = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisors = divisors + 1
    return divisors

d = 0
c = 0
for i in range (1,101):
    print(i)
    if conteo(i) > d:
        d = conteo(i)
        c = i

print(f"El número que té més divisors és:{c}, i en té {d}")



    
    