import numpy as np
import datetime


class Move:
    def way(self, spis, x1, y1, x2, y2, move_distance):

        lab = np.arange(move_distance ** 2)
        lab = lab.reshape(move_distance, move_distance)
        if [y2, x2] in spis:
            return False
        if abs(x2 - x1) > ((move_distance - 1) // 2) or abs(y2 - y1) > ((move_distance - 1) // 2):
            return False
        else:
            for h in range(move_distance):
                for b in range(move_distance):
                    if [(y1 - ((move_distance - 1) // 2)) + h, (x1 - ((move_distance - 1) // 2)) + b] not in spis:
                        lab[h, b] = 0
                    elif [(y1 - ((move_distance - 1) // 2)) + h, (x1 - ((move_distance - 1) // 2)) + b] in spis:
                        lab[h, b] = -1
            x2 = x2 - x1 + ((move_distance - 1) // 2)
            y2 = y2 - y1 + ((move_distance - 1) // 2)
            x1 = ((move_distance - 1) // 2)
            y1 = ((move_distance - 1) // 2)
            lab = self.voln(x1, y1, 1, move_distance, move_distance, lab)
            if lab[y2][x2] > 0 and lab[y2][x2] <= ((move_distance + 1) // 2):
                return True

    def voln(self, x, y, cur, n, m, lab):
        lab[x][y] = cur
        if y + 1 < m:
            if lab[x][y + 1] == 0 or (lab[x][y + 1] != -1 and lab[x][y + 1] > cur):
                self.voln(x, y + 1, cur + 1, n, m, lab)
        if x + 1 < n:
            if lab[x + 1][y] == 0 or (lab[x + 1][y] != -1 and lab[x + 1][y] > cur):
                self.voln(x + 1, y, cur + 1, n, m, lab)
        if x - 1 >= 0:
            if lab[x - 1][y] == 0 or (lab[x - 1][y] != -1 and lab[x - 1][y] > cur):
                self.voln(x - 1, y, cur + 1, n, m, lab)
        if y - 1 >= 0:
            if lab[x][y - 1] == 0 or (lab[x][y - 1] != -1 and lab[x][y - 1] > cur):
                self.voln(x, y - 1, cur + 1, n, m, lab)
        return lab
