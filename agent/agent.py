import maps.position as Position
import random
import math
import sys
import numpy as np

class Agent:
    __hint = []
    __coordinate_x = None
    __coordinate_y = None
    __agent_map = [[]] 
    # Map that agent can see (0 for any tile that has not been discovered, 
    # -1 for those that has bee discovered)

    def __init__(self, coordinate_x, coordinate_y, hint, agent_map):
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__hint = hint
        self.__agent_map = agent_map

    def action(self, coordinate_x, coordinate_y):
        

