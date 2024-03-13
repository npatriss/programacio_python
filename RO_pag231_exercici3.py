#RO_pag231_exercici3.py

def objectes(n):
    pesos = []
    print("Introdueix els pesos dels", n, "objectes de una bodega:")
    for i in range (n):
        pes = float(input("Pes de l'objecte: "))
        pesos.append(pes)
        
    pesos.sort()
    
    rang_pesos = pesos[-1] - pesos[0]
    print ("Rang dels pesos dels objectes: ", rang_pesos)
    
n = int(input("Introdueix el nombre de objectes de la bodega: "))
objectes(n)
        
    