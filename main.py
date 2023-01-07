import time

import pygame

from agent.agent import Agent
from hint import Hint
from maps.map import read_input
from pirate import Pirate
from ui.UI import draw_grid, redraw, START_MAP, draw_log


def is_win(knowledge_map, treasure):
    if knowledge_map[treasure.get_x()][treasure.get_y()] == '-':
        return True
    return False
def is_lose(pirate,treasure):
    if pirate.get_position().get_x() == treasure.get_x() and pirate.get_position().get_y() == treasure.get_y():
        return True
    return False


def print_log(index, string, result):
    path = f'log{index}.txt'
    f = open(path, "w")
    f.write(str(len(string))+'\n')
    f.write(result + '\n')
    for row in string:
        f.write(str(row)+'\n')

    f.close()

if __name__ == '__main__':
    index = 2
    turn_reveals, turn_free, map_game = read_input(f'data/Map{index}.txt')
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
    screen = pygame.display.set_mode((1300, 840))
    clock = pygame.time.Clock()
    log = []
    start_map = [0, 0]
    draw_grid(screen)
    draw_log(screen, 850, START_MAP)
    agent = Agent(map_game)
    agent.init_map()
    agent.spawn()
    pirate = Pirate(map_game)
    pirate.spawn()
    turn = 1
    while True:
        hint = Hint(map_game,pirate,agent)
        if hint.verify_hint():
            log.append('Turn 0')
            log.append(f'The agent spawn at {agent.get_coordinate().get_x()} {agent.get_coordinate().get_y()}')
            log.append(f'The pirate is free at the beginning of the {turn_free}th turn')
            log.append(hint.get_message())
            agent.merge_hint(hint)
            break

    while not (is_win(agent.get_agent_map(), map_game.get_treasure()) or is_lose(pirate,map_game.get_treasure())):
        # TODO: set knowledge_map here

        # TODO: set location of agent here
        log.append('Turn '+ str(turn))
        treasure = map_game.get_treasure()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if turn_reveals == turn:
            log.append(f'The pirate at {pirate.get_position().get_x()} {pirate.get_position().get_y()}')
        if turn == turn_free:
            log.append(f'The pirate free')
        if turn > turn_free:
            log.append(f'{pirate.move()} then {pirate.move()}')
        hint = Hint(map_game,pirate,agent)
        agent.receive_hint(hint)
        log.append(hint.get_message())
        log.append(agent.action())
        log.append(agent.action())
        print(f'The pirate at {pirate.get_position().get_x()} {pirate.get_position().get_y()}')
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
        time.sleep(0.1)
        clock.tick(60)
        turn += 1
    if is_win(agent.get_agent_map(), map_game.get_treasure()):
        print_log(index,log,"WIN")
    if is_lose(pirate,map_game.get_treasure()):
        print_log(index, log, "LOSE")

    del agent
    del pirate
    del map_game
