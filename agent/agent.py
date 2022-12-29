import maps.position as Position
import maps.map as map
import random
import math
import sys
import numpy as np

class Agent:
    __hint = []
    __coordinate = Position(None, None)
    __agent_map = [] 
    # Map that agent can see (0 for any tile that has not been discovered, 
    # -1 for those that has bee discovered)

    def __init__(self, coordinate, hint, agent_map):
        self.__coordinate = coordinate
        self.__hint = hint
        self.__agent_map = agent_map

    def init_map(self, width, height):
        for x in range(height):
            row = []
            for y in range(width):
                row.append('0')
            self.__agent_map.append(row)

    def spawn(self, width, height, map):
        while True:
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            if ('M' not in map[x][y] and 'P' not in map[x][y] and map[x][y] != '0'):
                self.__agent_map[x][y].append('-1')
                return self.__coordinate.set(x, y)

    def action(self, map):
        random_action = random.randint(0, 3)
        if (random_action == 0): # verify if the hint is true or not
            in_progress
        elif (random_action == 1): # move 1-2 steps and perform small scan
            move = random.choice([1, 2])
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            while True:
                step = random.randint(0, 3)
                if (step == 0):
                    x = x + move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    if ('T' in map[x - 1][y - 1]):
                        return self.__coordinate.set(x - 1, y - 1)
                    if ('T' in map[x - 1][y]):
                        return self.__coordinate.set(x - 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    if ('T' in map[x][y - 1]):
                        return self.__coordinate.set(x, y - 1)
                    if ('T' in map[x][y + 1]):
                        return self.__coordinate.set(x, y + 1)
                    if ('T' in map[x + 1][y - 1]):
                        return self.__coordinate.set(x + 1, y - 1)
                    if ('T' in map[x + 1][y]):
                        return self.__coordinate.set(x + 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 1):
                    x = x - move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    if ('T' in map[x - 1][y - 1]):
                        return self.__coordinate.set(x - 1, y - 1)
                    if ('T' in map[x - 1][y]):
                        return self.__coordinate.set(x - 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    if ('T' in map[x][y - 1]):
                        return self.__coordinate.set(x, y - 1)
                    if ('T' in map[x][y + 1]):
                        return self.__coordinate.set(x, y + 1)
                    if ('T' in map[x + 1][y - 1]):
                        return self.__coordinate.set(x + 1, y - 1)
                    if ('T' in map[x + 1][y]):
                        return self.__coordinate.set(x + 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 2):
                    y = y + move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    if ('T' in map[x - 1][y - 1]):
                        return self.__coordinate.set(x - 1, y - 1)
                    if ('T' in map[x - 1][y]):
                        return self.__coordinate.set(x - 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    if ('T' in map[x][y - 1]):
                        return self.__coordinate.set(x, y - 1)
                    if ('T' in map[x][y + 1]):
                        return self.__coordinate.set(x, y + 1)
                    if ('T' in map[x + 1][y - 1]):
                        return self.__coordinate.set(x + 1, y - 1)
                    if ('T' in map[x + 1][y]):
                        return self.__coordinate.set(x + 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 3):
                    y = y - move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    if ('T' in map[x - 1][y - 1]):
                        return self.__coordinate.set(x - 1, y - 1)
                    if ('T' in map[x - 1][y]):
                        return self.__coordinate.set(x - 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    if ('T' in map[x][y - 1]):
                        return self.__coordinate.set(x, y - 1)
                    if ('T' in map[x][y + 1]):
                        return self.__coordinate.set(x, y + 1)
                    if ('T' in map[x + 1][y - 1]):
                        return self.__coordinate.set(x + 1, y - 1)
                    if ('T' in map[x + 1][y]):
                        return self.__coordinate.set(x + 1, y)
                    if ('T' in map[x + 1][y + 1]):
                        return self.__coordinate.set(x + 1, y + 1)
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
        elif (random_action == 2): # move 3-4 steps
            move = random.choice([3, 4])
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            while True:
                step = random.randint(0, 3)
                if (step == 0):
                    x = x + move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 1):
                    x = x - move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 2):
                    y = y + move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
                elif (step == 3):
                    y = y - move
                    if (map[x][y] == '0' or 'M' in map[x][y]):
                        continue
                    self.__agent_map[x][y].append('-1')
                    return self.__coordinate.set(x, y)
        elif (random_action == 3): # stay and perform large scan
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            if ('T' in map[x - 1][y - 1]):
                return self.__coordinate.set(x - 1, y - 1)
            if ('T' in map[x - 1][y]):
                return self.__coordinate.set(x - 1, y)
            if ('T' in map[x + 1][y + 1]):
                return self.__coordinate.set(x + 1, y + 1)
            if ('T' in map[x][y - 1]):
                return self.__coordinate.set(x, y - 1)
            if ('T' in map[x][y + 1]):
                return self.__coordinate.set(x, y + 1)
            if ('T' in map[x + 1][y - 1]):
                return self.__coordinate.set(x + 1, y - 1)
            if ('T' in map[x + 1][y]):
                return self.__coordinate.set(x + 1, y)
            if ('T' in map[x + 1][y + 1]):
                return self.__coordinate.set(x + 1, y + 1)
            if ('T' in map[x - 2][y - 2]):
                return self.__coordinate.set(x - 2, y - 2)
            if ('T' in map[x - 2][y - 1]):
                return self.__coordinate.set(x - 2, y - 1)
            if ('T' in map[x - 2][y]):
                return self.__coordinate.set(x - 2, y)
            if ('T' in map[x - 2][y + 1]):
                return self.__coordinate.set(x - 2, y + 1)
            if ('T' in map[x - 2][y + 2]):
                return self.__coordinate.set(x - 2, y + 2)
            if ('T' in map[x - 1][y - 2]):
                return self.__coordinate.set(x - 1, y - 2)
            if ('T' in map[x - 1][y + 2]):
                return self.__coordinate.set(x - 1, y + 2)
            if ('T' in map[x][y - 2]):
                return self.__coordinate.set(x + 1, y - 2)
            if ('T' in map[x][y + 2]):
                return self.__coordinate.set(x - 1, y + 2)
            if ('T' in map[x + 1][y - 2]):
                return self.__coordinate.set(x + 1, y - 2)
            if ('T' in map[x + 1][y + 2]):
                return self.__coordinate.set(x + 1, y + 2)
            if ('T' in map[x + 2][y - 2]):
                return self.__coordinate.set(x + 2, y - 2)
            if ('T' in map[x + 2][y - 1]):
                return self.__coordinate.set(x + 2, y - 1)
            if ('T' in map[x + 2][y]):
                return self.__coordinate.set(x + 2, y)
            if ('T' in map[x + 2][y + 1]):
                return self.__coordinate.set(x + 2, y + 1)
            if ('T' in map[x + 2][y + 2]):
                return self.__coordinate.set(x + 2, y + 2)
            self.__agent_map[x][y].append('-1')
            return self.__coordinate.set(x, y)

    def teleport(self, width, height, map):
        while True:
            x = random.randint(0, height - 1)
            y = random.randint(0, width - 1)
            if ('M' not in map[x][y] and 'T' not in map[x][y] and map[x][y] != '0'):
                self.__agent_map[x][y].append('-1')
                return self.__coordinate.set(x, y)