#RO_pag180_exercici3.py

def perfecto(n):
    suma_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisors += i
    return suma_divisors == n

def trobar_numeros_perfectos():
    numeros_perfectos = []
    for num in range(1, 1001):
        if perfecto(num):
            numeros_perfectos.append(num)
    return numeros_perfectos

numeros_perfectos = trobar_numeros_perfectos()
print(f"Números perfectos entre 1 i 1000: {numeros_perfectos}")
    
    