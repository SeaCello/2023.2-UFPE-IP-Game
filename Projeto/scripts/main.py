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

person_img = pygame.image.load('Projeto/assets/character.png')
person = player()

WIDTH = 1260
HEIGHT = 720
AMARELO = (255,255,0)
PRETO = (0,0,0)
VELOCIDADE = 10

LARGURA_BLOCO = 800//20 #40 largura
ALTURA_BLOCO = 600//20 #30 altura

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    dt = clock.tick(60) / 100

    person.movimenta(dt)

    screen.blit(fundo_img, (0, 0))

    for c in range(0, 64, 16):
        left = load_crop_image(person_img, c, 96, 16, 32, False)
        left = pygame.transform.scale(left, (48,96))

    screen.blit(left, (person.player_posx, person.player_posy))

pygame.quit()