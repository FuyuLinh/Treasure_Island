from maps.map import Map
from maps.position import Position
import math
import random


class Pirate:
    __position = Position(None, None)
    __map = Map(None, None, None, None, None)

    def __init__(self, map):
        self.__map = map

    def get_coordinate(self):
        return self.__position
    def get_position(self):
        return self.__position
    def move(self):
        x = self.__position.get_x()
        y = self.__position.get_y()
        top = bottom = left = right = False
        value_top = -1
        value_bottom = -1
        value_left = -1
        value_right = -1

        if x > 0 and 'M' not in str(self.__map.get_data()[x - 1][y]) and '0' not in str(
                self.__map.get_data()[x - 1][y]):
            top = True
        if x < self.__map.get_height() - 1 and 'M' not in str(self.__map.get_data()[x + 1][y]) and '0' not in str(
                self.__map.get_data()[x + 1][y]):
            bottom = True
        if y > 0 and 'M' not in str(self.__map.get_data()[x][y - 1]) and '0' not in str(
                self.__map.get_data()[x][y - 1]):
            left = True
        if y < self.__map.get_width() - 1 and 'M' not in str(self.__map.get_data()[x][y + 1]) and '0' not in str(
                self.__map.get_data()[x][y + 1]):
            right = True

        temp_list = []
        if top == True:
            value_top = math.sqrt(abs(self.__map.get_treasure().get_x() - x - 1) ** 2 + abs(self.__map.get_treasure().get_y() - y) ** 2)
            temp_list.append(value_top)
        if bottom == True:
            value_bottom = math.sqrt(abs(self.__map.get_treasure().get_x() - x + 1) ** 2 + abs(self.__map.get_treasure().get_y() - y) ** 2)
            temp_list.append(value_bottom)
        if left == True:
            value_left = math.sqrt(abs(self.__map.get_treasure().get_x() - x) ** 2 + abs(self.__map.get_treasure().get_y() - y - 1) ** 2)
            temp_list.append(value_left)
        if right == True:
            value_right = math.sqrt(abs(self.__map.get_treasure().get_x() - x) ** 2 + abs(self.__map.get_treasure().get_y() - y + 1) ** 2)
            temp_list.append(value_right)

        if value_top == min(temp_list):
            x = x - 1
            message = 'Pirate go to the top'
        elif value_bottom == min(temp_list):
            x = x + 1
            message = 'Pirate go to the bottom'
        elif value_left == min(temp_list):
            y = y - 1
            message = 'Pirate go to the left'
        elif value_right == min(temp_list):
            y = y + 1
            message = 'Pirate go to the right'
        self.__position.set(x, y)
        return message

    def spawn(self):
        temp_list_X = []
        temp_list_Y = []

        for i in range(0, self.__map.get_width()):
            for j in range(0, self.__map.get_height()):
                if 'P' in str(self.__map.get_data()[i][j]):
                    temp_list_X.append(i)
                    temp_list_Y.append(j)

        spawn_random = random.randint(0, len(temp_list_X) - 1)

        self.__position.set(temp_list_X[spawn_random], temp_list_Y[spawn_random])
