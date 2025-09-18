import sqlite3 as sql 
import pandas as pd 

conn = sql.connect("mi_base.db")
cursor = conn.cursor() 

cursor.execute(
    """CREATE TABLE IF NOT EXISTS empleados2 (
        id INTEGER PRIMARY KEY, 
        nombre TEXT ,
        edad INTEGER, 
        cargo TEXT, 
        salario REAL 
    )"""
)

conn.commit() 
conn.close() 

conn = sql.connect("mi_base.db")
cursor = conn.cursor() 

cursor.execute(
    """INSERT INTO empleados2 VALUES(4,"Pablo", 23, "Analista", 2333)"""
) 
conn.commit() 

cursor.execute(
    """SELECT * FROM empleados2"""
)
todos = cursor.fetchall() 
print("Todos los registros: ", todos)

cursor.execute(
    """SELECT * FROM empleados2 WHERE ID = 1"""
)
todos = cursor.fetchone() 
print("Solo muestra uno: ", todos)

df = pd.DataFrame(todos, columns=["id", "nombre", "edad", "cargo", "salario"])
print(df)