import time

import pygame

from agent.agent import Agent
from hint import Hint
from maps.map import read_input
from ui.UI import draw_grid, redraw


def is_win(knowledge_map, treasure):
    if knowledge_map[treasure.get_x()][treasure.get_y()] == '-':
        return True
    return False


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

    pygame.init()
    screen = pygame.display.set_mode((1200, 840))
    clock = pygame.time.Clock()

    start_map = [0, 0]
    draw_grid(screen)
    agent = Agent(map_game)
    agent.init_map()
    agent.spawn()
    while not is_win(agent.get_agent_map(), map_game.get_treasure()):
        # TODO: set knowledge_map here

        # TODO: set location of agent here

        treasure = map_game.get_treasure()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # TODO: move screen
                if event.key == pygame.K_UP and start_map[0] > 0:
                    start_map[0] -= 1
                if event.key == pygame.K_DOWN and start_map[0] + 15 < map_game.get_height() - 1:
                    start_map[0] += 1
                if event.key == pygame.K_LEFT and start_map[1] > 0:
                    start_map[1] -= 1
                if event.key == pygame.K_RIGHT and start_map[1] + 15 < map_game.get_height() - 1:
                    start_map[1] += 1
                if event.key == pygame.K_SPACE:
                    hint = Hint(map_game)
                    agent.receive_hint(hint)
                    print(hint.get_message())
                    if not agent.action():
                        break
                    print(agent.get_coordinate().get_x(), agent.get_coordinate().get_y())
                    if map_game.get_height() - 1 - agent.get_coordinate().get_x() < 8:
                        start_map[0] = map_game.get_height() - 16
                    elif agent.get_coordinate().get_x() < 7:
                        start_map[0] = 0
                    else:
                        start_map[0] = agent.get_coordinate().get_x() - 7
                    if map_game.get_width() - 1 - agent.get_coordinate().get_y() < 8:
                        start_map[1] = map_game.get_width() - 16
                    elif agent.get_coordinate().get_y() < 7:
                        start_map[1] = 0
                    else:
                        start_map[1] = agent.get_coordinate().get_y() - 7
        redraw(start_map, screen, map_game.get_data(), map_game.get_region(), agent.get_coordinate(),
               agent.get_agent_map(), treasure)
        pygame.display.update()
        time.sleep(1)
        clock.tick(60)

    if is_win(agent.get_agent_map(), map_game.get_treasure()):
        print('Victory')
