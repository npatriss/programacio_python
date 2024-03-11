# RO_pag148_exercici24.py
from random import *

dolars = 0
intents_max = 10
n = 1
while n <= intents_max :
    numero = randint (1, 6)
    if numero == 6:
        dolars = dolars + 5
        
    elif numero == 1:
        dolars = dolars + 1
        
    elif numero == 2 or numero == 3 or numero == 4 or numero == 5:
        dolars = dolars - 2
        
    print ("tirada",n,"=",numero, end=" ")
    print ("  dolars = ", dolars)
    n = n + 1

print (f"El nombre final de dolars es = {dolars}")
