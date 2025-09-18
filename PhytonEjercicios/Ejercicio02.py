import pandas as pd 
import matplotlib.pyplot as plt 

datos = {"nombre": ["Pablo", "Juan", "Pedro" , "Rosa"], 
         "gatos" : [2,3,4,5], 
         "perros" : [2,1,3,4]}
df = pd.DataFrame(data=datos)
df

df.plot() 


