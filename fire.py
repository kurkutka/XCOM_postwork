import math
import pygame


class Fire:
    def fire(self, y1, x1, y2, x2, sprt, spis, dist, scr):
        bools_way = math.sqrt((abs(x1 * 32 - x2 * 32) ** 2) + (abs(y1 * 32 - y2 * 32) ** 2))
        math.floor(bools_way)
        bools_way = int(bools_way)
        if bools_way <= dist * 32:
            y1 = y1 * 32 + 16
            x1 = x1 * 32 + 16
            y2 = y2 * 32 + 16
            x2 = x2 * 32 + 16
            if y2 - y1 != 0 or x2 - x1 != 0:
                grad = math.acos((y2 - y1) / bools_way)
                grad = math.degrees(grad)
            elif y2 - y1 == 0:
                grad = 0
            elif x2 - x1 == 0:
                grad = 270
            scr.blit(sprt, (x1, y1))
            sprt1 = pygame.transform.scale(sprt, (1, bools_way * 2))
            scr.blit(sprt1, (x1, y1))
            if x2 > x1 and y2 < y1:
                grad = 270 + grad - 90
            elif x2 < x1 and y2 > y1:
                grad = 90 - grad + 90
            elif x2 > x1 and y2 > y1:
                grad = 180 + grad
            elif x2 < x1 and y2 < y1:
                grad = 180 - grad
            sprt1 = pygame.transform.rotate(sprt1, grad)
            sprt2 = pygame.sprite.Sprite()
            sprt2.image = sprt1
            sprt2.rect = sprt2.image.get_rect()
            xx = [x1 - (sprt2.rect[2] // 2), y1 - (sprt2.rect[3] // 2)]
            scr.blit(sprt1, (x1 - (sprt2.rect[2] // 2), y1 - (sprt2.rect[3] // 2)))
            sprt2.rect.x = x1 - (sprt2.rect[2] // 2)
            sprt2.rect.y = y1 - (sprt2.rect[3] // 2)
            sprt2.mask = pygame.mask.from_surface(sprt2.image)
            flag = 0
            s = []
            x1 -= 16
            x2 -= 16
            y2 -= 16
            y1 -= 16
            s_kill = []
            for elem in spis:
                x = elem.rect.x
                y = elem.rect.y
                if x1 > x2 and y1 > y2:
                    if x <= x1 and x >= x2 and y <= y1 and y >= y2:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 < x2 and y1 > y2:
                    if x <= x2 and x >= x1 and y <= y1 and y >= y2:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 < x2 and y1 < y2:
                    if x <= x2 and x >= x1 and y <= y2 and y >= y1:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 > x2 and y1 < y2:
                    if x <= x1 and x >= x2 and y <= y2 and y >= y1:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 > x2 and y1 == y2:
                    if x <= x1 and x >= x2 and y == y2:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 < x2 and y1 == y2:
                    if x <= x2 and x >= x1 and y == y2:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 == x2 and y1 < y2:
                    if x == x1 and y <= y2 and y >= y1:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
                elif x1 == x2 and y1 > y2:
                    if x == x2 and y <= y1 and y >= y2:
                        if pygame.sprite.collide_mask(sprt2, elem):
                            flag = 1
                            s.append([x, y])
                            s_kill.append(elem)
            ss = [s, s_kill, sprt1, h]
            if flag == 1:
                return ss
            else:
                return False
        else:
            return [1, 1]
