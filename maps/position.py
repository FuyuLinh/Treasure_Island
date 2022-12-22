class Position:
    __X = None
    __Y = None
    def __init__(self, x, y):
        self.__X = x
        self.__Y = y

    def set(self, x, y):
        self.__X = x
        self.__Y = y

    def get_x(self):
        return self.__X

    def get_y(self):
        return self.__Y
