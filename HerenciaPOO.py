import math 
class Punto(): 

    def __init__(self, x = 0, y= 0):
        self.x = x
        self.y = y
    
    @property
    def x(self): 
        print("Doy x: ")
        return self.__x
    
    @property
    def y(self): 
        print("Doy y: ")
        return self.__y
    
    @x.setter 
    def x(self,x): 
        print("Cambio de la x! ")
        self.__x = x
    
    
    @y.setter 
    def y(self,y): 
        print("Cambio de la y! ")
        self.__y= y


class Punto3D(Punto): 
    def __init__(self, x=0, y=0, z = 0):
        super().__init__(x, y)
        self.z = z 
    
    @property
    def z(self): 
        print("Doy z: ")
        return self.__z
    
    @z.setter 
    def z(self,z): 
        print("Cambio de la z! ")
        self.__z = z

    def mostrar(self): 
        return super().mostrar()+ " : " + str(self.z)
    

p3d = Punto3D(4,5,6)
print(p3d.x)