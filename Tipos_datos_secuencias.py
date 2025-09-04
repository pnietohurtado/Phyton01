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

