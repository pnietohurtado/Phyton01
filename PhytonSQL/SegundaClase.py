import sqlite3 as sql

conexion = sql.connect("mi_base.db")
# Si la base de datos existe, la abre 
# En caso de que no exista, crea una desde cero y la abre 

cursor = conexion.cursor()
# Encargado de permitir a python llevar a cabo esas sentencias a las BBDD 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
""")

conexion.commit() # Efectuar los cambios 