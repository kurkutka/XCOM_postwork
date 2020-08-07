import os
import pygame


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
        screen.blit(text, (20, 350))
        if self.x >= 10:
            self.alex.draw(screen)
            text = pygame.font.SysFont(None, 36).render('Александр Буренчев', True, pygame.Color('green'))
            screen.blit(text, (10, 240 - text.get_height() // 2))
        if self.x >= 25:
            self.kirill.draw(screen)
            text = pygame.font.SysFont(None, 36).render('Кирилл Золотарев', True, pygame.Color('red'))
            screen.blit(text, (280, 240 - text.get_height() // 2))
        if self.x >= 40:
            self.ilya.draw(screen)
            text = pygame.font.SysFont(None, 36).render('Илья Борисов', True, pygame.Color('purple'))
            screen.blit(text, (580, 240 - text.get_height() // 2))
        if self.x >= 80:
            running = False
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.rect.x += 20


pygame.init()
FPS = 5
all_sprites = pygame.sprite.Group()
alex = pygame.sprite.Sprite()
kirill = pygame.sprite.Sprite()
ilya = pygame.sprite.Sprite()
todd = pygame.sprite.Sprite()
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
running = True
screen.fill((0, 0, 0))
image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/cat.png')), (200, 200))
alex.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/alex.jpg')), (260, 230))
alex.rect = alex.image.get_rect()
alex.rect.x = 10
alex.rect.y = 0
kirill.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/kirill.png')), (260, 230))
kirill.rect = kirill.image.get_rect()
kirill.rect.x = 270
kirill.rect.y = 0
ilya.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/ilya.jpg')), (260, 230))
ilya.rect = ilya.image.get_rect()
ilya.rect.x = 530
ilya.rect.y = 0
todd.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/todd.jpg')), (800, 250))
todd.rect = todd.image.get_rect()
todd.rect.x = 0
todd.rect.y = 350
all_sprites.add(todd)
Cat((alex, kirill, ilya), image, 1, 2, -150, 250)
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
