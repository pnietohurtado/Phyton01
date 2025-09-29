import pandas as pd 
import numpy as np

data2 = pd.Series(data = ["dato 1", "dato 2", "dato 3"], index = [pd.Period("2020-09-01"), pd.Period("2021-08-12"), pd.Period("2018-07-27")])
print(data2)

print(data2.index)
#data2.index = data2.index.tolist
print(data2.index)

fechas = ["Jun 30, 2019", "Jul 31 2021", "May 26, 2023"]
Data = pd.DataFrame(data = ["dato 1", "dato 2", "dato 3"], index = fechas, columns = ["Datos"])
print(Data)