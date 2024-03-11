# RO_pag96_exercici8.py
from math import *

#RO_Pag96_Ex8

print("Alumne 1:")
print(" ")

nota1 = float(input("1ra nota de l'alumne 1 = "))
nota2 = float(input("2na nota de l'alumne 1 = "))
nota3 = float(input("3ra nota de l'alumne 1 = "))

if nota1 == nota2 and nota2 == nota3: 
    notafinal1 = nota1 + nota2 
elif nota1 == nota2 and nota1 > nota3: 
    notafinal1 = nota1 + nota2  
elif nota2 == nota3 and nota2 > nota1: 
    notafinal1 = nota2 + nota3
elif nota1 == nota3 and nota3 > nota2: 
    notafinal1 = nota1 + nota3  
elif nota1 > nota2 and nota2 > nota3: 
    notafinal1 = nota1 + nota2
elif nota2 > nota3 and nota3 > nota1: 
    notafinal1 = nota2 + nota3
elif nota2 > nota1 and nota1 > nota3: 
    notafinal1 = nota1 + nota2    
elif nota1 == nota2 and nota3 > nota1:
    notafinal1 = nota1 + nota3
elif nota3 > nota2 and nota2 > nota1:
    notafinal1 = nota3 + nota2   
elif nota2 == nota3 and nota1 > nota2:
    notafinal1 = nota1 + nota2   
elif nota1 == nota3 and nota2 > nota1:
    notafinal1 = nota1 + nota2
    
print("La nota final de l'alumne 1 és d'un",notafinal1)
    
print(" ")
print("Alumne 2:")
print(" ")

nota4 = float(input("1ra nota de l'alumne 2 = "))
nota5 = float(input("2na nota de l'alumne 2 = "))
nota6 = float(input("3ra nota de l'alumne 2 = "))

if nota4 == nota5 and nota5 == nota6: 
    notafinal2 = nota4 + nota5 
elif nota4 == nota5 and nota4 > nota6: 
    notafinal2 = nota4 + nota5
elif nota5 == nota6 and nota5 > nota4: 
    notafinal2 = nota5 + nota6
elif nota4 == nota6 and nota6 > nota5: 
    notafinal2 = nota4 + nota6
elif nota4 > nota5 and nota5 > nota6: 
    notafinal2 = nota1 + nota2
elif nota5 > nota6 and nota6 > nota4: 
    notafinal2 = nota5 + nota6
elif nota5 > nota4 and nota4 > nota6: 
    notafinal2 = nota4 + nota5   
elif nota4 == nota5 and nota6 > nota4:
    notafinal2 = nota4 + nota6
elif nota6 > nota5 and nota5 > nota4:
    notafinal2 = nota6 + nota5  
elif nota5 == nota6 and nota4 > nota5:
    notafinal2 = nota4 + nota5  
elif nota4 == nota6 and nota5 > nota4:
    notafinal2 = nota4 + nota5
    
print("La nota final de l'alumne 2 és d'un",notafinal2)
    
print(" ")

if notafinal1 > notafinal2:
    print("L'alumne 1 ha tret millor nota que l'alumne 2")

elif notafinal2 > notafinal1:
    print("L'alumne 2 ha tret millor nota que l'alumne 1")
    
elif notafinal1 == notafinal2:
    print("Els dos han tret la mateixa nota")