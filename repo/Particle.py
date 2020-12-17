class Particle:

    # Arreglo de elementos que componen la particula: [0,1,0.,..]
    __elements = None

    #La energia que generan los elementos de la particula (En este problema seria el equivalente al Peso de la particula)
    #En MKP los pesos de la particula son una matriz (por cada mochila sus elementos pesan distintos)
    __weight = None
    __weightMKP = None

    #La ganancia total que generan los elementos de la particula
    __gain = None

    def __init__(self, elements, weight, gain):
        self.__elements = elements
        self.__weight = weight
        self.__gain = gain
    
    # Set and Get de los elementos
    def set_elements(self, elements):
        self.__elements = elements
    
    def get_elements(self):
        return self.__elements

    # Set and Get de la energia
    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight


    # Set and Get de la ganancia
    def set_gain(self, gain):
        self.__gain = gain

    def get_gain(self):
        return self.__gain

    # Proceso en el que la particula se dividen en un numero determinado de hijos
    def diffusion(self, num_duffusion, ec_moviment, best_son, type_problem):
        sons = []
        #Proceso de Explotacion
        #Se generan los hijos, segun la Ec. de movimiento definida por el algoritmo SFS
        for son in range(num_duffusion):
            sons.append( ec_moviment(self) )
        
        #De las particulas hijas creadas, se selecciona la mejor y se retorna
        if(type_problem == "KP"):
          return best_son(sons, Particle([], 0, 0))

        else:
          return best_son(sons, Particle([], [], 0))

 