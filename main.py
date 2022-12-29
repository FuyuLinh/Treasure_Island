from maps.map import read_input
from maps.position import Position
from agent.agent import Agent

if __name__ == '__main__':
    turn_reveals, turn_free, map_game = read_input('data/Map0.txt')
    # TODO: get treasure location
    # map_game.get_treasure().get_x()
    # map_game.get_treasure().get_y()

    # TODO: get the map
    # map_game.get_data()

    # TODO: get number of region
    # map_game.get_region()

    # TODO: get width, height
    # map_game.get_width()
    # map_game.get_height()

    map = map_game.get_data()
    print(map[8][13])