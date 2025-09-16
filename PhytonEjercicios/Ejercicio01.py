import pandas as pd
import matplotlib.pyplot as plt

nombre = ["Oliva", "Pablo", "Pepe"]
puntaje = [11.5, 8, 15.5]
intentos = [1,3,2]
califico = ["Sí", "No", "Sí"]
indices = ["a", "b", "c"]
jugadores = {"nombre" : nombre, "puntaje" : puntaje, "intentos" : intentos
             , "califico" : califico}
df = pd.DataFrame(data=jugadores , index = indices)
df

df.plot(kind="line", y = "puntaje", color="red")
plt.show()