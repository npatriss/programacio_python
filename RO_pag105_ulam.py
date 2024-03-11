#RO_pag105_ulam.py
from random import *

x=int(input('Ingresa la dada inicial: '))
while x>1:
    if x%2 == 0:
        x=x//2
    else:
        x=3*x+1
    print(x)
     