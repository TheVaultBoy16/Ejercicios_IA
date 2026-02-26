import random

class Problema_Genetico(object):
    def __init__(self,genes,longitud_individuos,decodifica,fitness,opt):
        self.genes= genes
        self.longitud_individuos= longitud_individuos
        self.decodifica= decodifica
        self.fitness= fitness
        self.opt= opt


def binario_a_decimal(l):
    return sum(x*(2**i) for (i,x) in enumerate(l))

cuad_gen=Problema_Genetico([0,1],10,binario_a_decimal,lambda x: (binario_a_decimal(x)+5)**2,min) # instancia de la clase. opt indica si el problema es de maximizacion o minimizacion



def poblacion_inicial(problema_genetico,N):
   
    aux=[]
    res=[]

    for _ in range(N):
        res.append(aux)
        aux.clear()
        for _ in range(problema_genetico.longitud_individuos):
            aux.append(random.choice(problema_genetico.genes))
    return res 

"""     return [[random.choice(problema_genetico.genes)
    for _ in range(problema_genetico.longitud_individuos)]
    for _ in range(N)] """


print (poblacion_inicial(cuad_gen,6))

def cruza(c1,c2):
    hijo1=[]
    hijo2=[]
    pos=random.randint(1,len(c1))

    hijo1= c1[: pos] + c2[pos: ]
    hijo2= c2[: pos] + c1[pos: ]

    return [hijo1,hijo2]


def cruza_padres(padres):
    hijos=[]
    for i in range(0,len(padres),2):
        hijos+=(cruza(padres[i],padres[i+1]))
    return hijos


pob = poblacion_inicial(cuad_gen,6)

print(cruza(pob[1],pob[2]))

print(cruza_padres(poblacion_inicial(cuad_gen,6)))

def muta(c,prob,genes):
    cm=c[:] # una copia
    for i in range(len(cm)):
        if random.random()< prob:
            cm[i]=random.choice(genes)
    return cm

def muta_individuos(poblacion,prob,genes):
    res=[]

    for i in poblacion:
        res.append(muta(i,prob,genes))
    
    return res

print (muta(pob[1],0.5,cuad_gen.genes))

print(muta_individuos(poblacion_inicial(cuad_gen,6),0.5,cuad_gen.genes))

def selecciona_un_torneo(problema_genetico, poblacion,k):
    participantes=random.sample(poblacion,k) #selecciona k participantes
    return 


def selecciona_n_torneo(problema_genetico, poblacion,k,n):







