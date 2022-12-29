from UI import drawGrid
from maps.map import read_input
from maps.position import Position
import pygame
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
    for i in range(16):
        print(i)
    # pygame.init()
    # screen = pygame.display.set_mode((900,900))
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #     drawGrid(900, 16,screen)
    #     pygame.display.update()
