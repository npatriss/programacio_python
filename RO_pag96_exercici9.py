#RO_pag96_exercici9.py
from math import *

calificacio1 = float(input("La primera calificació del estudiant és: "))
calificacio2 = float(input("La segona calificació del estudiant és: "))
calificacio3 = float(input("La tercera calificació del estudiant és: "))
resultat1 = 0
resultat2 = 0

#Calificació més alta
if calificacio1 == calificacio2 and calificacio2 == calificacio3 :
    resultat1 = calificacio1
    print ("Les tres notes del estudiant son la mateixes, pertant qualsevol d'elles és el resultat més alt=",calificacio1)
    
elif calificacio1 > calificacio2 and calificacio1 > calificacio3 :
    resultat1 = calificacio1
    print ("Les nota més alta d'aquest estudiant és la calificació del primer exàmen=",calificacio1)
    
elif calificacio2 > calificacio1 and calificacio2 > calificacio3 :
    resultat1 = calificacio2
    print ("Les nota més alta d'aquest estudiant és la calificació del segon exàmen=",calificacio2)
    
elif calificacio3 > calificacio1 and calificacio3 > calificacio2 :
    resultat1 = calificacio3
    print ("Les nota més alta d'aquest estudiant és la calificació del tercer exàmen=",calificacio3)
    
#Calificació més baixa
if calificacio1 == calificacio2 and calificacio2 == calificacio3 :
    resultat1 = calificacio1
    print ("Les tres notes del estudiant son la mateixes, pertant qualsevol d'elles és el resultat més baix=",calificacio1)

elif calificacio1 < calificacio2 and calificacio1 < calificacio3 :
    resultat1 = calificacio1
    print ("Les nota més baixa d'aquest estudiant és la calificació del primer exàmen=",calificacio1)
    
elif calificacio2 < calificacio1 and calificacio2 < calificacio3 :
    resultat1 = calificacio1
    print ("Les nota més baixa d'aquest estudiant és la calificació del primer exàmen=",calificacio1)
    
elif calificacio3 < calificacio1 and calificacio3 < calificacio2 :
    resultat1 = calificacio3
    print ("Les nota més baixa d'aquest estudiant és la calificació del tercer exàmen=",calificacio3)