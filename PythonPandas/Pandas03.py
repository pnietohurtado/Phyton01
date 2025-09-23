import pandas as pd
import xlrd as x 

ruta = "C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\"
# pd.read_excel("titanic.xlsx")

df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";")
print(df.head())

print("=======Archivos .txt ==========")
df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";")
print(df.head()) 

print("=======Archivos .indexados ==========")
#df1 = pd.read_html("https://es.wikipedia.org/wiki/Luisiana")
#print(df1[0]) 

df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";", index_col = 0)
print(df.head())
print("---------")
"""
df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";", nrow = 3)
print(df.head())
"""
df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";", usecols=["Survived", "Nombre", "Sexo"])
print(df.head())
print("------------")
df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";", skiprows=3)
print(df.head())
print("------------")
df = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";",header=None, names= ["Id_Pasajero", "Survived", "Clase", "Nombre"], skiprows=3)
print(df.head())



#Funciones básicas de almacenamiento 
titanic = pd.read_csv("C:\\Users\\pablo\\Desktop\\Py\\PANDAS-main\\PANDAS-main\\titanic.csv", sep=";")
titanic.to_csv("copia_titanic.csv")
titanic.to_csv("copia_titanic.txt")
titanic.to_html("copia_titanic.html")
