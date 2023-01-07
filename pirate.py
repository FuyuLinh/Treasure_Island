import math
import random

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
  
  def move(self, treasure_X, treasure_Y, main_map, width, height):
    top, bottom, left, right = False
    value_top = -1
    value_bottom = -1
    value_left = -1
    value_right = -1
    
    if self.__X > 0 and 'M' not in str(main_map[self.__X - 1][self.__Y]) and '0' not in str(main_map[self.__X - 1][self.__Y]):
      top = True
    if self.__X < width - 1 and 'M' not in str(main_map[self.__X + 1][self.__Y]) and '0' not in str(main_map[self.__X + 1][self.__Y]):
      bottom = True
    if self.__Y > 0 and 'M' not in str(main_map[self.__X][self.__Y - 1]) and '0' not in str(main_map[self.__X][self.__Y - 1]):
      left = True
    if self.__Y < height - 1 and 'M' not in str(main_map[self.__X][self.__Y + 1]) and '0' not in str(main_map[self.__X][self.__Y + 1]):
      right = True
    
    temp_list = []
    if top == True:
      value_top = math.sqrt(abs(treasure_X - self.__X - 1)**2 + abs(treasure_Y - self.__Y)**2)
      temp_list.append(value_top)
    if bottom == True:
      value_bottom = math.sqrt(abs(treasure_X - self.__X + 1)**2 + abs(treasure_Y - self.__Y)**2)
      temp_list.append(value_bottom)
    if left == True:
      value_left = math.sqrt(abs(treasure_X - self.__X)**2 + abs(treasure_Y - self.__Y - 1)**2)
      temp_list.append(value_left)
    if right == True:
      value_right = math.sqrt(abs(treasure_X - self.__X)**2 + abs(treasure_Y - self.__Y + 1)**2)
      temp_list.append(value_right)

    if value_top == min(temp_list):
      self.__X = self.__X - 1
      message = 'Pirate go to the top'
    elif value_bottom == min(temp_list):
      self.__X = self.__X + 1
      message = 'Pirate go to the bottom'
    elif value_left == min(temp_list):
      self.__Y = self.__Y - 1
      message = 'Pirate go to the left'
    elif value_right == min(temp_list):
      self.__Y = self.__Y + 1
      message = 'Pirate go to the right'

    return message

  def spawn(self, main_map, width, height):
    temp_list_X = []
    temp_list_Y = []

    for i in range(0, width):
      for j in range(0, height):
        if 'M' in str(main_map[i][j]):
          temp_list_X.append(i)
          temp_list_Y.append(j)
    
    spawn_random = random.randint(0, len(temp_list_X) - 1)

    self.__X = temp_list_X(spawn_random)
    self.__Y = temp_list_Y(spawn_random)

    
