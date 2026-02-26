import random, time, math
from itertools import permutations

class Viajante_n():
 
    def __init__(self,n,escala): #ciudades=estado
        super().__init__()
        self.n=n
        self.escala=escala
        self.ciudades=range(1,n)
        self.coordenadas=dict()
        for i in self.ciudades:
            self.coordenadas[i]=[random.randrange(-escala, escala),random.randrange(-escala, escala)]


    def distancia_circuito(self,lc): # lc lista de ciudades (la primera despues de la última), d = √((x2 - x1)² + (y2 - y1)²)
        #coord_c1= lc[0]
        #coord_c2= lc[1]
        res=0
        coordenadas=dict()
        for i in lc:
            coordenadas[i]=[random.randrange(-self.escala, self.escala),random.randrange(-self.escala, self.escala)]
        #math.hypot(coord_c1[0]-coord_c2[0],coord_c1[1]-coord_c2[1])
        #sum(self.escala(lc[i],lc[i+1]) for i in range (len(lc)-1)) + self.escala(lc[-1],lc[0])
        for i in range(len(lc)-1):
            coord_c1= coordenadas[lc[i]]
            coord_c2= coordenadas[lc[i+1]]
            res+=math.hypot(coord_c1[0]-coord_c2[0],coord_c1[1]-coord_c2[1])
        
        coord_c1= coordenadas[lc[-1]]
        coord_c2= coordenadas[lc[0]]
        res+=math.hypot(coord_c1[0]-coord_c2[0],coord_c1[1]-coord_c2[1])
        return res


pv5=Viajante_n(5,3)
print("Ciudades pv5: {}".format(pv5.ciudades))
print("Coordenadas pv5: {}".format(pv5.coordenadas))      
circuito5=[3,1,4,5,2]
print("Distancia recorrida circuito {}: {}".format(circuito5, pv5.distancia_circuito(circuito5)))