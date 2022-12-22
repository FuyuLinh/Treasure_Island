from maps.position import Position


class Map:
    __width = None
    __height = None
    __region = None
    __treasure = Position(None, None)
    __data = []

    def __init__(self, width, height, region, treasure, data):
        self.__width = width
        self.__height = height
        self.__region = region
        self.__treasure = treasure
        self.__data = data

    def get_treasure(self):
        return self.__treasure

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_region(self):
        return self.__region

    def get_data(self):
        return self.__data


def read_input(path):
    f = open(path, "r")
    size = f.readline().split()
    width = int(size[0])
    height = int(size[1])
    turn_reveal = int(f.readline())
    turn_free = int(f.readline())
    region = int(f.readline())
    temp = f.readline().split()
    treasure = Position(int(temp[0]), int(temp[1]))
    temp = []
    for x in range(height):
        row = f.readline().replace('\n', '').split("; ")
        temp.append(row)
    map_game = Map(width, height, region, treasure, temp)
    return turn_reveal, turn_free, map_game
