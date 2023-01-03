from maps.position import Position
from ui.UI import draw_grid, redraw
from maps.map import read_input

import pygame


def is_win(knowledge_map, treasure):
    if knowledge_map[treasure.get_x()][treasure.get_y()] == 1:
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

    while True:
        # TODO: set knowledge_map here
        knowledge_map = []

        # TODO: set location of agent here
        agent = Position(5, 10)

        treasure = map_game.get_treasure()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # TODO: game run in here
                    print("game turn")

                # TODO: move screen
                if event.key == pygame.K_UP and start_map[0] > 0:
                    start_map[0] -= 1
                if event.key == pygame.K_DOWN and start_map[0] + 15 < map_game.get_height() - 1:
                    start_map[0] += 1
                if event.key == pygame.K_LEFT and start_map[1] > 0:
                    start_map[1] -= 1
                if event.key == pygame.K_RIGHT and start_map[1] + 15 < map_game.get_height() - 1:
                    start_map[1] += 1

        redraw(start_map, screen, map_game.get_data(), map_game.get_region(), agent, knowledge_map, treasure)
        pygame.display.update()
        clock.tick(60)
