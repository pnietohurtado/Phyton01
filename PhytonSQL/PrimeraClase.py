"""
nombre = "Pablo" 
print("String: ", nombre)

edad = 28 
print("Integer: ",edad)

altura = 1.65
print("Float: ",altura)

mayor_edad = True
print("Boolean: ", mayor_edad)

colores = ["rojo","verde","azul"]
print("Lista" , colores )

cliente = {"nombre" : "Luis", "edad" : 35, "activo": True}
print("Diccionario " , cliente)

coordenadas = (40.3333, -83.999)
print("Tupla: ", coordenadas)

frutas = {"manzana", "platano", "manzana", "pera"}
print("Conjunto: ", frutas )

"""

"""
# Importar los datos 
import sys
print(sys.executable)


try: 
    import pandas as pd
    print("Pandas instalado correctamente!")
except ImportError: 
    print("Pandas no se pudo instalar!")

datos = { "nombre" : ["ana", "Luis", "Ana"], 
         "apellido" : ["Nieto", "Juan", "Pepe"]}
df = pd.DataFrame(datos)
print("DataFrame creado manualmente: ", df)


df = pd.read_csv("clientes.csv", sep=";")

print("Columna Nombre: ", df["Nombre"]) #Para poder acceder a los datos de la columna nombre 
print("Primera fila: ", df.iloc[0]) #Para acceder a una fila específica 
"""

"""
import pandas as pd 
data = {
    "Nombre" : ["Pablo", "Luis", "Carlos"],
    "Edad" : [23, 22, 21]
}

df = pd.DataFrame(data)
print(df)

print("======================")

df1 = pd.read_csv("Clientes.csv", sep=";")
print(df1)
"""