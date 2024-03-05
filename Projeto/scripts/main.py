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

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)
personagem = pygame.image.load('Projeto/assets/character.png') 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fundo_img, (0, 0))

    dt = clock.tick(60) / 100

    # screen.blit(personagem, (heroi.player_posx, heroi.player_posy))

    # heroi.processar_evento(dt)

    grupo_heroi.update()
    heroi.movimenta()
    grupo_heroi.draw(screen)

    pygame.display.flip()

pygame.quit()