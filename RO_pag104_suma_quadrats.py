#RO_pag104_suma_quadrats.py
from random import *

n=int(input('Ingresa el valor final: '))
s=0
i=1
while i<=n:
    c=i**2
    s=s+c
    i=i+1
print('La suma és: ', s)