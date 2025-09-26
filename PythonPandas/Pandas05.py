import pandas as pd 
import matplotlib.pyplot as mp
import seaborn as sb 

df = pd.read_csv("copia_titanic.csv", index_col = 0)
print(df.head())


print(df.iloc[0:4, 0:2]) # Lo primero son las filas y luego tenemos las columnas 
print(df.loc[df["Edad"] > 35, ["Nombre"]])
print(df.iloc[0:11, 2:7])

print("-------- SubFunciones útiles de pandas ------------")
print(df["Edad"].mean())
#print(df[df["Sexo"] == "Femenino"].max())



print("-------- Cargando datos con gráficos------------")
ap = pd.read_csv("air_quality_no2.csv", index_col=0, parse_dates=True)
print(ap.head())
print(ap.describe())
print(ap.info())

print(ap.resample("d").mean().head()) 
print(ap.resample("m").mean().head()) 

print(ap.plot())
print(ap["station_1"].plot())
mp.show()

mp.scatter(ap["station_3"], ap["station_2"]) 
mp.show()


ap.plot.box() 
mp.show() 

