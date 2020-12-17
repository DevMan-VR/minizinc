import math    
import random

class Distribution:
  
    @staticmethod
    def gaussian(self, mu=None, sigma=None):

      x = Distribution.uniform(self,-1.0, 1.0)
      y = Distribution.uniform(self,-1.0, 1.0)
      r = x * x + y * y
      while (r >= 1 or r == 0):
        x = Distribution.uniform(self,-1.0, 1.0)
        y = Distribution.uniform(self,-1.0, 1.0)
        r = x * x + y * y
      
      gaussian = x * math.sqrt(-2 * math.log(r) / r)

      if mu is not None and sigma is not None : #Caso con mu y sigma
        return mu + sigma * gaussian
      else:
        return gaussian #Caso gaussiana sin argumentoscalls

    @staticmethod
    def uniform(self, *args):
        if len(args) == 0:
            return random.SystemRandom().uniform(0.0, 1.0)
        if len(args) == 1:
            if isinstance(args[0], int):
                if args[0] <= 0:
                    raise ValueError("Parameter must be positive")
                return random.SystemRandom().randint(0,args[0])
        if len(args) == 2:
            if isinstance(args[0], int) and isinstance(args[1], int):
                if args[1]<= args[0]:
                    raise ValueError("Invalid range")
                if args[1] - args[0] >= (2**31)-1 :
                    raise ValueError("Invalid range")
                return args[0] + self.uniform(self, args[1] - args[0])
            elif isinstance(args[0], float) and isinstance(args[1], float):
                if not args[0] < args[1]:
                    raise ValueError("Invalid range")
                return args[0] + self.uniform(self) * (args[1] - args[0])
        else:
            raise ValueError("too many arguments")

        