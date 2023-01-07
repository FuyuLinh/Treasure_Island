import random

from maps.map import Map


class Hint:
    __hint_map = []
    __message = ''
    __map = Map(None, None, None, None, None)

    def __init__(self, __map):
        self.__map = __map
        # choose = random.randint(1, 16)
        choose = 1
        if choose == 1:
            self.__hint_map = self.hint_01()
            self.__message = "Hello this is hint 1"

    def get_message(self):
        return self.__message

    def get_hint_map(self):
        return self.__hint_map


    def verify_hint(self):
        if self.__hint_map[self.__map.get_treasure().get_x()][self.__map.get_treasure().get_y()] == 1:
            return True
        else:
            return False


    def hint_01(self):
        width = self.__map.get_width()
        height = self.__map.get_height()
        val_random = random.randint(1, 12)
        maps = []
        count = 0

        for i in range(0, width):
            maps.append([1] * height)

        while True:
            val_row = random.randint(0, width - 1)
            val_col = random.randint(0, height - 1)
            if maps[val_row][val_col] != 0:
                count += 1
                maps[val_row][val_col] = 0
                if count == val_random:
                    break
        return maps
