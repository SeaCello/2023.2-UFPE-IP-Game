import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from default import *
from nico import Player
import level
from level import Platform, Ground
from enemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)

enemy = Base_enemy(WIDTH, 100, 0)
enemy2 = Base_enemy(WIDTH, 300, 0)
grupo_enemies = pygame.sprite.Group()
grupo_enemies.add(enemy)
# grupo_enemies.add(enemy2)

bullet = Bullet(500, 70, 45)
grupo_bullet = pygame.sprite.Group()
grupo_bullet.add(bullet)

blocks = pygame.sprite.Group()
levelMap = level.levelDesign

blocks.add(Ground(0, 720))
blocks.add(Ground(900, 720))
blocks.add(Platform(500, 500))
blocks.add(Platform(532, 500))

all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(blocks)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_img, (0, 0))

    all_sprites_group.update()
    all_sprites_group.draw(screen)

    grupo_bullet.update()
    grupo_bullet.draw(screen)
    
    grupo_heroi.update(all_sprites_group)
    grupo_heroi.draw(screen)

    grupo_enemies.update(heroi.rect, grupo_bullet)
    grupo_enemies.draw(screen)

    pygame.display.flip()

pygame.quit()