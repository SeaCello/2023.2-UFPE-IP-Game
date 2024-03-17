import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'



import pygame
from default import *
from nico import Player
import level
from level import Platform
from enemy import *
from item import *

# pygame setup
pygame.init()
font = pygame.font.SysFont("arial", 30, True)
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

bullet = Bullet(500, 70, 45)
grupo_bullet = pygame.sprite.Group()
grupo_bullet.add(bullet)

blocks = pygame.sprite.Group()
levelMap = level.levelDesign

life = pygame.sprite.Group()
arrows = pygame.sprite.Group()
powerups = pygame.sprite.Group()

all_sprites_group = pygame.sprite.Group()

for blockY in range(len(levelMap)):
        for blockX in range(len(levelMap[blockY])):
            if(levelMap[blockY][blockX] == 1):            
                blocks.add(Platform(blockX*32+16, blockY*32+16))
            elif(levelMap[blockY][blockX] == 2):
                life.add(Life(blockX*32+16, blockY*32+16))
            elif(levelMap[blockY][blockX] == 3):
                arrows.add(Arrow(blockX*32+16, blockY*32+16))
            elif(levelMap[blockY][blockX] == 4):
                powerups.add(Powerup(blockX*32+16, blockY*32+16))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(fundo_img, (0, 0))
    
    blocks.update()
    blocks.draw(screen)
    
    life.update()
    life.draw(screen)

    arrows.update()
    arrows.draw(screen)

    powerups.update()
    powerups.draw(screen)
    
    grupo_bullet.update()
    grupo_bullet.draw(screen)
    
    grupo_heroi.update(blocks, life, arrows, powerups)
    grupo_heroi.draw(screen)

    grupo_enemies.update(heroi.rect, grupo_bullet)
    grupo_enemies.draw(screen)            

    textLife = font.render("Vida: " + str(heroi.life), 1, (0,0,0))
    textArrows = font.render("Flechas: " + str(heroi.arrows), 1, (0,0,0))
    screen.blit(textLife, (0, 10))
    screen.blit(textArrows, (0, 40))

    pygame.display.flip()

pygame.quit()