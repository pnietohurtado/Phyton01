import sqlite3 as sql 
import pandas as pd
import matplotlib.pyplot as plt 

conn = sql.connect("mi_base.db")
cursor = conn.cursor() 

df = pd.read_sql_query("SELECT * FROM empleados2", conn)
print(df)

plt.hist(df["edad"], bins = 10)
plt.title("Distribución de las edades")
plt.xlabel("Edad") 
plt.ylabel("Frecuencia")
plt.show() 