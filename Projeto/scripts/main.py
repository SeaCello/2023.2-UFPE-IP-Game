import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from default import *
from nico import Player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)
rect_heroi = heroi.rect

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_img, (0, 0))

    dt = clock.tick(60) / 1000

    # screen.blit(personagem, (heroi.player_posx, heroi.player_posy))

    # heroi.processar_evento(dt)

    grupo_heroi.update()

    heroi.movimenta(dt)

    grupo_heroi.draw(screen)

    pygame.display.flip()

pygame.quit()