#RO_pag96_exercici13.py
from math import *

#Dades
Juan_hores_treballades=float(input("Ingresa el nombre d'hores treballades per el Juan: "))
Juan_salari_hora=float(input("Ingresa el salari per hora del Juan: "))
Juan_descomptes=float(input("Ingresa els descomptes del Juan: "))

Pedro_hores_treballades=float(input("Ingresa el nombre d'hores treballades per el Pedro: "))
Pedro_salari_hora=float(input("Ingresa el salari per hora del Pedro: "))
Pedro_descomptes=float(input("Ingresa els descomptes del Pedro: "))

Jose_hores_treballades=float(input("Ingresa el nombre d'hores treballades per el José: "))
Jose_salari_hora=float(input("Ingresa el salari per hora del José: "))
Jose_descomptes=float(input("Ingresa els descomptes del José: "))

#Salaris
Salari_setmanal_Juan = Juan_hores_treballades * Juan_salari_hora - Juan_descomptes
Salari_setmanal_Pedro = Pedro_hores_treballades * Pedro_salari_hora - Pedro_descomptes
Salari_setmanal_Jose = Jose_hores_treballades * Jose_salari_hora - Jose_descomptes

#Quin salari és el més elevat dels tres
if Salari_setmanal_Juan == Salari_setmanal_Pedro and Salari_setmanal_Juan == Salari_setmanal_Jose :
    print("Els tres salaris dels tres treballadors són exactament iguals, pertant qualsevol dels tres és el més alt")
    
elif Salari_setmanal_Juan > Salari_setmanal_Pedro and Salari_setmanal_Juan > Salari_setmanal_Jose :
    print("El Juan és qui rebrà el salari més elevat dels tres.")
    
elif Salari_setmanal_Pedro > Salari_setmanal_Juan and Salari_setmanal_Pedro > Salari_setmanal_Jose :
    print("El Pedro és qui rebrà el salari més elevat dels tres.")
    
elif Salari_setmanal_Jose > Salari_setmanal_Pedro and Salari_setmanal_Jose > Salari_setmanal_Juan :
    print("El José és qui rebrà el salari més elevat dels tres.")


