#RO_Pag97_exercici19.py
from math import *

jutge1 =int(input("Pel primer jutge ingresa un 1 si el jutge està a favor o 0 si està en contra: "))
jutge2 =int(input("Pel primer jutge ingresa un 2 si el jutge està a favor o 0 si està en contra: "))
jutge3 =int(input("Pel primer jutge ingresa un 3 si el jutge està a favor o 0 si està en contra: "))

if jutge1 == 0 and jutge2 == 1 and jutge3 == 1 :
    print ("CONTINUA")
elif jutge1 == 1 and jutge2 == 0 and jutge3 == 1 :
    print ("CONTINUA")
elif jutge1 == 1 and jutge2 == 1 and jutge3 == 0 :
    print ("CONTINUA")
elif jutge1 == 1 and jutge2 == 1 and jutge3 == 1 :
    print ("CONTINUA")
elif jutge1 == 1 and jutge2 == 0 and jutge3 == 0 or jutge1 ==  0and jutge2 == 1 and jutge3 == 0 or jutge1 == 0 and jutge2 == 0 and jutge3 == 1 :
    print ("ELIMINADO")
