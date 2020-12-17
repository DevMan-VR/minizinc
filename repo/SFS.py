import random

from KPProblem import KPProblem
from Particle import Particle
from Binarization import Binarization
from Distribution import Distribution

#Stocastic Fractal Search Hereda las funciones determinadas por el problema a resolver
class SFS(KPProblem):
    
    __dimension = None
    __poblation = None
    __G_BEST = None

    def __init__(self, max_weight, energies, gain, type_problem = "KP"):

        self.__dimension = len(gain)

        #Se inicializa el padre, el problema que se va a resolver
        KPProblem.__init__(self, max_weight, energies , gain, type_problem)
    
    #Genera un poblacion aleatoria de particulas, la cual se puede utilizar como semilla
    def __genPoblation(self, num_particles):
        seed = []

        for new_particle in range(num_particles):
            if(self.get_typeProblem() == "KP"):
              seed.append( Particle([], 0, 0) )
            else:
              seed.append( Particle([], [], 0) )

            posX = 0

            #Que se genere una particula valida
            while (not self._isValid(seed[new_particle])):
                particle_random = self._genRandomParticle(self.__dimension)
                seed[new_particle] = Particle(particle_random, self._weightParticle(particle_random), self._fitness(particle_random))

            posX += 1

        return seed
       
    # Proceso en el que las particulas evolucionan hasta encontrar una mejor particula, cuyo fitness se acerca al valor optimo
    def cycle(self, generations, num_difussion, printer, size_poblation = 5 ):

        #Se genera la semilla inicial
        self.__poblation = self.__genPoblation( size_poblation )

        T = 1

        #Se inicializa la mejor Sol. Global con una particula de fitness 0
        if(self.get_typeProblem() == "KP"):
          self.__G_BEST = Particle([], 0, 0)
        else:
          self.__G_BEST = Particle([], [], 0)

        while(T <= generations):

            #Se compara la mejor particula global (GBEST) hasta ahora, con cada particula de la generacion T
            self.__G_BEST = self.__bestParticle(self.__poblation, self.__G_BEST)

            pos_particle = 0

            for particle in self.__poblation:

                #A la particula padre en la posiscion pos_particle, es remplazada por la mejor particula encontrada en su difusion 
                self.__poblation[pos_particle] = particle.diffusion(num_difussion, self.__movement, self.__bestParticle, self.get_typeProblem)

                pos_particle += 1

            T += 1

        # Proceso de actualizacion de las particulas
        for fase in range(2):
            self.__update(fase)

        if(printer):
          print("############# GBEST #############")
          print("Particula:",self.__G_BEST.get_elements())
          print("Peso / Peso Maximo:",self.__G_BEST.get_weight(), "/", self.get_maxWeight())
          print("Beneficio Obtenido:",self.__G_BEST.get_gain())
        return self.__G_BEST.get_gain()

    #Se determina la mejor particula de una poblacion (Mejor Local), o bien de generaciones (Mejor Global)
    def __bestParticle(self, poblation, Lbest):

        new_best = Lbest

        for particle in poblation:
            if(particle.get_gain() > new_best.get_gain()):
                new_best = particle
            
        return new_best
        
    #Movimientos de la particula, sus ecuaciones estan definidas el algoritmo
    def __movement(self, particle):

        dvest = self.__dynamicDvest()
        media = 1

        isValid = False

        #Exploracion de una particula o salto Gausseano
        while( not isValid ):

            new_particle = []

            #Se generan un arreglo [0,0,1,1,0,...] segun la distribucion Gaussiana
            for element in particle.get_elements():
                newElement = Binarization.toBinary(Distribution.gaussian(Distribution, media, dvest))
                new_particle.append(newElement)

            new_particle = Particle(new_particle, self._weightParticle(new_particle) ,self._fitness(new_particle))
            isValid = self._isValid(new_particle)


        return new_particle
    
    def __dynamicDvest(self):
        return 1

    def __genRandomNumber():
        return random.uniform(0,1)

    def __update(self, fase):

        index_particle = 0

        for particle in self.__poblation:

            # Indice Particulas aleatorias de la poblacion
            ir = random.randint( 0, len(self.__poblation) - 1 )
            it = random.randint( 0, len(self.__poblation) - 1 )

            pr = self.__poblation[ir].get_elements()
            pt = self.__poblation[it].get_elements()


            pai = self.__particle_pai(particle, len(self.__poblation))
            
            pos_particle = 0

            new_particle = []
            for element in particle.get_elements():

            # Primer proceso de actualizacion
                e = random.uniform(0,1)
                if(fase == 1):
                    if( e >= pai ):
                        # Eq (6)
                        pi = Binarization.toBinary( pr[pos_particle] - e * (pt[pos_particle] - element) )

                        new_particle.append(pi)
                    else:
                        new_particle.append(element)
                # Segundo proceso de Actualizacion
                else:
                    if( e > 0.5 ):
                        pi = Binarization.toBinary( element + e*( pt[pos_particle] - pr[pos_particle] )  )

                    else:
                        pi = Binarization.toBinary( element - e*( pt[pos_particle] - self.__G_BEST.get_elements()[pos_particle] ) )


                    new_particle.append(pi)

                pos_particle += 1
            
            # Se updatea la particula segun la Eq (6)
            self.__poblation[index_particle] = Particle( new_particle, self._weightParticle(new_particle), self._fitness(new_particle) )
                
            index_particle += 1              

    # Se obtiene el rank de uan particula respecto a la mejor particulap pasado por parametro
    def __particle_rank(self, particle): 
        return ( particle.get_gain() / self.__G_BEST.get_gain() )
  
    # Se retorna la probabilidad de seleccion a una particula
    def __particle_pai(self, particle, num_particles):
        return ( self.__particle_rank(particle) / num_particles )
    