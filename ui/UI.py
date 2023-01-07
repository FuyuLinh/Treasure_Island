import pygame

CELL_WIDTH = 50
START_MAP = 30
MAP_WIDTH = 800
COLOR_PALLET = ['#FFEFDB',
                '#F0FFFF',
                '#F5F5DC',
                '#FFEBCD',
                '#CAFF70',
                '#C1FFC1',
                '#FFFAF0',
                '#DCDCDC',
                '#F8F8FF',
                '#E0FFFF',
                '#FAFAD2',
                '#AB82FF',
                '#EAEAEA',
                '#FFC1C1',
                '#EEE5DE',
                '#6CA6CD',
                '#9FB6CD',
                '#00FF7F',
                '#FFE1FF',
                '#EEEE00']


class Cell(object):
    def __init__(self, start, color=(255, 0, 0)):
        self.pos = start
        self.color = color

    def draw(self, surface, text='', eyes=False):
        x = self.pos[0]
        y = self.pos[1]
        font = pygame.font.SysFont(None, 20)
        label = font.render(text, 1, (0, 0, 0))
        pygame.draw.rect(surface, self.color, (
            START_MAP + y * CELL_WIDTH + 1, START_MAP + x * CELL_WIDTH + 1, CELL_WIDTH - 2, CELL_WIDTH - 2))
        surface.blit(label, ((y + 0.4) * CELL_WIDTH + START_MAP, (x + 0.4) * CELL_WIDTH + START_MAP))


def fill_cell(start_map, surface, map, key, color):
    fill = pygame.Color(color)
    for x in range(16):
        for y in range(16):
            if key in map[x + start_map[0]][y + start_map[1]]:
                cell = Cell([x, y], fill)
                cell.draw(surface, map[x + start_map[0]][y + start_map[1]])


def draw_agent(surface, x, y):
    img = pygame.image.load('agent.png')
    img.convert()
    img0 = pygame.transform.rotozoom(img, 0, 0.04)
    surface.blit(img0, (START_MAP + 10 + y * CELL_WIDTH, START_MAP + 1 + x * CELL_WIDTH))


def draw_grid(surface):
    x = START_MAP
    y = START_MAP
    for line in range(17):
        pygame.draw.line(surface, (255, 255, 255), (x, START_MAP), (x, START_MAP + MAP_WIDTH))
        pygame.draw.line(surface, (255, 255, 255), (START_MAP, y), (START_MAP + MAP_WIDTH, y))
        x = x + CELL_WIDTH
        y = y + CELL_WIDTH


def draw_knowledge(start_map, surface, knowledge_map):
    fill = pygame.Color("#F4F4F4")
    for x in range(16):
        for y in range(16):
            if knowledge_map[x + start_map[0]][y + start_map[1]] == '-':
                cell = Cell([x, y], fill)
                cell.draw(surface, '')


def draw_cordinateX(surface, startX):
    fill = pygame.Color("#000000")
    for x in range(16):
        pygame.draw.rect(surface, fill, (
            0, START_MAP + x * CELL_WIDTH + 1, START_MAP, CELL_WIDTH - 2))
        font = pygame.font.SysFont(None, 20)
        label = font.render(str(startX + x), 1, (255, 255, 255))
        surface.blit(label, (10, (x + 0.4) * CELL_WIDTH + START_MAP))


def draw_cordinateY(surface, startY):
    fill = pygame.Color("#000000")
    for y in range(16):
        pygame.draw.rect(surface, fill, (
            START_MAP + y * CELL_WIDTH + 1, 0, CELL_WIDTH - 2, START_MAP))
        font = pygame.font.SysFont(None, 20)
        label = font.render(str(startY + y), 1, (255, 255, 255))
        surface.blit(label, ((y + 0.4) * CELL_WIDTH + START_MAP, 10))


def draw_treasure(surface, x, y):
    img = pygame.image.load('treasure.png')
    img.convert()
    img0 = pygame.transform.rotozoom(img, 0, 0.125)
    surface.blit(img0, (START_MAP + 1 + y * CELL_WIDTH, START_MAP + 1 + x * CELL_WIDTH))


def draw_log(surface, x, y):
    pygame.draw.line(surface, (255, 255, 255), (x, y), (x, y + 700))
    pygame.draw.line(surface, (255, 255, 255), (x + 400, y), (x + 400, y + 700))
    pygame.draw.line(surface, (255, 255, 255), (x, y), (x + 400, y))
    pygame.draw.line(surface, (255, 255, 255), (x, y + 700), (x + 400, y + 700))
    fill = pygame.Color("#000000")
    pygame.draw.rect(surface, fill, (
        x + 50, y + 200, 100, 50))
    font = pygame.font.SysFont(None, 50)
    label = font.render('LOGS', 1, (255, 255, 255))
    surface.blit(label, (x + 150, y+20))
    # pygame.draw.line(surface, fill, (START_MAP, y), (START_MAP + MAP_WIDTH, y))
    # pygame.draw.rect(surface, fill, (y, x, 400, 700))


def redraw(start_map, surface, map, region, agent, knowledge_map, treasure):
    fill_cell(start_map, surface, map, '0', "#00FFFF")
    for i in range(region - 1):
        fill_cell(start_map, surface, map, str(i + 1), COLOR_PALLET[i + 3])

    draw_cordinateX(surface, start_map[0])
    draw_cordinateY(surface, start_map[1])
    draw_knowledge(start_map, surface, knowledge_map)

    if -1 < agent.get_x() - start_map[0] < 16 and -1 < agent.get_y() - start_map[1] < 16:
        draw_agent(surface, agent.get_x() - start_map[0], agent.get_y() - start_map[1])
    if -1 < treasure.get_x() - start_map[0] < 16 and -1 < treasure.get_y() - start_map[1] < 16:
        draw_treasure(surface, treasure.get_x() - start_map[0], treasure.get_y() - start_map[1])
