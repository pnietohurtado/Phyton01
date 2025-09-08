"""
cadena = "información"
for caracter in cadena: 
    print(caracter)  # Se encarga de devolver un valor de la cadena uno a uno 
"""

"""
hora = "12:23:21"
hora.split(":")
print(hora)
"""

"""
cadena = input("Dime una cadena de caracteres: ")
cadena2 = input("Dime una cadena de caracteres: ")
if cadena.startswith(cadena2): 
    print("La cadena comienza por la subcadena!")
else: 
    print("La cadena NO comienza por la subcadena!")
"""

"""
cadena = input("Dime una cadena de caracteres: ")
while True: 
    car = input("Dime un carácter: ")
    if len(car) == 1: break 
print("En la cadena aparece el caracter ", cadena.count(car))
"""

"""
cont = 0
posicion = 0
cadena = input("Dime una cadena de caracteres: ")
cadena = cadena.strip() 
posicion = cadena.find(" ", posicion)
while posicion != -1: 
    cont += 1
    while cadena[posicion +1 ] == " ": 
        posicion = posicion +1 
    posicion = cadena.find(" ", posicion + 1 )
print ("La frase tiene ", cont + 1, " palabras")
"""

"""
lista = [1,2,3,4,5,6]
lista2 = ["a","b","c","d","e","f"]
for num, letra in zip(lista,lista2): 
    print(num, " " , letra)
print("Lista numérica invertida -> ", lista[::-1])
"""

"""
lista = [1,2,3,4,5,6]
lista[0] = 100
for i in lista: 
    print(lista)
lista.append(17)
print("Nueva lista ", lista )
"""

"""
lista = [1,2,3,4,5]
lista2 = [1,55,6,33,22]
lista = lista2
lista.append(13)
print(lista , " " , lista2) # Son en esencia la misma lista ya que ahora es como si compartieran mismo punto de referencia o cursor


lista = [1,2,3,4,5]
lista2 = [1,55,6,33,22]
lista = lista2[:]
lista.append(13)
print(lista , " " , lista2) # De esta forma ya no comparten el mismo cursor de los datos
"""

"""
lista = [1,2,3,4,5,6]
lista.pop(1)
lista.remove(3) #Elimina todos los "3"
lista.reverse()
lista.sort(reverse=True)
print(lista)
"""

"""
import random 
lista = []
for indice in range(1,11): 
    lista.append(random.randint(1,10))
for indice in lista: 
    print(lista[indice])
"""



"""
notas = []
suma = 0
for indice in range(1,6): 
    nota = int(input("Dime la primera nota: "))
    if nota > 0 and nota < 10: 
        notas.append(nota)
        suma += nota 
    else : 
        print("Esa nota no es válida!")
media = suma / 5
"""


"""
nombres = []
edades = []
while True: 
    nombre = input("Dime el nombre de un alumno: ")
    if nombre != "*": 
        nombres.append(nombre)
        edades.append(int(input("Dime la edad: ")))
    if nombre == "*": break; 
edad_max = max(edades)
print ("Alumnos mayores de edad")
for nombre, edad in zip(nombres, edades ): 
    if edad >= 18: 
        print(nombre)
"""

