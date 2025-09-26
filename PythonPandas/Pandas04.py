import pandas as pd 
import xlrd 
pd.__version__ 

df = pd.read_csv("copia_titanic.csv", index_col = 0)
print(df.head())
print(df["Nombre"])

print("-------")
print(df.head()) 
hombres = df[df["Sexo"] == "Masculino"]
print(hombres)

print("----------")
print(df.head())
id = df[df["Id_Pasajero"] > 10]
print(id)


print("---------")
print(df.head())
clase = df[df["Clase"].isin([1,2])]
print(clase.head())
print(clase.count() )


print("---------")
print(df.head()) 
edad_nonula = df[df["Edad"].notna()]
edad_nula = df[df["Edad"].isna()]
print(edad_nonula.head())