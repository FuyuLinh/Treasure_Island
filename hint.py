import random
class Hint:
  def hint_01(width, height):
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

