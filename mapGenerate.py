import csv
import math
import sys

import numpy as numpy


def print_map(map):
    for row in map:
        for item in row:
            if item != -1:
                print(item, end=' ')
            else:
                print(" ", end=' ')
        print('')


def counting(map, width, height, region):
    count = 0
    for x in range(height):
        for y in range(width):
            if map[x][y] == region:
                count += 1
    return count


def generate(index, width, height, turn_reveal, turn_free, region, treasure_x, treasure_y, map):
    path = f'data/Map{index}.txt'
    size = str(width) + ' ' + str(height)
    f = open(path, "w")
    f.write(size + "\n")
    f.write(str(turn_reveal) + '\n')
    f.write(str(turn_free) + '\n')
    f.write(str(region) + '\n')
    f.write(str(treasure_x) + ' ' + str(treasure_y) + '\n')
    for x in range(height):
        row = str(map[x][0])
        for y in range(1,width):
            row += '; ' + str(map[x][y])
        f.write(row + '\n')
    f.close()


def create_sea(map, width, height, area, space):
    while area > 0:
        choice = numpy.random.randint(0, 4)
        if choice == 0:
            for y in range(space, width - space, 1):
                if area > 0:
                    prob = numpy.random.randint(1, 10)
                    i = 0
                    while i < 3 and map[i][y] == 0:
                        i = i + 1
                    if map[i][y] != 0 and prob > 5:
                        map[i][y] = 0
                        area -= 1
                        if y == space:
                            for k in range(i + 1):
                                for m in range(space):
                                    if area > 0:
                                        if map[k][m] != 0:
                                            map[k][m] = 0
                                            area -= 1
                                    else:
                                        break
                        if y == width - space - 1:
                            for k in range(i + 1):
                                for m in range(width - space, width, 1):
                                    if area > 0:
                                        if map[k][m] != 0:
                                            map[k][m] = 0
                                            area -= 1
                                    else:
                                        break

        elif choice == 1:
            for y in range(space, width - space, 1):
                if area > 0:
                    prob = numpy.random.randint(1, 10)
                    i = height - 1
                    while i > height - 4 and map[i][y] == 0:
                        i = i - 1
                    if map[i][y] != 0 and prob > 5:
                        map[i][y] = 0
                        area -= 1
                        if y == space:
                            for k in range(i, height, 1):
                                for m in range(space):
                                    if area > 0:
                                        if map[k][m] != 0:
                                            map[k][m] = 0
                                            area -= 1
                                    else:
                                        break
                        if y == width - space - 1:
                            for k in range(i, height, 1):
                                for m in range(width - space, width, 1):
                                    if area > 0:
                                        if map[k][m] != 0:
                                            map[k][m] = 0
                                            area -= 1
                                    else:
                                        break
        elif choice == 2:
            for x in range(space, height - space, 1):
                if area > 0:
                    prob = numpy.random.randint(1, 10)
                    i = width - 1
                    while i > width - 4 and map[x][i] == 0:
                        i = i - 1
                    if map[x][i] != 0 and prob > 5:
                        map[x][i] = 0
                        area -= 1
                        if x == space:
                            for k in range(i, width, 1):
                                for m in range(space):
                                    if area > 0:
                                        if map[m][k] != 0:
                                            map[m][k] = 0
                                            area -= 1
                                    else:
                                        break
                        if x == height - space - 1:
                            for k in range(i, width, 1):
                                for m in range(height - space, height, 1):
                                    if area > 0:
                                        if map[m][k] != 0:
                                            map[m][k] = 0
                                            area -= 1
                                    else:
                                        break
        else:
            for x in range(space, height - space, 1):
                if area > 0:
                    prob = numpy.random.randint(1, 10)
                    i = 0
                    while i < 3 and map[x][i] == 0:
                        i = i + 1
                    if map[x][i] != 0 and prob > 5:
                        map[x][i] = 0
                        area -= 1
                        if x == space:
                            for k in range(i + 1):
                                for m in range(space):
                                    if area > 0:
                                        if map[m][k] != 0:
                                            map[m][k] = 0
                                            area -= 1
                                    else:
                                        break
                        if x == height - space - 1:
                            for k in range(i + 1):
                                for m in range(height - space, height, 1):
                                    if area > 0:
                                        if map[m][k] != 0:
                                            map[m][k] = 0
                                            area -= 1
                                    else:
                                        break


def fill_region(map, width, height, area, region, start_x, start_y, direction):
    if area == 0:
        return
    if direction == 1:
        # print("type 1")
        for r in range(width - start_y):
            for x in range(start_x + r):
                if x < height and area > 0 and map[x][start_y + r] == -1:
                    map[x][start_y + r] = region
                    area -= 1
                if area == 0:
                    return start_x, start_y + r, direction
            if area >= r and start_x + r < height:
                for y in range(r + 1):
                    if map[start_x + r][start_y + y] == -1:
                        map[start_x + r][start_y + y] = region
                        area -= 1
                    if area == 0:
                        return start_x, start_y + r, direction
        x = 0
        while start_x + x < height and map[start_x + x][start_y - 1] != -1:
            for y in range(width - start_y):
                if map[start_x + x][start_y + y] == -1:
                    if area > 0:
                        map[start_x + x][start_y + y] = region
                        area -= 1
                    else:
                        return start_x + x, start_y + y, direction
            x += 1
        fill_region(map, width, height, area, region, start_x + x, width - 1, 0)
        return start_x + x, width - 1, 0
    if direction == 0:
        # print("type 0")
        for r in range(start_y + 1):
            for x in range(start_x + r):
                if x < height and area > 0 and map[x][start_y - r] == -1:
                    map[x][start_y - r] = region
                    area -= 1
                if area == 0:
                    return start_x, start_y - r, direction
            if area >= r and start_x + r < height:
                for y in range(r + 1):
                    if map[start_x + r][start_y - y] == -1:
                        map[start_x + r][start_y - y] = region
                        area -= 1
                    if area == 0:
                        return start_x, start_y - r, direction
        x = 0
        while start_x + x < height and map[start_x + x][start_y + 1] != -1:
            for y in range(start_y + 1):
                if map[start_x + x][start_y - y] == -1:
                    if area > 0:
                        map[start_x + x][start_y - y] = region
                        area -= 1
                    else:
                        return start_x + x, start_y - y, direction
            x += 1
        fill_region(map, width, height, area, region, start_x + x, 0, 1)
        return start_x + x, 0, 1


def track_separated_area(map, width, height, space):
    for y in range(space - 1, -1, -1):
        for x in range(height - 1, -1, -1):
            if map[x][y] != 0 and map[x][y] != map[x][y + 1]:
                if x == height - 1 or map[x][y] != map[x + 1][y]:
                    map[x][y] = map[x][y + 1]
    for y in range(width - space - 1, width, 1):
        for x in range(height - 1, -1, -1):
            if map[x][y] != 0 and map[x][y] != map[x][y - 1]:
                if map[x][y - 1] != 0 and (x == height - 1 or map[x][y] != map[x + 1][y]):
                    map[x][y] = map[x][y - 1]
    for x in range(height - space - 1, height, 1):
        for y in range(width - 1, -1, -1):
            if y == width - 1 or y == 0:
                if map[x][y] != 0:
                    map[x][y] = map[x - 1][y]
            elif map[x][y] != 0 and map[x - 1][y] != 0:
                if map[x][y] != map[x - 1][y] and (map[x - 1][y] == map[x][y + 1] or map[x][y + 1] == 0):
                    map[x][y] = map[x - 1][y]


def create_map(width, height, region):
    # TODO: init the map with  value -1
    if width < 6 and height < 6:
        space = 1
    else:
        space = 3
    map = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append(-1)
        map.append(row)
    # TODO: setup calculate number of regions and area of them
    regions = []
    # --- sea area ---
    if width * height >= 16 * 16:
        sea_area = numpy.random.randint(3.5 * math.sqrt(width * height), ((width * height) ** (3 / 4)))
    else:
        sea_area = int(0.25 * width * height)
    remain_area = width * height - sea_area
    regions.append(sea_area)
    # --- islands area ---
    for i in range(region - 2):
        area = int(remain_area / (region - 1 - i)) + numpy.random.randint(-1, 1)
        remain_area -= area
        regions.append(area)
    regions.append(remain_area)

    # TODO: fill map with region number
    create_sea(map, width, height, regions[0], space)
    x = y = 0
    direction = 1
    list = [i for i in range(1, region)]

    for i in range(region - 1):
        reg = numpy.random.choice(list)
        list.remove(reg)
        x, y, direction = fill_region(map, width, height, regions[reg], reg, x, y, direction)

    # printMap(map)
    # print("-------")
    # TODO: make sure every area same region is adjacent
    if width * height >= 16 * 16:
        track_separated_area(map, width, height, space)
    return map


def add_mountain_and_prison(map, width, height, treasure_x, treasure_y, prison):
    temp = 0
    for mountain in range(int((width * height) ** (1 / 4)) + 1):
        lenght = numpy.random.randint(1, width * 0.5)
        mountainY = numpy.random.randint(3, width - 3)
        mountainX = numpy.random.randint(3, height - 3)
        for i in range(lenght):
            if map[mountainX][mountainY] == 0:
                temp += 0
            elif "M" in str(map[mountainX][mountainY]):
                temp += 0
            elif mountainX and treasure_x and mountainY == treasure_y:
                temp += 0
            else:
                map[mountainX][mountainY] = str(map[mountainX][mountainY]) + 'M'
            mountainY += numpy.random.choice([-1, 0, 1], p=[0.4, 0.2, 0.4])
            mountainX += numpy.random.choice([-1, 0, 1], p=[0.4, 0.2, 0.4])
            if mountainY > width - 1 or mountainY < 0 or mountainX > height - 1 or mountainY < 0:
                break

    prisons = [0, map[treasure_x][treasure_y]]
    i = 0
    loop = 0
    while i < prison + 1 and loop < 10000:
        prisonX = numpy.random.randint(2, height - 2)
        prisonY = numpy.random.randint(2, width - 2)
        if ("P" not in str(map[prisonX][prisonY])) and ("M" not in str(map[prisonX][prisonY])) and map[prisonX][
            prisonY] not in prisons:
            if abs(prisonX - treasure_x) > height ** 0.5 or abs(prisonY - treasure_y) > width ** 0.5:
                prisons.append(map[prisonX][prisonY])
                map[prisonX][prisonY] = str(map[prisonX][prisonY]) + "P"
                i += 1
        loop += 1


def main(width, height):
    f = open("data/init.txt", "r")
    index = int(f.read())
    f.close()
    width = int(width)
    height = int(height)
    region = int((width * height) ** (1 / 4)) + 3
    map = create_map(width, height, region)
    treasureX = numpy.random.randint(0.25 * height, 0.75 * height)
    treasureY = numpy.random.randint(0.25 * width, 0.75 * height)
    while map[treasureX][treasureY] == 0:
        treasureX = numpy.random.randint(0.25 * height, 0.75 * height)
        treasureY = numpy.random.randint(0.25 * width, 0.75 * height)
    prison = int(region - 3)
    add_mountain_and_prison(map, width, height, treasureX, treasureY, prison)
    # map[treasureX][treasureY] = str(map[treasureX][treasureY]) + "T"
    turn_reveal = numpy.random.randint(2, 4)
    turn_free = int((width * height) / 50)
    if (turn_free <= turn_reveal):
        turn_free = turn_reveal + 1
    # print_map(map)
    generate(index, width, height, turn_reveal, turn_free, region, treasureX, treasureY, map)
    f = open("data/init.txt", "w")
    f.write(str(index + 1))
    f.close()
    del map


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(0)
    if int(sys.argv[1]) < 8 or int(sys.argv[2]) < 8:
        print("please input width and height more than 8")
        sys.exit(0)
    main(sys.argv[1], sys.argv[2])
