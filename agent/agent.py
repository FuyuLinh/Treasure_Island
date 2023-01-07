from maps.position import Position
from maps.map import Map
import random


class Agent:
    __hint = []
    __coordinate = Position(None, None)
    __agent_map = []
    __map = Map(None, None, None, None, None)
    __teleport = True

    # Map that agent can see (0 for any tile that has not been discovered,
    # -1 for those that has been discovered)

    def __init__(self, map):
        self.__map = map

    def get_agent_map(self):
        return self.__agent_map

    def get_coordinate(self):
        return self.__coordinate

    def receive_hint(self, hint):
        self.__hint.append(hint)

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
            if (direction == 0):  # Up
                if x == 0 or 'M' in map[x - 1][y] or map[x - 1][y] == '0':
                    break
                x = x - 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 1):  # Down
                if x == self.__map.get_height() - 1 or 'M' in map[x + 1][y] or map[x + 1][y] == '0':
                    break
                x = x + 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 2):  # Left
                if y == 0 or 'M' in map[x][y - 1] or map[x][y - 1] == '0':
                    break
                y = y - 1
                self.__agent_map[x][y] = '-'
                step = step - 1
            elif (direction == 3):  # Right
                if y == self.__map.get_width() - 1 or 'M' in map[x][y + 1] or map[x][y + 1] == '0':
                    break
                y = y + 1
                self.__agent_map[x][y] = '-'
                step = step - 1
        self.__coordinate.set(x, y)

    def merge_hint(self, hint):
        if hint.verify_hint():
            for i in range(0, self.__map.get_height()):
                for j in range(0, self.__map.get_width()):
                    if hint.get_hint_map()[i][j] == 0 and self.__agent_map[i][j] != "-":
                        self.__agent_map[i][j] = "-"
        else:
            for i in range(0, self.__map.get_height()):
                for j in range(0, self.__map.get_width()):
                    if hint.get_hint_map()[i][j] == 1 and self.__agent_map[i][j] != "-":
                        self.__agent_map[i][j] = "-"

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
        # print("point achieved:", sum_point, "at", x,":",y)
        return sum_point

    def __calculate_hint_point(self, hint):
        sum_point = 0
        for i in range(0, self.__map.get_height()):
            for j in range(0, self.__map.get_width()):
                if hint.get_hint_map()[i][j] == 0 and self.__agent_map[i][j] != "-":
                    sum_point += 1
        for i in range(0, self.__map.get_height()-2):
            for j in range(0, self.__map.get_width()-2):
                if hint.get_hint_map()[i][j] == 1 and self.__agent_map[i][j] != "-":
                    sum_point += 1
        return sum_point / 2

    def __choose_action(self):
        map = self.__map.get_data()
        max_count = 0
        current_count = 0
        step = 0
        recored_dir = 0

        # Examine at its standing
        x = self.__coordinate.get_x()
        y = self.__coordinate.get_y()
        if self.__calculate_point(x, y) != 0:
            return step, recored_dir

        # Examine up direction
        for move in range(1, 5):
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            x -= move
            if x < 0 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            current_count = self.__calculate_point(x, y)
            if (current_count > max_count):
                step = move
                max_count = current_count
                recored_dir = 1

        # Examine down direction
        for move in range(1, 5):
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            x += move
            if x > self.__map.get_height() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            current_count = self.__calculate_point(x, y)
            if (current_count > max_count):
                step = move
                max_count = current_count
                recored_dir = 2

        # Examine right direction
        for move in range(1, 5):
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            y += move
            if y > self.__map.get_width() - 1 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            current_count = self.__calculate_point(x, y)
            if (current_count > max_count):
                step = move
                max_count = current_count
                recored_dir = 3

        # Examine left direction
        for move in range(1, 5):
            x = self.__coordinate.get_x()
            y = self.__coordinate.get_y()
            y -= move
            if y < 0 or 'P' in map[x][y] or 'M' in map[x][y] or map[x][y] == '0':
                break
            current_count = self.__calculate_point(x, y)
            if (current_count > max_count):
                step = move
                max_count = current_count
                recored_dir = 4

        # Examine verify hint
        for i in range(len(self.__hint)):
            if(len(self.__hint)>0):
                if self.__calculate_hint_point(self.__hint[i]) > 25:
                    recored_dir = 6
                    step = i
                    break

        if (recored_dir == 0):
            # print("Record_dir:", recored_dir)
            return step, 5
        # print("Record_dir:", recored_dir)
        return step, recored_dir

    def action(self):
        step, recored_dir = self.__choose_action()
        # print("Record taken:", recored_dir)
        if recored_dir == 0:
            self.__scan(2)
            return "The agent has stand still and perform BIG SCAN"

        # Move up
        elif recored_dir == 1:
            self.__move(0, step)
            if step == 1 or step == 2:
                self.__scan(1)
                return "The agent has move UP " + str(step) + " steps and perform SMALL SCAN"
            return "The agent has move UP " + str(step) + " steps"

        # Move down
        elif recored_dir == 2:
            self.__move(1, step)
            if step == 1 or step == 2:
                self.__scan(1)
                return "The agent has move DOWN " + str(step) + " steps and perform SMALL SCAN"
            return "The agent has move DOWN " + str(step) + " steps"

        # Move right
        elif recored_dir == 3:
            self.__move(3, step)
            if step == 1 or step == 2:
                self.__scan(1)
                return "The agent has move RIGHT " + str(step) + " steps and perform SMALL SCAN"
            return "The agent has move RIGHT " + str(step) + " steps"

        # Move left
        elif recored_dir == 4:
            self.__move(2, step)
            if step == 1 or step == 2:
                self.__scan(1)
                return "The agent has move LEFT " + str(step) + " steps and perform SMALL SCAN"
            return "The agent has move LEFT " + str(step) + " steps"

        # Teleport
        elif recored_dir == 5 and self.__teleport:
            self.__teleport()
            self.__teleport = False
            return "The agent has just TELEPORTED. What a magic move +_+"

        # Verify_hint
        elif recored_dir == 6:
            self.merge_hint(self.__hint[step])
            isTrue = self.__hint[step].verify_hint()
            self.__hint.pop(step)
            return f'The agent choose to use hint  {step} in queue to verify. IsTrue = {isTrue}'

        else:
            a = int(random.randint(0, 3))
            self.__move(a, 2)
            if a == 0:
                return "Agent cannot find the optimal path. Let's move UP"
            if a == 1:
                return "Agent cannot find the optimal path. Let's move DOWN"
            if a == 2:
                return "Agent cannot find the optimal path. Let's move LEFT"
            if a == 3:
                return "Agent cannot find the optimal path. Let's move RIGHT"

    def __teleport(self):
        map = self.__map.get_data()
        for x in range(0, self.__map.get_height()):
            for y in range(0, self.__map.get_width()):
                current_point = self.__calculate_point(x, y)
                if current_point != 0:
                    # print("Hey I'm in")
                    if ('M' not in map[x][y] and 'T' not in map[x][y] and map[x][y] != '0'):
                        self.__agent_map[x][y] = '-'
                        self.__coordinate.set(x, y)
                        break
