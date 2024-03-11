# RO_pag148_exercici29.py

dia = int(input("Inngresa el dia de naixament: "))
mes = int(input("Inngresa el mes de naixament: "))
anyy = int(input("Inngresa l'any de naixament: "))

suma = dia + mes + anyy
unitat = suma % 10
print ("unitat = ", unitat)
desena = (suma // 10) % 10
print ("Desena = ", desena)
centena = (suma // 100) % 100
print ("Centena = ", centena)
miler = suma // 10
print ("miler = ", miler)

suma2 = unitat + desena + centena + miler
unitat2 = suma2 % 10
print ("unitat2 = ", unitat2)
desena2 = (suma2 // 10) % 10
print ("desena2 = ", desena2)
miler2 = suma2 // 10
print ("miler2 = ", miler2)

suma3 = 