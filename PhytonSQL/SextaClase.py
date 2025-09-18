import _sqlite3 as sql 
import pandas as pd 

conn = sql.connect("empresa.db")
cursor = conn.cursor() 

cursor.execute(
    """INSERT INTO clientes(nombre, edad) VALUES ("Pablo", 22), ("Pepe", 19), ("Juan", 44)"""
)
conn.commit() 

cursor.execute(
    """UPDATE clientes SET edad = 12 WHERE nombre LIKE ?"""
, ("Pepe",))
conn.commit() 

df = pd.read_sql_query("SELECT * FROM clientes WHERE edad > 12", conn)
print(df)