#RO_pag180_exercici2.py
from math import *
from random import randint

def primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def trobar_numeros_primos():
    trobat = False
    while not trobat:
        numero1 = randint(1, 100)
        numero2 = randint(1, 100)
        suma = numero1 + numero2
        if primo(suma):
            trobat = True
    return numero1, numero2

if __name__ == "__main__":
    numero1, numero2 = trobar_numeros_primos()
    suma = numero1 + numero2
    print(f"Els numeros enters són: {numero1} y {numero2}")
    print(f"La suma dels números és: {suma} i és un numero primo.")