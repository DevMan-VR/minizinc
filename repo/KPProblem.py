import random

#Esta clase tiene todas las funcionalidades que involucran al problema
class KPProblem:

    #Peso Maximo
    __maxWeight = None

    #Arreglo que define el peso de cada uno de los elementos de la particula
    __weights = None

    #Arreglo que define la ganancia de cada uno de los elementos de la particula
    __gain = None

    type_problem = None


    def __init__(self, maxWeight, weights, gain, type_problem):

        self.type_problem = type_problem
        self.__maxWeight = maxWeight
        self.__weights = weights
        self.__gain = gain

    # Set and Get del peso maximo
    def set_maxWeight(self, maxWeight):
        self.__maxWeight = maxWeight
    
    def get_maxWeight(self):
        return self.__maxWeight

    # Set and Get de las ganancias
    def set_gain(self, gain):
        self.__gain = gain
    
    def get_gain(self):
        return self.__gain

    # Set and Get de las pesos
    def set_weights(self, weights):
        self.__weights = weights
    
    def get_weights(self):
        return self.__weights

    
    # Set and Get del peso maximo
    def set_typeProblem(self, typeProblem):
        self.type_problem = typeProblem
    
    def get_typeProblem(self):
        return self.type_problem

    #Se prueba si una particula es valida, segun la energia maxima
    def _isValid(self, particle):

        if(self.type_problem == "KP"):
          return (particle.get_weight() > 0 and particle.get_weight() <= self.get_maxWeight())

        else:
          return self.__isValidWeightMKP(particle)



    def __isValidWeightMKP(self, particle):

      if(len(particle.get_weight()) == 0): 
        return False

      index = 0
      isFactible = True
      for knapsack_weight in self.__maxWeight:

        if(particle.get_weight()[index] > knapsack_weight or particle.get_weight()[index] == 0):
          #print(particle.get_weight()[index], knapsack_weight)
          isFactible = False
        index += 1

      #print(isFactible, particle.get_elements())
      
      return isFactible



    #Genera una particula aleatoria, esta funcion es del problema, ya que genera la particula con elementos binarios
    def _genRandomParticle(self, dimensionParticula):
        
        new_particle = []

        for i in range(dimensionParticula):
            new_particle.append(random.randint(0,1))

        return new_particle

    #Se define el fitness, segun la ganancia definida por el problema (Knaspsack)
    def _fitness(self, particle):
        energy_total = 0
        index = 0

        for element in particle:
            energy_total += (element * self.get_gain()[index])
            index += 1

        return energy_total

    def _weightParticle(self, particle):


        #print(particle)
        if(self.type_problem == "KP"):
          total_weight = 0
          index = 0

          for element in particle:
              total_weight += (element * self.get_weights()[index])
              index += 1

          return total_weight


        else:
          total_weight = [0] * len(self.__weights)
          #print("Aasdssssdasd",total_weight)
          index_2 = 0
          for knapsack_weight in self.__weights:
            #print(knapsack_weight)
            index_1 = 0
            for element in particle:
              total_weight[index_2] = total_weight[index_2] + (element * knapsack_weight[index_1])
              index_1 += 1
            index_2 += 1
          
          return total_weight





