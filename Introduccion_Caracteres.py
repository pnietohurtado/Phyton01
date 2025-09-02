# Clase del 27/08/2025
"""
cadena = "Pablo"
print("La cadena del string se convierte de la siguiente forma \n" + cadena[0] + "\n" + cadena[2])
#Esto básicamente significa que las cadenas de caracteres las tratas como lo que son 
#caracteres dentro de un texto un no como un tipo de variable aislado como en Java 

if "informatica" > "informacion": 
    print("Informática pesa más que información!")

if "hola" == "hola": 
    print("hola es igual a hola")

cadena2 = "Nieto"
cadena3 = cadena + " " + cadena2.upper()  
print(cadena3)
"""

"""
import math 
cateto1 = float(input("Dime el cateto 1: "))
cateto2 = float(input("Dime el cateto 2: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print("La hipotenusa es %.2f" % hipotenusa) # Nos permite poner únicamente dos decimales 
"""

"""
parcial1 = float(input("Resultado primer parcial: "))
parcial2 = float(input("Resultado segundo parcial: "))
parcial3 = float(input("Resultado tercero parcial: "))
examen_final = float(input("Nota examen final: "))
trabajo_final = float(input("Nota trabajo final: "))
media_parciales  = float(((parcial1 + parcial2 + parcial3) / 3)  * 0.55 + (examen_final * 0.33) + (trabajo_final * 0.15))
print("La media de la nota del alumno es %.2f" % media_parciales)
"""

"""
a = int(input("Dime un numero: "))
b = int(input("Dime un numero: "))
aux = a 
a = b 
b = aux 
print("El numero a es ahora %d y el b es ahora %d"%(a,b))
"""

"""
hora = int(input("Dime la hora: "))
minutos = int(input("Dime la minutos: "))
segundos = int(input("Dime la segundos: "))
segundos_b = int(input("Dime la llegada en segundos: "))
if segundos + segundos_b > 60: 
    resto = (segundos + segundos_b) -  60; 
    minutos += 1
    print("La hora de llegada es %d:%d:%d"%(hora, minutos, resto))
else: 
    segundos += segundos_b
    print("La hora de llegada es %d:%d:%d"%(hora, minutos, segundos))
"""

"""
nombre = (input("Dime el nombre: "))
apellido = (input("Dime el apellido: "))
print("Las iniciales de la persona son %s.%s"%(nombre[0].upper(),apellido[0].upper()))
"""

"""
edad = int(input("Dime tu edad: "))
if edad > 18: 
    print("Eres mayor de edad!")
elif edad > 70: 
    print("Eres demasiado mayor bro") 
else : 
    print("Eres menor de edad!")
"""

"""
numero = int(input("Dime un numero: "))
if numero > 0: 
    print("El número es positivo!")
elif numero < 0: 
    print("El número es negativo!")
elif numero == 0:
    print("El número es igual a 0!")
"""


"""
usuario = input("Dime el usuario: ")
contra = input("Dime la contraseña: ")
if usuario == "pepe" and contra == "123": 
    print("Inicio de sesión correcto!")
else: 
    print("Inicio de sesión incorrecto!")
"""

"""
numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: "))
numero3 = int(input("Dime otro numero: "))
if numero1 > numero2: 
    if numero1 < numero3: 
        print(numero1 + " " + numero3 + " " + numero2)
    else: 
        print(numero3 + " " + numero1 + " " + numero2)
elif(numero)
"""

"""
dia = int(input("Dime el día: "))
mes = int(input("Dime un mes: "))
year = int(input("Dime el año: "))
if dia >  0 and dia < 31 :
    if mes > 0 and mes < 12: 
        if year > 0 and year < 2025: 
            print("La fecha es correcta!")
else: 
    print("La fecha es incorrecta!")
"""

"""
nombre = input("Dime tu nombre: ")
while nombre != "Pablo": 
    print("El nombre es incorrecto, vuelve a intentarlo!")
    nombre = input("Dime tu nombre: ")
    if nombre == "Pablo": 
        print("Nombre correcto!")
        break; 
"""


"""
cont = 0 
while cont < 10: 
    cont+=1
    if cont % 2 == 1: 
        continue
    print(cont)
"""

"""
for var in range(0,10,+1): 
    print(var, " ", end="") # Con ',end=""', lo que hacemos es que todo se imprima en una única línea 
"""
"""
cont = 0
for var in range (1,6): # 5 veces va a ejecutarse 
    num = int(input("Dime un número: "))
    if num % 2 == 0: 
        cont += 1
print("Has introducido un total de ",cont, " números pares")

"""
"""
indicador = False 
for var in range(1,6): 
    num = int(input("Dime un numero: "))
    if num % 2 == 0: 
        indicador = True
        break
print("El indicador se ha vuelto true!")
"""
