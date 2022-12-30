class Pirate:
  __X = None
  __Y = None
  
  def __init__(self,x,y) :
    self.__X = x
    self.__Y = y

  def verify_Hint(hint, treasure_X, treasure_Y):
    if hint[treasure_X][treasure_Y] == 1:
      return True
    else:
      return False


