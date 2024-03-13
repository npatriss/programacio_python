#RO_pag231_exercici2.py

def caixes(n):
    pesos = []
    print("Introdueix els pesos de les", n, "caixes:")
    for i in range (n):
        pes = float(input("Pes de la caixa: "))
        pesos.append(pes)
        
    pes_promig = sum(pesos) / n
    
    caixes_major_pes_promig = 0
    for pes in pesos:
        if pes > pes_promig:
            caixes_major_pes_promig += 1
            
    print ("El nombre de caixes amb major pes al peso promig son: ", caixes_major_pes_promig)
    
n = int(input("Introdueix el nombre de caixes: "))
caixes(n)
        
    