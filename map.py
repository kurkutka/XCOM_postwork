import pygame
import os
import random


class Map:
    def __init__(self, what_a_maps):
        self.play_btn = pygame.sprite.Group()
        btn = pygame.sprite.Sprite()
        btn.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/btn.png')), (70, 70))
        btn.rect = btn.image.get_rect()
        btn.rect.x = what_a_maps[0][0]
        btn.rect.y = what_a_maps[0][1]
        btn1 = pygame.sprite.Sprite()
        btn1.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/btn.png')), (70, 70))
        btn1.rect = btn1.image.get_rect()
        btn1.rect.x = what_a_maps[1][0]
        btn1.rect.y = what_a_maps[1][1]
        self.play_btn.add(btn)
        self.play_btn.add(btn1)

    def update(self):
        self.play_btn.draw(screen)


pygame.init()
pygame.mixer.music.load('data/sounds/menu music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
FPS = 5
map = pygame.sprite.Group()
bg = pygame.sprite.Sprite()
bg.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/map.jpg')), (800, 600))
bg.rect = bg.image.get_rect()
bg.rect.x = bg.rect.y = 0
map.add(bg)
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
running = True
x = random.choices([(90, 170), (220, 450), (400, 120), (450, 500), (700, 200)], k=2)
Map(x)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color('black'))
    map.draw(screen)
    Map.update(Map(x))
    pygame.display.flip()
    clock.tick(FPS)
