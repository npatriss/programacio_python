# RO_pag81_ex9.py

from math import *

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

x = sqrt(pow((c - a),2) + pow((d-b),2))
y = sqrt(pow(a,2)+pow(b,2))
z = sqrt(pow(c,2)+pow(d,2))
t = (x + y + z)/2
print(t)
area_quadrat= ((a * b)  