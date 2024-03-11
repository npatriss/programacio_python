# RO_pag150_exercici37_numeroaureo.py
from math import *

n = int(input("n = "))
print("Parelles de numeros (a, b) entre 1 i n")
print("=======================================")
parelles_num_aureos = 0
for a in range(1, n):
    for b in range(1,n):
        if a < b:
            b = a
        elif a > b:
            a = a
        elif (a + b) / b == a / b:
            parelles_num_aureo += 1
            print(a,b)