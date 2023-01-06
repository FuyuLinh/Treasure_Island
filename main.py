from maps.map import read_input
from maps.position import Position
from agent.agent import Agent
import mapGenerate

if __name__ == '__main__':
    turn_reveals, turn_free, map_game = read_input('data/Map2.txt')
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

    agent = Agent(map_game)
    agent.init_map()
    agent.spawn()
    # mapGenerate.print_map(agent.get_agent_map())
    print(agent.get_coordinate().get_x(), agent.get_coordinate().get_y())
    # agent.action()
    # print(agent.get_coordinate().get_x(), agent.get_coordinate().get_y())
    # mapGenerate.print_map(agent.get_agent_map())
    for i in range(500):
        print(i)
        r = input()
        if agent.action() == False:
            break
        print(agent.get_coordinate().get_x(), agent.get_coordinate().get_y())
        mapGenerate.print_map(agent.get_agent_map())