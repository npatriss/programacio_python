#RO_pag96_exercici10.py
from math import *

costat1=float(input("Ingresa el primer costat del triangle: "))
costat2=float(input("Ingresa el segon costat del triangle: "))
costat3=float(input("Ingresa el tercer costat del triangle: "))

if costat1 == costat2 == costat3 :
    print ("El triangle és de tipus Equilàter")
    
elif costat1 == costat2 or costat2 == costat3 or costat1 == costat3 :
    print ("El triangle és de tipus Isòscel·les")
    
else :
    print ("El triangle és de tipus Escalè.")