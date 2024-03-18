import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from default import *
from nico import *
import level
from level import *
from enemy import *
from item import *

# pygame setup
pygame.init()
font = pygame.font.Font("Projeto/assets/font.ttf", 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)

enemy = Base_enemy(WIDTH, 100, 0)
enemy2 = Base_enemy(WIDTH, 300, 0)
grupo_enemies = pygame.sprite.Group()
grupo_enemies.add(enemy)

bullet = Bullet(1000, 70, 45)
grupo_bullet = pygame.sprite.Group()
grupo_bullet.add(bullet)

arrow = arrowShot(1280, 720)
grupo_arrows = pygame.sprite.Group()
grupo_arrows.add(arrow)

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

class game():

    def __init__(self):
        self.running = True

    def play(self):
        pygame.init()
        
        pygame.display.set_caption("Uma Jornada Discreta")

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            screen.blit(fundo_img, (0, 0))
            
            blocks.update()
            blocks.draw(screen)
            
            life.update()
            life.draw(screen)

            arrows.update()
            arrows.draw(screen)

            powerups.update()
            powerups.draw(screen)
            
            grupo_arrows.update()
            grupo_arrows.draw(screen)
            
            grupo_heroi.update(blocks, life, arrows, powerups, grupo_arrows)
            grupo_heroi.draw(screen)

            grupo_enemies.update(grupo_bullet, grupo_arrows)
            grupo_enemies.draw(screen)

            grupo_bullet.update()
            grupo_bullet.draw(screen)

            textLife = font.render("Vida: " + str(heroi.life), 1, (0,0,0))
            textArrows = font.render("Flechas: " + str(heroi.arrows), 1, (0,0,0))
            screen.blit(textLife, (10, 10))
            screen.blit(textArrows, (10, 40))

            pygame.display.flip()

        pygame.quit()