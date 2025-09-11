"""

dict = {'one': 1, 'two' : 2, 'three' : 3}
dict.clear()
print(dict)
print("Lo volvemos a crear!")
dict = {'one': 1, 'two' : 2, 'three' : 3}
dict2 = {'four': 4, 'five':5}
dict.update(dict2)
print("El diccionario una vez añadidos los del segundo: ", dict)
print(dict["one"]) # No muy recomendable usar 
print(dict.get("one")) # Esta forma de búsqueda es mucho mejor (No devuelve una excepción si no existe)

for clave in dict.keys(): 
    print(clave)
    print(dict.get(clave))

for clave,valor in dict.items(): 
    print("La clave es ", clave, " y el valor es ", valor )
"""

"""
dict = {}
cadena = input("Dime una cadena: ")
for caracter in cadena: 
    if caracter in dict: 
        dict[caracter]+=1
    else: 
        dict[caracter]=1
for campo, valor in dict.items(): 
    print(campo, " -> ", valor)
"""



precios = {"manzana" : 2, "naranja" : 1.2, "platano": 4}
while True: 
    fruta = input("Dime la fruta que has vendido: ")
    if fruta.lower() not in precios: 
        print("Fruta no existe!")
    else: 
        cantidad = int(input("Dime la cantidad de frutas que has vendido: "))
        print("El precio es de %f" % (cantidad * precios[fruta.lower()]))
    opcion = input("¿quieres vender otra fruta[n/s]")