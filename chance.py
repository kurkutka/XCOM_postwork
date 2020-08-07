import random
import math


class Chance:
    def hit(self, y1, x1, y2, x2, spis, spec):
        bools_way = math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))
        math.floor(bools_way)
        bools_way = int(bools_way)
        defense = 0
        if y2 < y1 and (y2 + 1, x2) in spis:
            defense = 1
        elif x2 < x1 and (y2, x2 + 1) in spis:
            defense = 1
        elif x2 > x1 and (y2, x2 - 1) in spis:
            defense = 1
        elif y2 > y1 and (y2 - 1, x2) in spis:
            defense = 1
        else:
            defense = 0
        if spec == 1:
            chance_hit = 70 - (defense * 20) + (bools_way * 2) - random.randint(0, 10)
        else:
            chance_hit = 99 - (defense * 20) - (bools_way * 6) - random.randint(0, 10)
        return chance_hit
