import random
import math

# map có dạng mảng 2D int; 1: có kho báu, 0: không có kho báu
class Hint:

  # 1 đến 12 ô không có kho báu
  # width = row, height = col
  def hint_01(self, width, height):
    val_random = random.randint(1,12)
    maps = []
    count = 0

    for i in range(0, width):
      maps.append([1]*height)

    while True:
      val_row = random.randint(0,width - 1)
      val_col = random.randint(0, height - 1)
      if maps[val_row][val_col] != 0:
        count += 1
        maps[val_row][val_col] = 0
        if count == val_random:
          break
    return maps

  # 5 đến 20 ô chứa kho báu
  def hint_02(self, width, height):
    val_random = random.randint(5,20)
    maps = []
    count = 0

    for i in range(0, width):
      maps.append([0]*height)

    while True:
      val_row = random.randint(0,width - 1)
      val_col = random.randint(0, height - 1)
      if maps[val_row][val_col] != 1:
        count += 1
        maps[val_row][val_col] = 1
        if count == val_random:
          break
    return maps
    
  # 2 đến 5 vùng và 1 trong số chúng có kho báu
  def hint_03(self, number_areas, main_map, width, height):
    #random chọn số vùng và không tính biển trong đó
    while True:
      val_random = random.randint(2,5)
      if val_random < number_areas:
        break
    
    #chọn random các vùng trong map theo số lượng vùng đã được random ở trên
    number_areas_random = random.sample(range(1,number_areas - 1), val_random)

    #chuyển 2T -> 2, 4M -> 4,...
    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        temp = str(main_map[row][col]).rstrip('MPT')
        if int(temp) in number_areas_random:
          maps[row].append(1)
        else:
          maps[row].append(0)
    return maps
  
  # 1 đến 3 vùng và 1 trong số chúng không có kho báu
  def hint_04(self, number_areas, main_map, width, height):
    #random chọn số vùng và không tính biển trong đó
    while True:
      val_random = random.randint(1,3)
      if val_random < number_areas:
        break
    
    #chọn random các vùng trong map theo số lượng vùng đã được random ở trên
    # các vùng này không có kho báu
    number_areas_random = random.sample(range(1,number_areas - 1), val_random)

    #chuyển 2T -> 2, 4M -> 4,...
    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        temp = str(main_map[row][col]).rstrip('MPT')
        if int(temp) in number_areas_random:
          maps[row].append(0)
        else:
          maps[row].append(1)
    return maps

  # diện tích lớn hình chữ nhật có kho báu
  def hint_05(self, width, height):
    width_random = random.randint(round(float(width)/2),width)
    height_random = random.randint(round(float(height)/2),height)
    start_width_random = random.randint(0, width - width_random - 1)
    start_height_random = random.randint(0, height - height_random - 1)

    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        if col >= start_height_random and col < start_height_random + height_random and row >= start_width_random and row < start_width_random + width_random :
          maps[row].append(1)
        else:
          maps[row].append(0)
    return maps

  #diện tích nhỏ hình chữ nhật không có kho báu
  def hint_06(self, width, height):
    width_random = random.randint(1, round(((width - 1) / 2) - 0.1))
    height_random = random.randint(1, round(((height - 1) / 2) - 0.1))
    start_width_random = random.randint(0, width - width_random - 1 )
    start_height_random = random.randint(0, height - height_random - 1)

    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        if col >= start_height_random and col < start_height_random + height_random and row >= start_width_random and row <start_width_random + width_random:
          maps[row].append(0)
        else:
          maps[row].append(1)
    return maps

  # agent gần kho báu hơn
  # khi veryfi sẽ loại bỏ các vị trí đánh dấu là có kho báu mà gần pirate hơn agent, nếu hint đúng
  # = khoảng cách thì vẫn tính là gần pirate và xa agent
  def hint_07(self, agent_X, agent_Y, pirate_X, pirate_Y, treasure_X, treasure_Y, width, height):
    diagonal_agent = math.sqrt(abs(agent_X - treasure_X)**2 + abs(agent_Y - treasure_Y)**2)
    diagonal_pirate = math.sqrt(abs(pirate_X - treasure_X)**2 + abs(pirate_Y - treasure_Y)**2)

    maps = []
    for i in range(0, width):
      maps.append([])
      for j in range(0, height):
        location_to_agent = math.sqrt(abs(agent_X - i)**2 + abs(agent_Y - j)**2)
        location_to_pirate = math.sqrt(abs(pirate_X - i)**2 + abs(pirate_Y - j)**2)
        if location_to_agent >= location_to_pirate:
          maps[i].append(0)
        else:
          maps[i].append(1)
    return maps

  # hàng hoặc\và cột có chứa kho báu
  def hint_08(self, width, height):
    choose_random = random.randint(1,3)
    maps = []
    col_random = random.randint(0, height - 1)
    row_random = random.randint(0, width - 1)

    if choose_random == 1: # cột
      for i in range(0, width):
        maps.append([])
        for j in range(0, height):
          if j == col_random:
            maps[i].append(1)
          else:
            maps[i].append(0)
    elif choose_random == 2: # hàng
      for i in range(0,width):
        maps.append([])
        for j in range(0, height):
          if i == row_random:
            maps[i].append(1)
          else:
            maps[i].append(0)
    else: # hàng + cột
      for i in range(0,width):
        maps.append([])
        for j in range(0, height):
          if i == row_random or j == col_random:
            maps[i].append(1)
          else:
            maps[i].append(0)

    return maps

  # hàng hoặc\và cột không có chứa kho báu
  def hint_09(self, width, height):
    choose_random = random.randint(1,3)
    maps = []
    col_random = random.randint(0, height - 1)
    row_random = random.randint(0, width - 1)

    if choose_random == 1: # cột
      for i in range(0, width):
        maps.append([])
        for j in range(0, height):
          if j == col_random:
            maps[i].append(0)
          else:
            maps[i].append(1)
    elif choose_random == 2: # hàng
      for i in range(0,width):
        maps.append([])
        for j in range(0, height):
          if i == row_random:
            maps[i].append(0)
          else:
            maps[i].append(1)
    else: # hàng + cột
      for i in range(0,width):
        maps.append([])
        for j in range(0, height):
          if i == row_random or j == col_random:
            maps[i].append(0)
          else:
            maps[i].append(1)

    return maps

  # 2 vùng mà kho báu nằm đâu đó ở biên giới của chúng
  def hint_10(self, main_map, width, height):
    #chuyển 2T -> 2, 4M -> 4,...
    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        temp = str(main_map[row][col]).rstrip('MPT')
        maps[row].append(int(temp))

    # tìm ra biên giao nhau giữa các vùng và mỗi ô giao với vùng nào
    boundary_map = []
    adjacent_element_list = []
    for i in range(0, width):
      boundary_map.append([])
      adjacent_element_list.append([])
      for j in range(0, height):
        temp_list = []
        if i > 0 and maps[i][j] != maps[i - 1][j]:
          temp_list.append(maps[i - 1][j])
        if i < width - 1 and maps[i][j] != maps[i + 1][j]:
          temp_list.append(maps[i + 1][j])
        if j > 0 and maps[i][j] != maps[i][j - 1]:
          temp_list.append(maps[i][j - 1])
        if j < height - 1 and maps[i][j] != maps[i][j + 1]:
          temp_list.append(maps[i][j + 1])
        temp_list = list(set(temp_list))
        if len(temp_list) == 0:
          boundary_map[i].append(0)
        else:
          boundary_map[i].append(len(temp_list))
        adjacent_element_list[i].append(temp_list)
    
    # chọn biên giới giữa 2 vùng bất kỳ 
    while True:
      row_random = random.randint(0, width - 1)
      col_random = random.randint(0, height - 1)
      if boundary_map[row_random][col_random] != 0:
        break
    
    boundary_random_area1 = maps[row_random][col_random]
    boundary_random_area2 = random.choice(adjacent_element_list[row_random][col_random])

    result_map = []
    for row in range(0, width):
      result_map.append([])
      for col in range(0, height):
        if (maps[row][col] == boundary_random_area1 and boundary_random_area2 in adjacent_element_list[row][col]):
          result_map[row].append(1)
        elif (maps[row][col] == boundary_random_area2 and boundary_random_area1 in adjacent_element_list[row][col]):
          result_map[row].append(1)
        else:
          result_map[row].append(0)

    return result_map

  # kho báu nằm đâu đó ở biên giới của 2 vùng giao nhau
  def hint_11(self, main_map, width, height):
    #chuyển 2T -> 2, 4M -> 4,...
    maps = []
    for row in range(0, width):
      maps.append([])
      for col in range(0, height):
        temp = str(main_map[row][col]).rstrip('MPT')
        maps[row].append(int(temp))

    # tìm ra biên giao nhau giữa các vùng và mỗi ô giao với vùng nào
    boundary_map = []
    for i in range(0, width):
      boundary_map.append([])
      for j in range(0, height):
        if i > 0 and maps[i][j] != maps[i - 1][j]:
          boundary_map[i].append(1)
        elif i < width - 1 and maps[i][j] != maps[i + 1][j]:
          boundary_map[i].append(1)
        elif j > 0 and maps[i][j] != maps[i][j - 1]:
          boundary_map[i].append(1)
        elif j < height - 1 and maps[i][j] != maps[i][j + 1]:
          boundary_map[i].append(1)
        else:
          boundary_map[i].append(0)

    return boundary_map

  # kho báu ở đâu đó trong 1 - 3 ô tính từ biển
  def hint_12(self, main_map, width, height):
    random_tiles = random.randint(1,3)

    boundary_map = []
    for i in range(0, width):
      boundary_map.append([])
      for j in range(0, height):
        if i > 0 and main_map[i][j] != 0 and main_map[i - 1][j] == 0:
          boundary_map[i].append(1)
        elif i < width - 1 and main_map[i][j] != 0 and main_map[i + 1][j] == 0:
          boundary_map[i].append(1)
        elif j > 0 and main_map[i][j] != 0 and main_map[i][j - 1] == 0:
          boundary_map[i].append(1)
        elif j < height - 1 and main_map[i][j] != 0 and main_map[i][j + 1] == 0:
          boundary_map[i].append(1)
        else:
          boundary_map[i].append(0)
    
    if random_tiles == 2 or random_tiles == 3:
      for i in range(0, width):
        for j in range(0, height):
          if i > 1 and main_map[i][j] != 0 and main_map[i - 2][j] == 0:
            boundary_map[i][j] = 1
          elif i < width - 2 and main_map[i][j] != 0 and main_map[i + 2][j] == 0:
            boundary_map[i][j] = 1
          elif j > 1 and main_map[i][j] != 0 and main_map[i][j - 2] == 0:
            boundary_map[i][j] = 1
          elif j < height - 2 and main_map[i][j] != 0 and main_map[i][j + 2] == 0:
            boundary_map[i][j] = 1

    if random_tiles == 3:
      for i in range(0, width):
        for j in range(0, height):
          if i > 2 and main_map[i][j] != 0 and main_map[i - 3][j] == 0:
            boundary_map[i][j] = 1
          elif i < width - 3 and main_map[i][j] != 0 and main_map[i + 3][j] == 0:
            boundary_map[i][j] = 1
          elif j > 2 and main_map[i][j] != 0 and main_map[i][j - 3] == 0:
            boundary_map[i][j] = 1
          elif j < height - 3 and main_map[i][j] != 0 and main_map[i][j + 3] == 0:
            boundary_map[i][j] = 1
    return boundary_map
    
  # 1 nữa map có kho báu
  def hint_13(self, width, height):
    direction_random = random.randint(1,2)
    # 2 = vertical boundary
    # 1 = horizontal boundary
    side_random = random.randint(1,2)
    # 1 = left or top
    # 2 = right or bottom

    if direction_random == 1:
      if side_random == 1:
        maps = []
        for i in range(0, width):
          maps.append([])
          for j in range(0, height):
            if i < int(width / 2):
              maps[i].append(1)
            else:
              maps[i].append(0)
      if side_random == 2:
        maps = []
        for i in range(0, width):
          maps.append([])
          for j in range(0, height):
            if i > int((width - 1) / 2):
              maps[i].append(1)
            else:
              maps[i].append(0)
    else:
      if side_random == 1:
        maps = []
        for i in range(0, width):
          maps.append([])
          for j in range(0, height):
            if j < int(height  / 2):
              maps[i].append(1)
            else:
              maps[i].append(0)
      else:
        maps = []
        for i in range(0, width):
          maps.append([])
          for j in range(0, height):
            if j > int((height - 1)  / 2):
              maps[i].append(1)
            else:
              maps[i].append(0)
    return maps

  def hint_14(self, width, height, pirate_X, pirate_Y):
    # 1 = center of map
    # 2 = pirate location
    random_position = random.randint(1,2)
    
    random_direction = random.randint(1,8)
    # 1 = N
    # 2 = S
    # 3 = W
    # 4 = E
    # 5 = NW
    # 6 = NE
    # 7 = SW
    # 8 = SE

    direction_map = []
    for i in range(0, width):
      direction_map.append([0]*height)

    # khi xét từ trung tâm của map (center)
    if random_position == 1:
      for i in range(0, width):
        for j in range(0, height):
          if random_direction == 1:
            if i < width / 2 and j >= i and j <= width - 1 - i:
              direction_map[i][j] = 1
          if random_direction == 2:
            if i >= width / 2 and j <= i and j >= width - 1 - i:
              direction_map[i][j] = 1
          if random_direction == 3:
            if (i < width and j <= i) or (i >= width and j <= width - 1 - i):
              direction_map[i][j] = 1
          if random_direction == 4:
            if (i < width and j >= width - 1 - i) or (i >= width and j >= i):
              direction_map[i][j] = 1
          if random_direction == 5:
            if i < width / 2 and j < height / 2:
              direction_map[i][j] = 1
          if random_direction == 6:
            if i < width / 2 and j >= height / 2:
              direction_map[i][j] = 1
          if random_direction == 7:
            if i >= width / 2 and j < height / 2:
              direction_map[i][j] = 1
          if random_direction == 8:
            if i >= width / 2 and j >= height / 2:
              direction_map[i][j] = 1
    else: # khi xét từ vị trí của pirate
      for i in range(0, width):
        for j in range(0, height):
          if random_direction == 5:
            if i <= pirate_X and j <= pirate_Y:
              direction_map[i][j] = 1
          if random_direction == 6:
            if i <= pirate_X and j >= pirate_Y:
              direction_map[i][j] = 1
          if random_direction == 7:
            if i >= pirate_X and j <= pirate_Y:
              direction_map[i][j] = 1
          if random_direction == 8:
            if i >= pirate_X and j >= pirate_Y:
              direction_map[i][j] = 1
    return direction_map

  def hint_15(self, width, height):
    start_big_X = random.randint(0, width - 1)
    end_big_X = random.randint(start_big_X, width - 1)
    start_big_Y = random.randint(0, height - 1)
    end_big_Y = random.randint(start_big_Y, height - 1)

    start_small_X = random.randint(start_big_X, end_big_X)
    end_small_X = random.randint(start_small_X, end_big_X)
    start_small_Y = random.randint(start_big_Y, end_big_Y)
    end_small_Y = random.randint(start_small_Y, end_big_Y)

    maps = []
    for i in range(0, width):
      maps.append([])
      for j in range(0, height):
        if i < start_small_X:
          if i >= start_big_X and j >= start_big_Y and j <= end_big_Y:
            maps[i].append(1)
          else:
            maps[i].append(0)
        if i >= start_small_X and i < end_small_X:
          if (j >= start_big_Y and j < start_small_Y) or (j > end_small_Y and j <= end_big_Y):
            maps[i].append(1)
          else:
            maps[i].append(0)
        if i >= end_small_X:
          if i <= end_big_X and j >= start_big_Y and j <= end_big_Y:
            maps[i].append(1)
          else:
            maps[i].append(0)
    return maps

  def hint_16(self, main_maps, width, height):
    maps = []
    
    for i in range(0, width):
      maps.append([])
      for j in range(0, height):
        if 'M' in str(main_maps[i][j]):
          maps[i].append(1)
        else:
          maps[i].append(0)
    return maps

    







