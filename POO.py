"""
import math 
class Punto(): 
    def _init_(self, x = 0, y = 0): 
        self.x = x
        self.y = y
    def mostrar(self): 
        return str(self.x)+" : " + str(self.y)
    def distancia(self, otro): 
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt((dx * dx + dy*dy))
 
punto1 = Punto() 
punto1.x = 3
punto1.y = 6
print(punto1.x)
print(punto1.mostrar())

punto2 = Punto(5,7)
print("Distancia entre ambos puntos ",punto1.distancia(punto2))
"""


"""
class Circulo(): 
    def __init__(self, radio):
        self.radio= radio
    
    @property   # Método getter 
    def radio(self): 
        print("Estoy dando el radio!")
        return self.__radio 
    
    @radio.setter  # Método setter 
    def radio(self, radio): 
        if radio >= 0: 
            self.__radio = radio 
        else: 
            print("Radio debe ser positivo!")
            self.__radio = 0

c1 = Circulo(23)
c2 = Circulo(-2)
c1.radio
c2.radio
"""

