# RO_pag103_aleatoris.py
from random import *

c=0
x=0
while x!=3:
    x=randint(1, 6)
    c=c+1
print('Cantitat de llançaments fins que ha sortit el 3: ', c)