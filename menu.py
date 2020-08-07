import pygame
import os
import cat


class Text:
    def update(self):
        screen.blit(text, (0, 0))


pygame.mixer.music.load('data/sounds/Menu.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()
FPS = 5
text = pygame.font.SysFont(None, 72).render('XCOM     click to continue', True, pygame.Color('purple'))
all_sprites = pygame.sprite.Group()
bg = pygame.sprite.Sprite()
bg.image = pygame.transform.scale(pygame.image.load(os.path.join('data/Текстуры/background.jpg')), (800, 600))
bg.rect = bg.image.get_rect()
bg.rect.x = 0
bg.rect.y = 0
all_sprites.add(bg)
clock = pygame.time.Clock()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
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
pygame.quit()
