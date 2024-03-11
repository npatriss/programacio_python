#RO_pag180_exercici4.py
import random

def sumad(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n//10
    return suma

def trobar_suma_mes_gran():
    max_suma= 0
    numero_max_suma = 0
    for _ in range(10):
        numero = random.randint(1, 100)
        suma_digits = sumad(numero)
        if suma_digits > max_suma:
            max_suma = suma_digits
            numero_max_suma = numero
    return numero_max_suma

numero_max_suma = trobar_suma_mes_gran()
print (f"El numero amb la suma més gran de les seves xifres és: {numero_max_suma}")
      
    