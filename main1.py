import pygame
import os
import random
import datetime
import pygame
from pytmx.util_pygame import load_pygame
import math
from move import Move
from fire import Fire
from chance import Chance


class Cat(pygame.sprite.Sprite):
    def __init__(self, avatars, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.alex = pygame.sprite.Group()
        self.alex.add(avatars[0])
        self.kirill = pygame.sprite.Group()
        self.kirill.add(avatars[1])
        self.ilya = pygame.sprite.Group()
        self.ilya.add(avatars[2])
        self.x = 0
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        global running
        self.x += 1
        text = pygame.font.SysFont('comicsansms', 72).render('"KupiTeam" Presents', True, pygame.Color('white'))
        screen.blit(text, (250, 750))
        if self.x >= 10:
            self.alex.draw(screen)
            text = pygame.font.SysFont(None, 40).render('Александр Буренчев', True, pygame.Color('green'))
            screen.blit(text, (20, 415))
        if self.x >= 25:
            self.kirill.draw(screen)
            text = pygame.font.SysFont(None, 40).render('Кирилл Золотарев', True, pygame.Color('red'))
            screen.blit(text, (400, 415))
        if self.x >= 40:
            self.ilya.draw(screen)
            text = pygame.font.SysFont(None, 40).render('Илья Борисов', True, pygame.Color('purple'))
            screen.blit(text, (780, 415))
        if self.x >= 80:
            running = False
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.x += 20


pygame.init()
pygame.display.set_caption("XCOM")
FPS = 5
all_sprites = pygame.sprite.Group()
alex = pygame.sprite.Sprite()
kirill = pygame.sprite.Sprite()
ilya = pygame.sprite.Sprite()
todd = pygame.sprite.Sprite()
clock = pygame.time.Clock()
size = width, height = 1200, 960
screen = pygame.display.set_mode(size)
running = True
screen.fill((0, 0, 0))
image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/cat.png')), (300, 300))
alex.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/alex.jpg')), (400, 415))
kirill.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/kirill.png')), (400, 415))
todd.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/todd.jpg')), (1200, 400))
ilya.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/ilya.jpg')), (400, 415))
alex.rect = alex.image.get_rect()
ilya.rect = ilya.image.get_rect()
todd.rect = todd.image.get_rect()
kirill.rect = kirill.image.get_rect()
alex.rect.x = 20
alex.rect.y = kirill.rect.y = ilya.rect.y = todd.rect.x = 0
kirill.rect.x = 400
ilya.rect.x = 780
todd.rect.y = 600
all_sprites.add(todd)
Cat((alex, kirill, ilya), image, 1, 2, -150, 455)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)


class Text:
    def update(self):
        screen.blit(text, (520, 0))
        screen.blit(text1, (0, 920))


text = pygame.font.SysFont(None, 72).render('XCOM', True, pygame.Color('black'))
text1 = pygame.font.SysFont(None, 50).render('click to continue', True, pygame.Color('black'))
bg = pygame.sprite.Sprite()
bg.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/background.jpg')), (1200, 960))
bg.rect = bg.image.get_rect()
bg.rect.x = 0
bg.rect.y = 0
all_sprites.add(bg)
screen.fill((0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            running = False
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    Text.update(Text())
    pygame.display.flip()
    clock.tick(FPS)


class Map:
    def update(self):
        screen.blit(time, (280, 0))


class Text:
    def introduction(self):
        if flag_text:
            screen.blit(text1, (500, 200))
            screen.blit(text2, (220, 250))
            screen.blit(text3, (190, 300))
            screen.blit(text4, (320, 350))
            screen.blit(text5, (270, 400))
            screen.blit(text6, (200, 450))
            screen.blit(text7, (220, 500))
            screen.blit(text8, (180, 550))
            screen.blit(text9, (250, 600))
            screen.blit(text10, (290, 650))
            screen.blit(text11, (220, 700))
            screen.blit(text12, (250, 750))
            screen.blit(text13, (260, 800))
        else:
            screen.blit(no_text, (0, 0))

    def panic(self):

        # Северная Америка
        if panic[0] == 0:
            screen.blit(panic1, (40, 230))
        elif panic[0] == 1:
            screen.blit(panic2, (40, 230))
        else:
            screen.blit(panic3, (40, 230))

        # Южная Америка
        if panic[1] == 0:
            screen.blit(panic1, (210, 650))
        elif panic[1] == 1:
            screen.blit(panic2, (210, 650))
        else:
            screen.blit(panic3, (210, 650))

        # Евразия
        if panic[2] == 0:
            screen.blit(panic1, (700, 200))
        elif panic[2] == 1:
            screen.blit(panic2, (700, 200))
        else:
            screen.blit(panic3, (700, 200))

        # Африка
        if panic[3] == 0:
            screen.blit(panic1, (580, 550))
        elif panic[3] == 1:
            screen.blit(panic2, (580, 550))
        else:
            screen.blit(panic3, (580, 550))

        # Австралия
        if panic[4] == 0:
            screen.blit(panic1, (1000, 810))
        elif panic[4] == 1:
            screen.blit(panic2, (1000, 810))
        else:
            screen.blit(panic3, (1000, 810))


map = pygame.sprite.Group()
bg.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/map.jpg')), (1200, 960))
bg.rect = bg.image.get_rect()
bg.rect.x = bg.rect.y = 0
map.add(bg)

flag_text = True

text = ['Поздравляю!', 'Вас повысили! Теперь вы командующий', 'опергруппы. В данный момент идет первая',
        'галактическая война на Марсе', 'на базе пришельцев. Но на Землю', 'продолжают нападать маленькие отряды',
        'партизан. Ваша задача уничтожить эти', 'отряды и восстановить порядок на Земле.',
        'Они напали на наш генератор и наша', 'система питания была повреждена.', 'Энергии хватило на вывод карты мира',
        'в ужасном качестве. Это всё, что мы ', 'можем сделать. Удачи, командир!']

text1 = pygame.font.SysFont(None, 60).render(text[0], True, (100, 255, 100), pygame.Color('black'))
text2 = pygame.font.SysFont(None, 60).render(text[1], True, (100, 255, 100), pygame.Color('black'))
text3 = pygame.font.SysFont(None, 60).render(text[2], True, (100, 255, 100), pygame.Color('black'))
text4 = pygame.font.SysFont(None, 60).render(text[3], True, (100, 255, 100), pygame.Color('black'))
text5 = pygame.font.SysFont(None, 60).render(text[4], True, (100, 255, 100), pygame.Color('black'))
text6 = pygame.font.SysFont(None, 60).render(text[5], True, (100, 255, 100), pygame.Color('black'))
text7 = pygame.font.SysFont(None, 60).render(text[6], True, (100, 255, 100), pygame.Color('black'))
text8 = pygame.font.SysFont(None, 60).render(text[7], True, (100, 255, 100), pygame.Color('black'))
text9 = pygame.font.SysFont(None, 60).render(text[8], True, (100, 255, 100), pygame.Color('black'))
text10 = pygame.font.SysFont(None, 60).render(text[9], True, (100, 255, 100), pygame.Color('black'))
text11 = pygame.font.SysFont(None, 60).render(text[10], True, (100, 255, 100), pygame.Color('black'))
text12 = pygame.font.SysFont(None, 60).render(text[11], True, (100, 255, 100), pygame.Color('black'))
text13 = pygame.font.SysFont(None, 60).render(text[12], True, (100, 255, 100), pygame.Color('black'))
no_text = pygame.font.SysFont(None, 72).render('', True, pygame.Color('black'))

# Вся паника
panic_text = ['Уровень паники: 0', 'Уровень паники: 1', 'Уровень паники: 2']
panic = [0, 0, 0, 0, 0]
panic1 = pygame.font.SysFont(None, 30).render(panic_text[0], True, (0, 0, 0))
panic2 = pygame.font.SysFont(None, 30).render(panic_text[1], True, (0, 0, 0))
panic3 = pygame.font.SysFont(None, 30).render(panic_text[2], True, (0, 0, 0))

screen.fill((0, 0, 0))


def load_image(name):
    fullname = os.path.join('data/Текстуры', name)
    image = pygame.image.load(fullname)
    return image

FPS = 5
running = True
coord_missions = [[200, 250], [210, 500], [600, 200], [600, 450], [1100, 730]]
x = [0, 0]
in_game = True
stop = False
time_rn = datetime.datetime.now()
check = 0
tm = 13
colm = 0
btn = load_image('btn.png')
defeat = load_image('defeat.png')
win = load_image('win.png')
click_coord = [0, 0]
pygame.mixer.music.load('data/sounds/Menu.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()
while running:
    pn = 0
    for elem in panic:
        pn += elem
    if pn == 10:
        screen.blit(defeat, (0, 0))
    if colm == 7:
        screen.blit(win, (0, 0))
    for e in panic:
        if e == 2:
            del coord_missions[panic.index(e)]
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and stop:
            for elem in coord_missions:
                if elem[0] <= event.pos[0] and event.pos[0] <= elem[0] + 64 and elem[1] <= event.pos[1] and event.pos[1] <= elem[1] + 64:
                    click_coord = elem
        elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            flag_text = False
        elif event.type == pygame.QUIT:
            running = False
    if in_game:
        if tm % 14 == 0:
            in_game = False
            stop = True
            colm += 1
        check += 1
        if check == 50:
            check = 0
            tm += 1
            time_rn += datetime.timedelta(days=1)
        if check == 1200:
            pygame.mixer.music.load('data/sounds/Menu.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
        time = pygame.font.SysFont(None, 72).render(str(time_rn).split()[0].replace('-', '.'),
                                                    True, pygame.Color('black'))
        screen.fill(pygame.Color('black'))
        Text.panic(Text())
        map.draw(screen)
        Map.update(Map())
        Text.panic(Text())
        Text.introduction(Text())
        pygame.display.flip()
        clock.tick(FPS)
        x = [[0, 0], [0, 0]]
        while x[0] == x[1]:
            x = random.choices(coord_missions, k=2)
    elif stop:
        for el in x:
            screen.blit(btn, (el[0], el[1]))
        in_game = False
        Text.panic(Text())
        Map.update(Map())
        Text.panic(Text())
        Text.introduction(Text())
        pygame.display.flip()
        clock.tick(FPS)
        if click_coord != [0, 0]:
            for el in x:
                if el != click_coord:
                    if panic[coord_missions.index(el)] != 2:
                        panic[coord_missions.index(el)] += 1
            stop = False
    else:
        pygame.init()
        size = width, height = 1200, 960
        screen = pygame.display.set_mode(size)
        running = True
        global s, flag, choice_hs, hero, error_tail, way, flag_turn, flag_turn1, \
            flag_turn2, flag_turn3, turn_enemy, choice_alien, destr, health_hero, health_alien, fire, hit, tmp, mrh, \
            flag_choice_alien, type_alien, choice_hs, dead, flag_ab, g1, flag_ab1, col_ab, fj
        mp = random.randint(1, 5)
        if mp == 1:
            pygame.mixer.music.load('data/sounds/mission1.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            tmxdata = load_pygame("data/map1.1.tmx")
            s = [[2, 4], [2, 3], [3, 3], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2],
                 [12, 2],
                 [13, 2], [14, 2], [15, 2], [16, 2], [16, 3], [16, 5], [16, 6], [15, 6], [14, 6], [13, 6], [12, 6],
                 [11, 6],
                 [10, 6], [8, 6], [9, 6], [7, 6], [6, 6], [5, 6], [4, 6], [3, 6], [2, 5], [3, 5], [9, 9], [9, 10],
                 [9, 11],
                 [18, 14], [18, 15], [18, 16], [15, 12], [14, 12], [13, 12], [13, 11], [13, 10], [14, 10], [15, 10],
                 [14, 19],
                 [15, 19], [16, 19], [17, 19], [18, 19], [18, 20], [18, 21], [18, 22], [18, 23], [18, 24], [18, 25],
                 [17, 25], [16, 25], [15, 25], [14, 25], [14, 24], [14, 23], [14, 21], [14, 20], [7, 26],
                 [6, 26], [6, 27], [5, 27], [4, 27], [4, 26], [3, 26], [3, 25], [3, 24], [3, 23], [3, 22], [3, 21],
                 [3, 20],
                 [3, 19], [3, 18], [3, 17], [3, 16], [3, 15], [4, 15], [4, 14], [5, 14], [6, 14], [6, 15], [7, 15],
                 [7, 16],
                 [7, 17], [7, 19], [7, 20], [7, 21], [7, 22], [7, 23], [7, 24], [7, 25], [18, 15],
                 [24, 19], [25, 19], [25, 18], [24, 18], [22, 7], [23, 7], [23, 6], [22, 6]]
            health_alien = [5, 5, 5, 5, 5, 5, 5, 5, 5]
            type_alien = ['sectoid', 'sectoid', 'sectoid', 'sectoid', 'sectoid',
                          'sectoid', 'sectoid', 'sectoid', 'sectoid']
            choice_alien = [[3, 4], [4, 3], [4, 5], [5, 9], [5, 11],
                            [5, 17], [5, 19], [16, 21], [16, 23]]  # список клятых алиенов (сектоидов)
        elif mp == 2:
            pygame.mixer.music.load('data/sounds/mission3.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            tmxdata = load_pygame("data/map2_krissalids_nights.tmx")
            s = [[24, 10], [24, 11], [24, 12], [24, 13], [25, 18], [25, 19], [25, 20], [25, 21], [17, 10], [17, 9],
                 [16, 9],
                 [15, 9], [14, 9], [13, 9], [12, 9], [11, 9], [10, 9], [9, 9], [8, 9], [7, 9], [6, 9], [6, 8], [6, 7],
                 [6, 6], [6, 5], [6, 4], [6, 3], [5, 3], [4, 3], [3, 3], [2, 3], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7],
                 [1, 8], [1, 9], [1, 10], [1, 9], [1, 11], [1, 12], [1, 13], [2, 13], [3, 13], [4, 13], [5, 13],
                 [6, 13],
                 [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13], [13, 13], [14, 13], [15, 13], [16, 13],
                 [17, 13],
                 [17, 12], [12, 15], [11, 15], [10, 15], [9, 15], [8, 15], [7, 15], [7, 16], [7, 17], [7, 18], [7, 19],
                 [7, 20],
                 [7, 21], [7, 22], [7, 23], [8, 23], [9, 23], [10, 23], [11, 23], [12, 23], [12, 22], [12, 21],
                 [12, 20],
                 [12, 18],
                 [12, 17], [12, 16], [13, 12], [13, 10], [10, 10], [10, 12], [7, 12], [7, 10], [14, 17], [14, 18],
                 [14, 20],
                 [14, 21], [16, 17], [16, 18], [16, 20], [16, 21], [18, 17], [18, 18], [18, 20], [18, 21]]
            choice_alien = [[21, 1], [22, 1], [6, 2], [15, 15], [9, 18], [10, 20], [4, 6], [4, 8]]
            health_alien = [7, 7, 5, 7, 5, 5, 5, 5]
            type_alien = ['krissalid', 'krissalid', 'sectoid', 'krissalid', 'sectoid',
                          'sectoid', 'sectoid', 'sectoid']
        elif mp == 3:
            pygame.mixer.music.load('data/sounds/mission2.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            tmxdata = load_pygame("data/map3.tmx")
            s = [[25, 12], [25, 11], [25, 10], [25, 9], [25, 8], [25, 7], [25, 6], [25, 5], [25, 4], [25, 3], [25, 2],
                 [25, 1],
                 [25, 0], [25, 15], [25, 16], [25, 17], [25, 18], [25, 19], [25, 20], [25, 21], [25, 22], [25, 23],
                 [25, 24],
                 [25, 25], [25, 26], [25, 27], [25, 28], [25, 29], [15, 11], [15, 10], [15, 9], [14, 9], [14, 8],
                 [13, 8],
                 [12, 8], [11, 8], [10, 8], [9, 8], [9, 9], [8, 9], [8, 10], [7, 10], [6, 10], [6, 11], [5, 11],
                 [5, 12],
                 [4, 12], [4, 13], [4, 14], [5, 14], [5, 15], [6, 15], [6, 16], [7, 16], [8, 16], [8, 17], [9, 17],
                 [9, 18],
                 [10, 18], [11, 18], [12, 18], [13, 18], [14, 18], [14, 17], [15, 17], [15, 16], [15, 15], [14, 15],
                 [13, 17],
                 [12, 17], [11, 17], [10, 17], [14, 11], [13, 9], [12, 9], [11, 9], [10, 9], [21, 11], [23, 11],
                 [21, 9],
                 [23, 9],
                 [21, 7], [23, 7], [21, 5], [23, 5], [21, 3], [23, 3], [21, 1], [23, 1], [21, 16], [23, 16], [21, 18],
                 [23, 18],
                 [21, 20], [23, 20], [21, 22], [23, 22], [21, 24], [23, 24], [21, 26], [23, 26], [21, 28], [23, 28],
                 [11, 24],
                 [11, 23], [10, 23], [9, 23], [8, 23], [7, 23], [6, 23], [6, 24], [6, 25], [6, 26], [6, 27], [7, 27],
                 [8, 27],
                 [9, 27], [10, 27], [11, 27], [11, 26], [13, 4], [12, 4], [11, 4], [10, 4], [9, 4], [8, 4], [7, 4],
                 [7, 5],
                 [7, 6], [10, 3], [10, 2]]
            choice_alien = [[8, 12], [9, 13], [8, 14], [8, 24], [8, 26], [8, 3], [8, 1], [7, 2], [7, 25]]
            health_alien = [10, 10, 10, 5, 5, 5, 5, 5, 5]
            type_alien = ['myton', 'myton', 'myton', 'sectoid', 'sectoid',
                          'sectoid', 'sectoid', 'sectoid', 'sectoid']
        elif mp == 4:
            pygame.mixer.music.load('data/sounds/battle1.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            tmxdata = load_pygame("data/map4.tmx")
            s = [[21, 4], [21, 5], [21, 6], [21, 7], [21, 8], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 15],
                 [21, 16], [21, 17], [21, 18], [21, 19], [21, 20], [21, 21], [21, 22], [21, 24], [21, 25], [21, 26],
                 [20, 26], [19, 26], [18, 26], [17, 26], [16, 26], [15, 26], [14, 26], [13, 26], [12, 26], [11, 26],
                 [11, 25],
                 [11, 24], [11, 23], [11, 22], [11, 21], [11, 20], [11, 19], [11, 18], [11, 17], [11, 16], [11, 15],
                 [11, 14],
                 [11, 13], [11, 12], [11, 11], [11, 10], [11, 9], [11, 8], [11, 7], [11, 6], [11, 5], [11, 4], [12, 4],
                 [13, 4],
                 [14, 4], [15, 4], [16, 4], [17, 4], [18, 4], [19, 4], [20, 4], [12, 8], [13, 8], [14, 8], [15, 8],
                 [17, 8], [18, 8], [19, 8], [20, 8], [12, 12], [13, 12], [14, 12], [15, 12], [17, 12], [18, 12],
                 [19, 12],
                 [20, 12], [12, 16], [13, 16], [14, 16], [15, 16], [15, 18], [15, 19], [16, 19], [17, 19], [18, 19],
                 [19, 19],
                 [20, 19], [6, 6], [6, 7], [8, 6], [8, 7], [4, 6], [4, 7], [4, 3], [4, 4], [6, 3], [6, 4], [8, 3],
                 [8, 4],
                 [7, 19], [6, 19], [5, 19], [4, 19], [3, 19], [2, 19], [1, 19], [0, 19], [0, 20], [0, 21], [0, 22],
                 [0, 23],
                 [0, 24], [0, 25], [0, 26], [0, 27], [0, 28], [0, 29], [1, 29], [2, 29], [3, 29], [4, 29], [5, 29],
                 [6, 29],
                 [7, 29], [7, 28], [7, 27], [7, 26], [7, 25], [7, 24], [7, 23], [7, 22], [7, 21]]
            choice_alien = [[2, 12], [3, 13], [2, 14], [14, 21], [14, 23], [14, 5], [14, 7], [3, 22], [4, 23], [3, 24],
                            [14, 14]]
            health_alien = [6, 6, 6, 10, 10, 5, 5, 5, 5, 5, 5]
            type_alien = ['vaiper', 'vaiper', 'vaiper', 'myton', 'myton',
                          'sectoid', 'sectoid', 'sectoid', 'sectoid', 'sectoid', 'sectoid']
        elif mp == 5:
            pygame.mixer.music.load('data/sounds/battle3.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            tmxdata = load_pygame("data/map5_final.tmx")
            s = [[0, 9], [2, 9], [2, 10], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14], [3, 15], [3, 16], [3, 17],
                 [3, 18],
                 [3, 19], [2, 19], [2, 20], [0, 20], [6, 7], [6, 8], [6, 9], [6, 20], [6, 21], [6, 22], [8, 4], [8, 5],
                 [8, 6],
                 [8, 23], [8, 24], [8, 25], [10, 2], [10, 3], [10, 4], [10, 25], [10, 26], [10, 27], [12, 0], [12, 2],
                 [12, 4],
                 [12, 6], [12, 8], [12, 10], [12, 12], [12, 14], [12, 16], [12, 18], [12, 20], [12, 22], [12, 24],
                 [12, 26],
                 [12, 28], [19, 0], [19, 1], [19, 2], [19, 3], [19, 5], [19, 6], [19, 7], [19, 8], [19, 9], [19, 10],
                 [20, 10],
                 [21, 10], [22, 10], [23, 10], [24, 10], [25, 10], [26, 10], [27, 10], [28, 10], [29, 10], [29, 19],
                 [28, 19],
                 [27, 19], [26, 19], [25, 19], [24, 19], [23, 19], [22, 19], [21, 19], [20, 19], [19, 19], [19, 20],
                 [19, 21],
                 [19, 22], [19, 23], [19, 24], [19, 26], [19, 27], [19, 28], [19, 29]]
            choice_alien = [[1, 13], [1, 14], [1, 15], [3, 25], [4, 26], [4, 3],
                            [3, 4], [26, 3], [25, 4], [26, 5], [26, 23], [25, 24], [26, 25]]
            health_alien = [10, 10, 10, 7, 6, 7, 6, 5, 5, 5, 5, 5, 5]
            type_alien = ['myton', 'myton', 'myton', 'krissalid', 'vaiper',
                          'krissalid', 'vaiper', 'sectoid', 'sectoid', 'sectoid', 'sectoid', 'sectoid', 'sectoid']
        flag = [2000, 2000]
        hero = 0
        error_tail = 0
        way = 0
        fj = 0
        fire = 0
        flag_ab = [0, 0, 0, 0]
        mrh = 0
        col_ab = [0, 0, 0, 0]
        flag_ab1 = 0
        flag_choice_alien = 0
        health_hero = [6, 5, 4, 5]
        choice_hs = [[28, 13], [28, 12], [29, 11], [29, 14]]
        dead = [0, 0, 0, 0]
        flag_turn = 0  # флаг хода саппорта
        flag_turn1 = 0  # флаг хода штурмовика
        flag_turn2 = 0  # флаг хода снайпера
        flag_turn3 = 0  # флаг хода медика
        turn_enemy = 0  # флаг хода клятых алиенов
        hit = 0
        tmp = 10
        g1 = []
        destr = []  # список разрушений


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
                            if type_alien[choice_alien.index(elem)] == 'sectoid':
                                screen.blit(sectoid, (elem[1] * 32, elem[0] * 32))
                            elif type_alien[choice_alien.index(elem)] == 'krissalid':
                                screen.blit(krissalid, (elem[1] * 32, elem[0] * 32))
                            elif type_alien[choice_alien.index(elem)] == 'myton':
                                screen.blit(myton, (elem[1] * 32, elem[0] * 32))
                            elif type_alien[choice_alien.index(elem)] == 'vaiper':
                                screen.blit(vaiper, (elem[1] * 32, elem[0] * 32))
                        if dead[0] == 0:
                            screen.blit(support, (choice_hs[0][1] * 32, choice_hs[0][0] * 32))
                        if dead[1] == 0:
                            screen.blit(eng, (choice_hs[1][1] * 32, choice_hs[1][0] * 32))
                        if dead[2] == 0:
                            screen.blit(sniper, (choice_hs[2][1] * 32, choice_hs[2][0] * 32))
                        if dead[3] == 0:
                            screen.blit(medic, (choice_hs[3][1] * 32, choice_hs[3][0] * 32))
                        if dead[0] == 1:
                            screen.blit(dead_support, (choice_hs[0][1] * 32, choice_hs[0][0] * 32))
                        if dead[1] == 1:
                            screen.blit(dead_eng, (choice_hs[1][1] * 32, choice_hs[1][0] * 32))
                        if dead[2] == 1:
                            screen.blit(dead_sniper, (choice_hs[2][1] * 32, choice_hs[2][0] * 32))
                        if dead[3] == 1:
                            screen.blit(dead_medic, (choice_hs[3][1] * 32, choice_hs[3][0] * 32))
                        if hero == 1 or hero == 2 or hero == 3 or hero == 4:
                            screen.blit(menu, (960, 0))
                            if dead[0] == 0 and hero == 1:
                                screen.blit(sup, (1090, 152))
                                screen.blit(health1, (1070, 46))
                                if flag_turn == 1:
                                    screen.blit(action, (965, 176))
                                if flag_turn == 0:
                                    screen.blit(action, (965, 176))
                                    screen.blit(action, (1080, 176))
                                if col_ab[0] == 0:
                                    screen.blit(support_ability, (1095, 70))
                            elif hero == 2 and dead[1] == 0:
                                screen.blit(health2, (1070, 46))
                                screen.blit(en, (1090, 152))
                                if flag_turn1 == 1:
                                    screen.blit(action, (965, 176))
                                if flag_turn1 == 0:
                                    screen.blit(action, (965, 176))
                                    screen.blit(action, (1080, 176))
                                if col_ab[1] == 0:
                                    screen.blit(eng_ability, (1095, 70))
                            elif hero == 3 and dead[2] == 0:
                                screen.blit(health3, (1070, 46))
                                screen.blit(sn, (1090, 152))
                                if flag_turn2 == 1:
                                    screen.blit(action, (965, 176))
                                if flag_turn2 == 0:
                                    screen.blit(action, (965, 176))
                                    screen.blit(action, (1080, 176))
                                if col_ab[2] == 0:
                                    screen.blit(sniper_ability, (1095, 70))
                            elif hero == 4 and dead[3] == 0:
                                screen.blit(health4, (1070, 46))
                                screen.blit(md, (1090, 152))
                                if flag_turn3 == 1:
                                    screen.blit(action, (965, 176))
                                if flag_turn3 == 0:
                                    screen.blit(action, (965, 176))
                                    screen.blit(action, (1080, 176))
                                if col_ab[3] == 0:
                                    screen.blit(medic_ability, (1095, 70))
                        if x == flag[1] and y == flag[0]:
                            screen.blit(red, (flag[1] * 32, flag[0] * 32))
                        elif error_tail == 1:
                            screen.blit(red, (s1[1] * 32, s1[0] * 32))
                        if [x * 32, y * 32] in destr:
                            screen.blit(del_bl, (x * 32, y * 32))
                        else:
                            screen.blit((tmxdata.get_tile_image(x, y, 0)), (x * 32, y * 32))
                        if fire == 2 and flag_ab[hero - 1] == 0:
                            screen.blit(health_a, (965, 280))
                            screen.blit(ffire, (965, 208))
                            screen.blit(shoot, (970, 230))
                        if fire == 1:
                            screen.blit(health_a, (965, 280))
                            screen.blit(ire, (965, 208))
                            screen.blit(shoot, (970, 230))
                        if tmp != 10:
                            if fire == 3:
                                screen.blit(health_a, (965, 280))
                                screen.blit(re, (965, 208))
                            elif mrh == 1:
                                screen.blit(strk, (965, 208))
                            else:
                                screen.blit(miss, (965, 208))
                        if flag_ab1 == 1:
                            for cor in range(g1[0] - 2, g1[0] + 3):
                                if cor >= 0 and cor <= 30 and g1[1] * 32 + 64 >= 0 and g1[1] * 32 - 64 <= 960:
                                    screen.blit(zone1, (cor * 32, g1[1] * 32 + 64))
                                    screen.blit(zone1, (cor * 32, g1[1] * 32 - 96))
                            for cor in range(g1[1] - 2, g1[1] + 3):
                                if cor >= 0 and cor <= 30 and g1[0] * 32 + 64 >= 0 and g1[0] * 32 - 64 <= 960:
                                    screen.blit(zone, (g1[0] * 32 + 96, cor * 32))
                                    screen.blit(zone, (g1[0] * 32 - 64, cor * 32))

            def get_cell(self, mouse_pos):
                if mouse_pos[0] < self.width * self.cell_size and \
                        mouse_pos[1] < self.height * self.cell_size:
                    x = (mouse_pos[0]) // self.cell_size
                    y = (mouse_pos[1]) // self.cell_size
                    return y, x  # обратите внимание!!!!!
                else:
                    return None

            def get_click(self, mouse_pos):
                cell = self.get_cell(mouse_pos)
                self.on_click(cell)

            def on_click(self, cell):
                if cell != None:
                    pass


        def load_image1(name):
            fullname = os.path.join('data/Текстуры', name)
            image = pygame.image.load(fullname).convert()
            return image


        def load_image(name):
            fullname = os.path.join('data/Текстуры', name)
            image = pygame.image.load(fullname)
            return image


        board = XCOM(30, 30)
        rg = True
        clock = pygame.time.Clock()
        global_menu = load_image1('global_menu.png')
        menu = load_image1('menut.png')
        support = load_image('Heavy_support.png')
        eng = load_image('Engeniiiiiier.png')
        sniper = load_image('sniper.png')
        medic = load_image('medic.png')
        zone1 = load_image('zone1.png')
        red = load_image('red_sqr.png')
        dead_support = load_image('dead_support.png')
        dead_sniper = load_image('dead_sniper.png')
        dead_eng = load_image('dead_eng.png')
        dead_medic = load_image('dead_medic.png')
        sectoid = load_image('sectoid.png')
        del_bl = load_image('del_blok.png')
        del_bl1 = load_image('del_bl1.png')
        action = load_image1('action.png')
        shoot = load_image1('shoot.png')
        zone = load_image('zone_explosion.png')
        myton = load_image('myton.png')
        vaiper = load_image('vaiper.png')
        krissalid = load_image('krissalids.png')
        support_ability = load_image1('rocket_support.png')
        eng_ability = load_image1('eng_explosion.png')
        sniper_ability = load_image1('sniper_shot.png')
        medic_ability = load_image1('medic_reanimation.png')
        dead_menu = load_image1('dead_menu.png')
        text_menu = pygame.font.Font(None, 24)
        sup = text_menu.render('Поддержка', 0, (0, 0, 0))
        en = text_menu.render('Инженер', 0, (0, 0, 0))
        sn = text_menu.render('Снайпер', 0, (0, 0, 0))
        md = text_menu.render('Медик', 0, (0, 0, 0))
        ffire = text_menu.render('Шанс попадания - ' + str(hit), 0, (0, 0, 0))
        health1 = text_menu.render(str(health_hero[0]), 0, (255, 0, 0))
        health2 = text_menu.render(str(health_hero[1]), 0, (255, 0, 0))
        health3 = text_menu.render(str(health_hero[2]), 0, (255, 0, 0))
        health4 = text_menu.render(str(health_hero[3]), 0, (255, 0, 0))
        ire = text_menu.render('Вы не поразите цель.', 0, (0, 0, 0))
        re = text_menu.render('Вам не хватает дальности', 0, (0, 0, 0))
        miss = text_menu.render('Промах', 0, (0, 0, 0))
        strk = text_menu.render('Попадание', 0, (0, 0, 0))
        health_a = text_menu.render('HP пришельца - ' + str(health_alien[flag_choice_alien]), 0, (0, 0, 0))
        wall = pygame.sprite.Group()
        for elem in s:
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image("blue wall.png")
            sprite.rect = sprite.image.get_rect()
            wall.add(sprite)
            sprite.rect.x = elem[1] * 32
            sprite.rect.y = elem[0] * 32
        wall.draw(screen)
        fire_line = load_image("red_sqr.png")
        while rg:
            pl = 0
            if len(choice_alien) == 0:
                rg = False
                in_game = True
                stop = False
                tm += 1
                time_rn += datetime.timedelta(days=1)
            for r in dead:
                pl += r
            if pl == 8:
                rg = False
                in_game = True
                stop = False
                tm += 1
                time_rn += datetime.timedelta(days=1)
                if panic[coord_missions.index(click_coord)] != 2:
                    panic[coord_missions.index(click_coord)] += 1
            if dead[0] == 0:
                health1 = text_menu.render(str(health_hero[0]), 0, (255, 0, 0))
            if dead[1] == 0:
                health2 = text_menu.render(str(health_hero[1]), 0, (255, 0, 0))
            if dead[2] == 0:
                health3 = text_menu.render(str(health_hero[2]), 0, (255, 0, 0))
            if dead[3] == 0:
                health4 = text_menu.render(str(health_hero[3]), 0, (255, 0, 0))
            for elem in health_hero:
                if elem <= 0:
                    dead[health_hero.index(elem)] = 1
                    if dead[0] == 1:
                        flag_turn = 2
                    if dead[1] == 1:
                        flag_turn1 = 2
                    if dead[2] == 1:
                        flag_turn2 = 2
                    if dead[3] == 1:
                        flag_turn3 = 2
            for elem in wall:
                x = elem.rect.x
                y = elem.rect.y
                if [y // 32, x // 32] not in s:
                    elem.kill()
                    destr.append([x, y])
            for hp in health_alien:
                if hp <= 0:
                    del choice_alien[health_alien.index(hp)]
                    del type_alien[health_alien.index(hp)]
                    del health_alien[health_alien.index(hp)]

            if flag_turn == 2 and flag_turn1 == 2 and flag_turn2 == 2 and flag_turn3 == 2:
                turn_enemy = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rg = False
                if event.type == pygame.MOUSEBUTTONDOWN and turn_enemy == 0:
                    if event.button == 1:
                        board.get_click(event.pos)
                        if event.pos[0] <= 960 and event.pos[1] <= 960:
                            s1 = [board.get_cell(event.pos)[0], board.get_cell(event.pos)[1]]
                        if s1 in s:
                            flag = s1
                        if s1 in choice_alien:
                            health_a = text_menu.render(
                                'HP пришельца - ' + str(health_alien[choice_alien.index(s1)]), 0,
                                (0, 0, 0))
                        if event.pos[0] >= 1095 and event.pos[1] >= 70 and event.pos[0] <= 1127 and event.pos[1] <= 102 \
                                and col_ab[hero - 1] == 0:  # flag ab.
                            if hero == 1:
                                flag_ab[0] = 1
                            elif hero == 3:
                                flag_ab[2] = 1
                            elif hero == 2:
                                flag_ab[1] = 1
                            elif hero == 4:
                                flag_ab[3] = 1

                        if fire == 1 or fire == 2:
                            if event.pos[0] >= 970 and event.pos[1] >= 230 and event.pos[0] <= 1190 and event.pos[
                                1] <= 270:
                                if hero == 1:
                                    flag_turn = 2
                                if hero == 2:
                                    flag_turn1 = 2
                                if hero == 3:
                                    flag_turn2 = 2
                                if hero == 4:
                                    flag_turn3 = 2
                                if fire == 1:
                                    for elem in sd:
                                        if [elem[1] // 32, elem[0] // 32] in s:
                                            del s[s.index([elem[1] // 32, elem[0] // 32])]
                                        destr.append(elem)
                                    for ele in s_kill:
                                        ele.kill()
                                else:
                                    ver = random.uniform(0, 100)
                                    if ver <= hit:
                                        mrh = 1
                                        if hero == 1:
                                            x = random.randint(3, 4)
                                            health_alien[flag_choice_alien] -= x
                                            if health_alien[flag_choice_alien] > 0:
                                                strk = text_menu.render('Попадание' + ' HP пришельца - ' +
                                                                        str(health_alien[flag_choice_alien]), 0,
                                                                        (0, 0, 0))
                                                health_a = text_menu.render(
                                                    'HP пришельца - ' + str(health_alien[flag_choice_alien]), 0,
                                                    (0, 0, 0))
                                            else:
                                                strk = text_menu.render('Пришелец уничтожен', 0, (0, 0, 0))
                                            for hp in health_alien:
                                                if hp <= 0:
                                                    del choice_alien[health_alien.index(hp)]
                                                    del type_alien[health_alien.index(hp)]
                                                    del health_alien[health_alien.index(hp)]
                                        if hero == 2:
                                            x1 = random.randint(2, 3)
                                            health_alien[flag_choice_alien] -= x1
                                            if health_alien[flag_choice_alien] > 0:
                                                strk = text_menu.render('Попадание' + ' HP пришельца - ' +
                                                                        str(health_alien[flag_choice_alien]), 0,
                                                                        (0, 0, 0))
                                                health_a = text_menu.render(
                                                    'HP пришельца - ' + str(health_alien[flag_choice_alien]), 0,
                                                    (0, 0, 0))
                                            else:
                                                strk = text_menu.render('Пришелец уничтожен', 0, (0, 0, 0))
                                            for hp in health_alien:
                                                if hp <= 0:
                                                    del choice_alien[health_alien.index(hp)]
                                                    del type_alien[health_alien.index(hp)]
                                                    del health_alien[health_alien.index(hp)]
                                        if hero == 3:
                                            x2 = random.randint(4, 5)
                                            health_alien[flag_choice_alien] -= x2
                                            if health_alien[flag_choice_alien] > 0:
                                                strk = text_menu.render('Попадание' + ' HP пришельца - ' +
                                                                        str(health_alien[flag_choice_alien]), 0,
                                                                        (0, 0, 0))
                                                health_a = text_menu.render(
                                                    'HP пришельца - ' + str(health_alien[flag_choice_alien]), 0,
                                                    (0, 0, 0))
                                            else:
                                                strk = text_menu.render('Пришелец уничтожен', 0, (0, 0, 0))
                                            for hp in health_alien:
                                                if hp <= 0:
                                                    del choice_alien[health_alien.index(hp)]
                                                    del type_alien[health_alien.index(hp)]
                                                    del health_alien[health_alien.index(hp)]
                                        if hero == 4:
                                            x2 = random.randint(1, 3)
                                            health_alien[flag_choice_alien] -= x2
                                            if health_alien[flag_choice_alien] > 0:
                                                strk = text_menu.render('Попадание' + ' HP пришельца - ' +
                                                                        str(health_alien[flag_choice_alien]), 0,
                                                                        (0, 0, 0))
                                                health_a = text_menu.render(
                                                    'HP пришельца - ' + str(health_alien[flag_choice_alien]), 0,
                                                    (0, 0, 0))
                                            else:
                                                strk = text_menu.render('Пришелец уничтожен', 0, (0, 0, 0))
                                            for hp in health_alien:
                                                if hp <= 0:
                                                    del choice_alien[health_alien.index(hp)]
                                                    del type_alien[health_alien.index(hp)]
                                                    del health_alien[health_alien.index(hp)]
                                    else:
                                        mrh = 0
                                    tmp = 0
                                fire = 0

                        if flag_ab1 == 1:  # ability support
                            flag_ab1 = 0
                            flag_ab[0] = 0
                            col_ab[0] = 1
                            for xx in range(s1[1] - 2, s1[1] + 3):
                                for yy in range(s1[0] - 2, s1[0] + 3):
                                    if [yy, xx] in s:
                                        del s[s.index([yy, xx])]
                                    elif [yy, xx] in choice_alien:
                                        u = random.randint(4, 7)
                                        health_alien[choice_alien.index([yy, xx])] -= u
                                        health_a = text_menu.render(
                                            'HP пришельца - ' + str(health_alien[choice_alien.index([yy, xx])]), 0,
                                            (0, 0, 0))

                        elif flag_ab[2] == 1 and s1 in choice_alien:  # ability sniper
                            u = random.randint(4, 7)
                            health_alien[choice_alien.index(s1)] -= u
                            col_ab[2] = 1
                            flag_ab[2] = 0

                        elif flag_ab[1] == 1 and s1 in s and abs(s1[0] - choice_hs[1][0]) <= 1 and abs(
                                s1[1] - choice_hs[1][1]) \
                                <= 1:  # ability eng
                            col_ab[1] = 1
                            fj = 1
                            flag_ab[1] = 0
                            del s[s.index(s1)]

                        elif flag_ab[3] == 1 and s1 == choice_hs[dead.index(1)]:  # ability medic
                            col_ab[3] = 1
                            flag_ab[3] = 0
                            dead[choice_hs.index(s1)] = 0
                            health_hero[choice_hs.index(s1)] = 4

                        elif hero != 0 and s1 in choice_alien and event.pos[0] <= 960 and event.pos[1] <= 960:
                            flag_choice_alien = choice_alien.index(s1)
                            if hero == 1 and flag_turn != 2:
                                if Fire.fire(Fire(), choice_hs[0][0], choice_hs[0][1], s1[0], s1[1], fire_line, wall,
                                             10,
                                             screen):
                                    sd = \
                                    Fire.fire(Fire(), choice_hs[0][0], choice_hs[0][1], s1[0], s1[1], fire_line, wall,
                                              10,
                                              screen)[0]
                                    s_kill = \
                                    Fire.fire(Fire(), choice_hs[0][0], choice_hs[0][1], s1[0], s1[1], fire_line, wall,
                                              10,
                                              screen)[1]
                                    if sd == 1:
                                        health_a = text_menu.render(
                                            'HP пришельца - ' + str(health_alien[choice_alien.index([s1[0], s1[1]])]),
                                            0,
                                            (0, 0, 0))
                                        fire = 3
                                        tmp = 0
                                    elif sd:
                                        fire = 1
                                else:
                                    fire = 2
                                    hit = Chance.hit(Chance(), choice_hs[0][0], choice_hs[0][1], s1[0], s1[1], s, 0)
                                    ffire = text_menu.render('Шанс попадания - ' + str(hit), 0, (0, 0, 0))
                            elif hero == 2 and flag_turn1 != 2:
                                if Fire.fire(Fire(), choice_hs[1][0], choice_hs[1][1], s1[0], s1[1], fire_line, wall, 9,
                                             screen):
                                    sd = \
                                    Fire.fire(Fire(), choice_hs[1][0], choice_hs[1][1], s1[0], s1[1], fire_line, wall,
                                              9,
                                              screen)[0]
                                    s_kill = \
                                        Fire.fire(Fire(), choice_hs[1][0], choice_hs[1][1], s1[0], s1[1], fire_line,
                                                  wall, 9,
                                                  screen)[1]
                                    if sd == 1:
                                        fire = 3
                                        health_a = text_menu.render(
                                            'HP пришельца - ' + str(health_alien[choice_alien.index([s1[0], s1[1]])]),
                                            0,
                                            (0, 0, 0))
                                        tmp = 0
                                    elif sd:
                                        fire = 1
                                else:
                                    fire = 2
                                    hit = Chance.hit(Chance(), choice_hs[1][0], choice_hs[1][1], s1[0], s1[1], s, 0)
                                    ffire = text_menu.render('Шанс попадания - ' + str(hit), 0, (0, 0, 0))
                            elif hero == 3 and flag_turn2 == 0:
                                if Fire.fire(Fire(), choice_hs[2][0], choice_hs[2][1], s1[0], s1[1], fire_line, wall,
                                             15,
                                             screen):
                                    sd = \
                                    Fire.fire(Fire(), choice_hs[2][0], choice_hs[2][1], s1[0], s1[1], fire_line, wall,
                                              15,
                                              screen)[0]
                                    s_kill = \
                                    Fire.fire(Fire(), choice_hs[2][0], choice_hs[2][1], s1[0], s1[1], fire_line, wall,
                                              15, screen)[1]
                                    if sd == 1:
                                        fire = 3
                                        health_a = text_menu.render(
                                            'HP пришельца - ' + str(health_alien[choice_alien.index([s1[0], s1[1]])]),
                                            0,
                                            (0, 0, 0))
                                        tmp = 0
                                    elif sd:
                                        fire = 1
                                else:
                                    fire = 2
                                    hit = Chance.hit(Chance(), choice_hs[2][0], choice_hs[2][1], s1[0], s1[1], s, 1)
                                    ffire = text_menu.render('Шанс попадания - ' + str(hit), 0, (0, 0, 0))
                            elif hero == 4 and flag_turn3 != 2:
                                if Fire.fire(Fire(), choice_hs[3][0], choice_hs[3][1], s1[0], s1[1], fire_line, wall, 9,
                                             screen):
                                    sd = \
                                    Fire.fire(Fire(), choice_hs[3][0], choice_hs[3][1], s1[0], s1[1], fire_line, wall,
                                              9,
                                              screen)[0]
                                    s_kill = \
                                    Fire.fire(Fire(), choice_hs[3][0], choice_hs[3][1], s1[0], s1[1], fire_line, wall,
                                              9, screen)[1]
                                    if sd == 1:
                                        fire = 3
                                        health_a = text_menu.render(
                                            'HP пришельца - ' + str(health_alien[choice_alien.index([s1[0], s1[1]])]),
                                            0,
                                            (0, 0, 0))
                                        tmp = 0
                                    elif sd:
                                        fire = 1
                                else:
                                    fire = 2
                                    hit = Chance.hit(Chance(), choice_hs[3][0], choice_hs[3][1], s1[0], s1[1], s, 0)
                                    ffire = text_menu.render('Шанс попадания - ' + str(hit), 0, (0, 0, 0))
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    fire = 0
                        if s1 not in choice_alien and event.pos[0] <= 960 and event.pos[1] <= 960:
                            if s1 == choice_hs[0] and dead[0] == 0:  # support
                                if s1 not in s:
                                    hero = 1
                                    error_tail = 0
                                    choice_hs[0] = s1
                            if s1 != choice_hs[0] and hero == 1 and dead[0] == 0:
                                if s1 not in s and Move.way(Move(), s, choice_hs[0][1], choice_hs[0][0], s1[1], s1[0],
                                                            7) \
                                        and flag_turn != 2 and s1 != choice_hs[2] and s1 != choice_hs[3] and s1 != \
                                        choice_hs[1] \
                                        and s1 not in choice_alien:
                                    choice_hs[0] = s1
                                    hero = 0
                                    flag_turn += 1
                                    error_tail = 0
                                    flag[0] = flag[0] + 1000
                                else:
                                    if flag_ab[0] == 0:
                                        error_tail = 1

                            if s1 == choice_hs[1] and dead[1] == 0:  # eng
                                if s1 not in s:
                                    hero = 2
                                    error_tail = 0
                                    choice_hs[1] = s1
                            if s1 != choice_hs[1] and hero == 2 and dead[1] == 0:
                                if s1 not in s and Move.way(Move(), s, choice_hs[1][1], choice_hs[1][0],
                                                            s1[1], s1[0], 9) \
                                        and flag_turn1 != 2 and s1 not in choice_hs \
                                        and s1 not in choice_alien and fj == 0:
                                    choice_hs[1] = s1
                                    hero = 0
                                    flag_turn1 += 1
                                    error_tail = 0
                                    flag[0] = flag[0] + 1000
                                else:
                                    if flag_ab[1] == 0:
                                        error_tail = 1

                            if s1 == choice_hs[2] and dead[2] == 0:  # sniper
                                if s1 not in s:
                                    hero = 3
                                    error_tail = 0
                                    choice_hs[2] = s1
                            if s1 != choice_hs[2] and hero == 3 and dead[2] == 0:
                                if s1 not in s and Move.way(Move(), s, choice_hs[2][1],
                                                            choice_hs[2][0], s1[1], s1[0], 7) \
                                        and flag_turn2 != 2 and s1 not in choice_hs \
                                        and s1 not in choice_alien:
                                    choice_hs[2] = s1
                                    hero = 0
                                    error_tail = 0
                                    flag_turn2 += 1
                                    flag[0] = flag[0] + 1000
                                else:
                                    if flag_ab[2] == 0:
                                        error_tail = 1

                            if s1 == choice_hs[3] and dead[3] == 0:  # medic
                                if s1 not in s:
                                    hero = 4
                                    error_tail = 0
                                    choice_hs[3] = s1
                            if s1 != choice_hs[3] and hero == 4 and dead[3] == 0:
                                if s1 not in s and Move.way(Move(), s, choice_hs[3][1],
                                                            choice_hs[3][0], s1[1], s1[0], 9) \
                                        and flag_turn3 != 2 and s1 not in choice_hs \
                                        and s1 not in choice_alien:
                                    choice_hs[3] = s1
                                    hero = 0
                                    error_tail = 0
                                    flag_turn3 += 1
                                    flag[0] = flag[0] + 1000
                                else:
                                    error_tail = 1
                        if event.pos[0] > 1100 and event.pos[1] > 870:
                            flag_turn = 0
                            flag_turn1 = 0
                            flag_turn2 = 0
                            flag_turn3 = 0
                            turn_enemy = 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        turn_enemy = 1
                    if event.key == pygame.K_ESCAPE:
                        fire = 0
                        flag_ab[0] = 0
                        flag_ab1 = 0
                        flag_ab[2] = 0
                        flag_ab[1] = 0
                        flag_ab[3] = 0
                if event.type == pygame.MOUSEMOTION and flag_ab[0] == 1 and event.pos[0] <= 960 and event.pos[1] <= 960:
                    # first ability
                    g1 = [board.get_cell(event.pos)[1], board.get_cell(event.pos)[0]]
                    b_way = math.sqrt(
                        (abs(choice_hs[hero - 1][1] - g1[0]) ** 2) + (abs(choice_hs[hero - 1][0] - g1[1]) ** 2))
                    math.floor(b_way)
                    b_way = int(b_way)
                    if b_way <= 15:
                        flag_ab1 = 1
                    else:
                        flag_ab1 = 0
                    board.render()
                if turn_enemy == 1:
                    for elem in choice_alien:
                        x = []
                        y = []
                        if type_alien[choice_alien.index(elem)] == 'sectoid':
                            best_enemy = [1000, 1000]
                            for p in choice_hs:
                                if abs(p[0] - elem[0]) <= abs(best_enemy[0] - elem[0]) \
                                        and abs(p[1] - elem[1]) <= abs(best_enemy[1] - elem[1]) and \
                                        dead[choice_hs.index(p)] == 0:
                                    best_enemy[0] = p[0]
                                    best_enemy[1] = p[1]
                            rm = random.uniform(0, 100)
                            if Fire.fire(Fire(), elem[0], elem[1], best_enemy[0], best_enemy[1], fire_line, wall, 9,
                                         screen) is False and rm <= 80:
                                if Chance.hit(Chance(), elem[0], elem[1], best_enemy[0], best_enemy[1], s, 0) <= \
                                        random.uniform(1, 100):
                                    dmg = random.randint(1, 3)
                                    health_hero[choice_hs.index(best_enemy)] -= dmg
                                turn_enemy = 0
                            else:
                                for _ in range(3):
                                    x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                    y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                flag_x = 100
                                flag_y = 100
                                for e in y:
                                    if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                        flag_y = e
                                for t in x:
                                    if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                        flag_y = t
                                perfect_coords = [flag_x, flag_y]
                                fg = 1
                                while fg == 1:
                                    x = []
                                    y = []
                                    for _ in range(3):
                                        x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                        y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                    flag_x = 100
                                    flag_y = 100
                                    for e in y:
                                        if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                            flag_y = e
                                    for t in x:
                                        if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                            flag_x = t
                                    perfect_coords = [flag_x, flag_y]
                                    if perfect_coords in s:
                                        fg = 1
                                    elif perfect_coords in choice_hs:
                                        fg = 1
                                    elif perfect_coords in choice_alien:
                                        fg = 1
                                    elif Move.way(Move(), s, elem[1], elem[0], perfect_coords[1], perfect_coords[0],
                                                  5) is not \
                                            True:
                                        fg = 1
                                    else:
                                        fg = 0
                                choice_alien[choice_alien.index(elem)] = perfect_coords
                        elif type_alien[choice_alien.index(elem)] == 'myton':
                            best_enemy = [1000, 1000]
                            for p in choice_hs:
                                if abs(p[0] - elem[0]) <= abs(best_enemy[0] - elem[0]) \
                                        and abs(p[1] - elem[1]) <= abs(best_enemy[1] - elem[1]) and \
                                        dead[choice_hs.index(p)] == 0:
                                    best_enemy[0] = p[0]
                                    best_enemy[1] = p[1]
                            rm = random.uniform(0, 100)
                            if Fire.fire(Fire(), elem[0], elem[1], best_enemy[0], best_enemy[1], fire_line, wall, 11,
                                         screen) is False and rm <= 90:
                                if Chance.hit(Chance(), elem[0], elem[1], best_enemy[0], best_enemy[1], s, 0) <= \
                                        random.uniform(1, 100):
                                    dmg = random.randint(3, 5)
                                    health_hero[choice_hs.index(best_enemy)] -= dmg
                                turn_enemy = 0
                            else:
                                for _ in range(3):
                                    x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                    y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                flag_x = 100
                                flag_y = 100
                                for e in y:
                                    if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                        flag_y = e
                                for t in x:
                                    if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                        flag_y = t
                                perfect_coords = [flag_x, flag_y]
                                fg = 1
                                while fg == 1:
                                    x = []
                                    y = []
                                    for _ in range(3):
                                        x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                        y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                    flag_x = 100
                                    flag_y = 100
                                    for e in y:
                                        if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                            flag_y = e
                                    for t in x:
                                        if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                            flag_x = t
                                    perfect_coords = [flag_x, flag_y]
                                    if perfect_coords in s:
                                        fg = 1
                                    elif perfect_coords in choice_hs:
                                        fg = 1
                                    elif perfect_coords in choice_alien:
                                        fg = 1
                                    elif Move.way(Move(), s, elem[1], elem[0], perfect_coords[1], perfect_coords[0],
                                                  5) is not \
                                            True:
                                        fg = 1
                                    else:
                                        fg = 0
                                choice_alien[choice_alien.index(elem)] = perfect_coords
                        elif type_alien[choice_alien.index(elem)] == 'krissalid':
                            best_enemy = [1000, 1000]
                            for p in choice_hs:
                                if abs(p[0] - elem[0]) <= abs(best_enemy[0] - elem[0]) \
                                        and abs(p[1] - elem[1]) <= abs(best_enemy[1] - elem[1]) and \
                                        dead[choice_hs.index(p)] == 0:
                                    best_enemy[0] = p[0]
                                    best_enemy[1] = p[1]
                            if abs(best_enemy[0] - elem[0]) <= 1 and abs(best_enemy[1] - elem[1]) <= 1:
                                dmg = random.randint(3, 7)
                                health_hero[choice_hs.index(best_enemy)] -= dmg
                            else:
                                for _ in range(3):
                                    x.append(random.randint(elem[0] - 5, elem[0] + 5))
                                    y.append(random.randint(elem[1] - 5, elem[1] + 5))
                                flag_x = 1000
                                flag_y = 1000
                                for e in y:
                                    if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                        flag_y = e
                                for t in x:
                                    if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                        flag_x = t
                                perfect_coords = [flag_x, flag_y]
                                fh = 1
                                while fh == 1:
                                    for _ in range(3):
                                        x.append(random.randint(elem[0] - 5, elem[0] + 5))
                                        y.append(random.randint(elem[1] - 5, elem[1] + 5))
                                    flag_x = 1000
                                    flag_y = 1000
                                    for e in y:
                                        if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                            flag_y = e
                                    for t in x:
                                        if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                            flag_x = t
                                    perfect_coords = [flag_x, flag_y]
                                    if perfect_coords not in s and perfect_coords not in \
                                            choice_alien and perfect_coords not in choice_hs:
                                        fh = 0
                                    else:
                                        fh = 1
                                choice_alien[choice_alien.index(elem)] = perfect_coords
                        elif type_alien[choice_alien.index(elem)] == 'vaiper':
                            best_enemy = [1000, 1000]
                            for p in choice_hs:
                                if abs(p[0] - elem[0]) <= abs(best_enemy[0] - elem[0]) \
                                        and abs(p[1] - elem[1]) <= abs(best_enemy[1] - elem[1]) and \
                                        dead[choice_hs.index(p)] == 0:
                                    best_enemy[0] = p[0]
                                    best_enemy[1] = p[1]
                            if Fire.fire(Fire(), elem[0], elem[1], best_enemy[0], best_enemy[1], fire_line, wall, 15,
                                         screen) is False:
                                if Chance.hit(Chance(), elem[0], elem[1], best_enemy[0], best_enemy[1], s, 1) <= \
                                        random.uniform(1, 100):
                                    dmg = random.randint(4, 5)
                                    health_hero[choice_hs.index(best_enemy)] -= dmg
                                turn_enemy = 0
                            else:
                                for _ in range(3):
                                    x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                    y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                flag_x = 100
                                flag_y = 100
                                for e in y:
                                    if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                        flag_y = e
                                for t in x:
                                    if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                        flag_y = t
                                perfect_coords = [flag_x, flag_y]
                                fg = 1
                                while fg == 1:
                                    x = []
                                    y = []
                                    for _ in range(3):
                                        x.append(random.randint(elem[0] - 2, elem[0] + 2))
                                        y.append(random.randint(elem[1] - 2, elem[1] + 2))
                                    flag_x = 100
                                    flag_y = 100
                                    for e in y:
                                        if abs(best_enemy[1] - flag_y) > abs(best_enemy[1] - e):
                                            flag_y = e
                                    for t in x:
                                        if abs(best_enemy[0] - flag_x) > abs(best_enemy[0] - t):
                                            flag_x = t
                                    perfect_coords = [flag_x, flag_y]
                                    if perfect_coords in s:
                                        fg = 1
                                    elif perfect_coords in choice_hs:
                                        fg = 1
                                    elif perfect_coords in choice_alien:
                                        fg = 1
                                    elif Move.way(Move(), s, elem[1], elem[0], perfect_coords[1], perfect_coords[0],
                                                  5) is not \
                                            True:
                                        fg = 1
                                    else:
                                        fg = 0
                                choice_alien[choice_alien.index(elem)] = perfect_coords
                    if dead[0] == 0:
                        flag_turn = 0
                    if dead[1] == 0:
                        flag_turn1 = 0
                    if dead[2] == 0:
                        flag_turn2 = 0
                    if dead[3] == 0:
                        flag_turn3 = 0
                    turn_enemy = 0
            fj = 0
            if tmp != 10:
                tmp += 1
            board.render()
            clock.tick(10)
            pygame.display.flip()

