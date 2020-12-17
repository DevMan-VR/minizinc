import math    
from Distribution import Distribution

class Binarization:
  
  @staticmethod
  def standard(x=0):
    return 1 if Distribution.uniform(x) <= x else 0

  @staticmethod
  def sShape2(x=0):
    return (1 / (1 + math.pow(math.e, -x)))
  
  @staticmethod
  def toBinary(x=0):
    return Binarization.standard(Binarization.sShape2(x))