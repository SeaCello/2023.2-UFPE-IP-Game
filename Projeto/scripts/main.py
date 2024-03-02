import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from nico import player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

person_img = pygame.image.load('Projeto/assets/test_person2.png')
person = player()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    person.movimenta(dt)

    screen.blit(fundo_img, (0, 0))
    screen.blit(person_img, (person.player_posx, person.player_posy))

pygame.quit()