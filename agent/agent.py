from maps.position import Position
from maps.map import Map
import random
import math
import sys
import numpy as np

class Agent:
    __hint = []
    __coordinate = Position(None, None)
    __agent_map = []
    __map = Map(None, None, None, None, None)
    __teleport = True
    # Map that agent can see (0 for any tile that has not been discovered, 
    # -1 for those that has bee discovered)

    def __init__(self, map):
        self.__map = map

    def get_agent_map(self):
        return self.__agent_map

    def get_coordinate(self):
        return self.__coordinate

    def init_map(self):
        for x in range(self.__map.get_height()):
            row = []
            for y in range(self.__map.get_width()):
                row.append('1')
            self.__agent_map.append(row)

    def spawn(self):
        map = self.__map.get_data()
        while True:
            x = random.randint(0, self.__map.get_height() - 1)
            y = random.randint(0, self.__map.get_width() - 1)
            if ('M' not in map[x][y] and 'P' not in map[x][y] and map[x][y] != '0'):
                self.__agent_map[x][y] = '-'
                return self.__coordinate.set(x, y)


    def __move(self, direction, step):
        map = self.__map.get_data()
        x = self.__coordinate.get_x()
        y = self.__coordinate.get_y()
        while (step > 0):
            if (direction == 0): # Up
                if ('M' in map[x-1][y] or map[x-1][y] == '0' or x == 0):
                    break
                x = x - 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 1): # Down
                if ('M' in map[x+1][y] or map[x+1][y] == '0' or x == self.__map.get_height() - 1):
                    break
                x = x + 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 2): # Left
                if ('M' in map[x][y-1] or map[x][y-1] == '0' or y == 0):
                    break
                y = y - 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 3): # Right
                if ('M' in map[x][y+1] or map[x][y+1] == '0' or y == self.__map.get_width() - 1):
                    break
                y = y + 1
                self.__agent_map[x][y] = '-'
                step = step - 1
        self.__coordinate.set(x, y)

    def __scan(self, type):
        x = self.__coordinate.get_x()
        y = self.__coordinate.get_y()
        for i in range(x - type, x + type + 1):
            for j in range(y - type, y + type + 1):
                if i < 0 or j < 0 or i > self.__map.get_height() - 1 or j > self.__map.get_width() - 1:
                    continue
                self.__agent_map[i][j] = '-'
    
    def __calculate_point(self, x, y):
        sum_point = 0
        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                if i < 0 or j < 0 or i > self.__map.get_height() - 1 or j > self.__map.get_width() - 1:
                    continue
                if (self.__agent_map[i][j] == '1'):
                    sum_point += 1
        return sum_point

    def __choose_action(self):
        map = self.__map.get_data()
        max_count = 0
        current_count = 0 
        step = 0
        recored_dir = 0
        x = self.__coordinate.get_x()
        y = self.__coordinate.get_y()
        if self.__calculate_point(x, y) > 5:
            return max_count, step, recored_dir
        for move in range(1, 5):
            # Move up
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            x -= move
            current_count = self.__calculate_point(x, y)
            if x < 0 or y < 0 or x > self.__map.get_height() - 1 or y > self.__map.get_width() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            if (current_count>max_count):
                step = move
                max_count = current_count
                recored_dir = 1

        for move in range(1, 5):    
            # Move down
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            x += move
            current_count = self.__calculate_point(x, y)
            if x < 0 or y < 0 or x > self.__map.get_height() - 1 or y > self.__map.get_width() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            if (current_count>max_count):
                step = move
                max_count = current_count
                recored_dir = 2

        for move in range(1, 5):
            # Move right
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            y += move
            current_count = self.__calculate_point(x, y)
            if x < 0 or y < 0 or x > self.__map.get_height() - 1 or y > self.__map.get_width() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            if (current_count>max_count):
                step = move
                max_count = current_count
                recored_dir = 3

        for move in range(1, 5):
            # Move left
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            y -= move
            current_count = self.__calculate_point(x, y)
            if x < 0 or y < 0 or x > self.__map.get_height() - 1 or y > self.__map.get_width() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            if (current_count>max_count):
                step = move
                max_count = current_count
                recored_dir = 4
        if recored_dir == 0:
            recored_dir = 5
        return max_count, step, recored_dir

    def action(self):
        max_count, step, recored_dir = self.__choose_action()
        if recored_dir == 0:
            self.__scan(2)
            print("Stand and scan")
        elif recored_dir == 1:
            self.__move(0, step)
            if step == 1 or step == 2:
                self.__scan(1)
            print("Move up", step)
        elif recored_dir == 2:
            self.__move(1, step)
            if step == 1 or step == 2:
                self.__scan(1)
            print("Move down", step)
        elif recored_dir == 3:
            self.__move(3, step)
            if step == 1 or step == 2:
                self.__scan(1)
            print("Move right", step)
        elif recored_dir == 4:
            self.__move(2, step)
            if step == 1 or step == 2:
                self.__scan(1)
            print("Move left", step)
        elif recored_dir == 5 and self.__teleport == True:
            print("Teleport :)))")
            self.teleport()
            self.__teleport = False
        else:
            return False
        return True

        


    def teleport(self):
        map = self.__map.get_data()
        for x in range(0, self.__map.get_height()):
            for y in range(0, self.__map.get_width()):
                current_point = self.__calculate_point(x, y)
                if current_point > 2:
                    if ('M' not in map[x][y] and 'T' not in map[x][y] and map[x][y] != '0'):
                        self.__agent_map[x][y] = '-'
                        self.__coordinate.set(x, y)
                        break

    