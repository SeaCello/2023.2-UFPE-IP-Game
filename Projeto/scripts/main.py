import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from default import *
from nico import Player
import level
from level import Platform, Ground

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)

blocks = pygame.sprite.Group()
levelMap = level.levelDesign

blocks.add(Ground(0, 600))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_img, (0, 0))

    for blockY in range(len(levelMap)):
        for blockX in range(len(levelMap[blockY])):
            if(levelMap[blockY][blockX] == 1):            
                blocks.add(Platform(blockX*32+300, blockY*32+500))
    
    blocks.draw(screen)

    # pygame.draw.rect(screen, (255, 255, 255), rect_obst)

    dt = clock.tick(60) / 1000

    # screen.blit(personagem, (heroi.player_posx, heroi.player_posy))

    # heroi.processar_evento(dt)

    grupo_heroi.update(blocks)

    grupo_heroi.draw(screen)

    pygame.display.flip()

pygame.quit()