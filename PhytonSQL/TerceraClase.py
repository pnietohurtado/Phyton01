import sqlite3 as sql 

conexion = sql.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("""
    INSERT INTO empleados(nombre, edad) VALUES ("Pepe", 12)
""")
conexion.commit() 

cursor.execute(
    """DELETE FROM empleados WHERE nombre = ?""", ("Pablo",)
)
conexion.commit() 

cursor.execute(
    """SELECT * FROM empleados"""
)
conexion.commit()

resultados = cursor.fetchall() 
print(resultados)