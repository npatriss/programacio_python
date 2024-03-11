# RO_pag83_exercici2.py
from  math import *

dies=int(input("dies = "))

mesos = (x, y)=divmod (dies, 30)
setmanes = (y,z)=divmod (y, 7)

print (f" {dies} dies equivalen a {x} mesos, {y} setmanes i {z} dies")