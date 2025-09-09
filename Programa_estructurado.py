"""
def factorial(n): 
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado 

num = int(input("Dime un numero: "))
print(factorial(num))
"""

"""
def EsMultiplo(n,n2): 
    resultado = False 
    if n % n2 == 0: 
        resultado = True
    else: 
        resultado = False 
    return resultado 


numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
if EsMultiplo(numero1, numero2): 
    print("Si son múltiplos")
else: 
    print("No son múltiplos")
"""

"""
import random 
def calcular(lista): 
    return (max(lista), min(lista))

numeros = []
for i in range(10): 
    numeros.append(random.randint(1,100))
vmax,vmin = calcular(numeros)
print("El número máximo es: ", vmax)
print("El número mínimo es: ", vmin)
"""


def Calcular_dia_juliano(d,m,y): 
    diaj = 0
    for mes in range(1, m): 
        diaj = diaj + DiasdelMes(m,y)
    diaj = diaj + d
    return diaj 

def LeerFecha(): 
    day = int(input("Día: "))
    mes = int(input("Mes: "))
    año = int(input("Año: "))
    return day,mes,año

d,m,a = LeerFecha()
print("Dia Juliano: ", Calcular_dia_juliano(d,m,a))