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
conexion.commit() 

cursor.execute("""
    INSERT INTO empleados(nombre, edad) VALUES ("Pepe", 12)
""")
conexion.commit() 

cursor.execute(
    """DELETE FROM empleados WHERE nombre = ?""", ("Pablo",)
)
conexion.commit() 

cursor.execute("""
    SELECT * FROM empleados
""")
conexion.commit() # Efectuar los cambios 

resultados = cursor.fetchall() # Para poder sacar todos los resultados de la sentencia 
# resultados = cursor.fetchone() # Para que devuelva únicamente uno 

#for fila in resultados: 
print(resultados)


# Separación 
print("########################")


nombre = "Pepe" 
cursor.execute("""
    SELECT * FROM empleados WHERE nombre LIKE ?
""", (nombre,))
conexion.commit() 

datos = cursor.fetchall() 
print(datos)