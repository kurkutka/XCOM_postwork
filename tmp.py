import pygame
from pytmx.util_pygame import load_pygame
import os

pygame.init()
size = width, height = 1200, 960
screen = pygame.display.set_mode(size)
running = True
global s, flag, choice_hero, hero, choice_alien
s = [[21, 4], [21, 5], [21, 6], [21, 7], [21, 8], [21, 9], [21, 10], [21, 10], [21, 11], [21, 12], [21, 13], [21, 15],
     [21, 16], [21, 17], [21, 18], [21, 19], [21, 20], [21, 21], [21, 22], [21, 24], [21, 25], [21, 25], [21, 26],
     [20, 26], [19, 26], [18, 26], [17, 26], [16, 26], [15, 26], [14, 26], [13, 26], [12, 26], [11, 26], [11, 25],
     [11, 24], [11, 23], [11, 22], [11, 21], [11, 20], [11, 19], [11, 18], [11, 17], [11, 16], [11, 15], [11, 14],
     [11, 13], [11, 12], [11, 11], [11, 10], [11, 9], [11, 8], [11, 7], [11, 6], [11, 5], [11, 4], [12, 4], [13, 4],
     [14, 4], [15, 4], [16, 4], [17, 4], [18, 4], [19, 4], [20, 4], [21, 4], [12, 8], [13, 8], [14, 8], [15, 8],
     [17, 8], [18, 8], [19, 8], [20, 8], [12, 12], [13, 12], [14, 12], [15, 12], [17, 12], [18, 12], [19, 12],
     [20, 12], [12, 16], [13, 16], [14, 16], [15, 16], [15, 18], [15, 19], [16, 19], [17, 19], [18, 19], [19, 19],
     [20, 19], [6, 6], [6, 7], [8, 6], [8, 7], [4, 6], [4, 7], [4, 3], [4, 4], [6, 3], [6, 4], [8, 3], [8, 4],
     [7, 19], [6, 19], [5, 19], [4, 19], [3, 19], [2, 19], [1, 19], [0, 19], [0, 20], [0, 21], [0, 22], [0, 23],
     [0, 24], [0, 25], [0, 26], [0, 27], [0, 28], [0, 29], [1, 29], [2, 29], [3, 29], [4, 29], [5, 29], [6, 29],
     [7, 29], [7, 28], [7, 27], [7, 26], [7, 25], [7, 24], [7, 23], [7, 22], [7, 21]]
flag = [2000, 2000]
choice_hero = [26, 11]
choice_alien = [[2, 12], [3, 13], [2, 14], [14, 21], [14, 23]]
hero = 0

tmxdata = load_pygame("data/map4.tmx")


class XCOM:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.cell_size = 32

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for x in range(30):
            for y in range(30):
                for elem in choice_alien:
                    screen.blit(self.load_image('sectoid.png'), (elem[1] * 32, elem[0] * 32))
                if hero == 1:
                    screen.blit(self.load_image('menut.png'), (960, 0))
                    screen.blit(self.load_image('Heavy_support.png'), (choice_hero[1] * 32, choice_hero[0] * 32))
                else:
                    screen.blit(self.load_image('Heavy_support.png'), (choice_hero[1] * 32, choice_hero[0] * 32))
                screen.blit((tmxdata.get_tile_image(x, y, 0)), (x * 32, y * 32))

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.width * self.cell_size and\
                mouse_pos[1] < self.height * self.cell_size:
            x = (mouse_pos[0]) // self.cell_size
            y = (mouse_pos[1]) // self.cell_size
            return y, x
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def on_click(self, cell):
        if cell != None:
            choice_alien.append([cell[0], cell[1]])
            print(choice_alien)

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data/Текстуры', name)
        image = pygame.image.load(fullname)
        return image


board = XCOM(30, 30)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                board.get_click(event.pos)
                s1 = [board.get_cell(event.pos)[0], board.get_cell(event.pos)[1]]
                if s1 in s:
                    flag = s1
                if s1 == choice_hero:
                    if s1 not in s:
                        hero = 1
                        choice_hero = s1
                if s1 != choice_hero and hero == 1:
                    if s1 not in s:
                        choice_hero = s1
                        hero = 0
                        flag[0] = flag[0] + 1000
    screen.fill((0, 0, 0))
    board.render()
    clock.tick(10)
    pygame.display.flip()