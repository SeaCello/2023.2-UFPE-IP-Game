import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from default import *
from nico import *
import level
from level import *
from enemy import *
from item import *
from loser import *
from winner import *

# pygame setup
# pygame.init()
font = pygame.font.Font("Projeto/assets/font.ttf", 30)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
fundo_img = pygame.image.load('Projeto/assets/imagem_de_fundo.jpg')

heroi = Player()
grupo_heroi = pygame.sprite.Group(heroi)

enemy = Base_enemy(WIDTH, 200, 0)
enemy2 = Base_enemy(WIDTH, 400, 0)
grupo_enemies = pygame.sprite.Group()
grupo_enemies.add(enemy)
grupo_enemies.add(enemy2)

grupo_bullet = pygame.sprite.Group()

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
        pygame.mixer.pause()
        pygame.mixer.music.load('Projeto/assets/Música fase 1.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        
        pygame.display.set_caption("Uma Jornada Discreta")

        last = 0
        cooldown = 20000

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif heroi.life <= 0:
                    final()
                elif len(grupo_enemies) == 0:
                    main()
            
            screen.blit(fundo_img, (0, 0))
            
            blocks.update()
            blocks.draw(screen)
            
            life.update(blocks)
            life.draw(screen)

            arrows.update(blocks)
            arrows.draw(screen)

            powerups.update(blocks)
            powerups.draw(screen)

            grupo_bullet.update(blocks)
            grupo_bullet.draw(screen)
            
            grupo_arrows.update(blocks)
            grupo_arrows.draw(screen)
            
            grupo_heroi.update(blocks, life, arrows, powerups, grupo_arrows, grupo_bullet, grupo_enemies)
            grupo_heroi.draw(screen)

            grupo_enemies.update(grupo_bullet, grupo_arrows)
            grupo_enemies.draw(screen)

            textLife = font.render("Vida: " + str(heroi.life), 1, (0,0,0))
            textArrows = font.render("Flechas: " + str(heroi.arrows), 1, (0,0,0))
            screen.blit(textLife, (10, 10))
            screen.blit(textArrows, (10, 40))

            now = pygame.time.get_ticks()
            if now - last >= cooldown:
                last = now
                picked = random.randint(1,3)
                if picked == 1:
                    life.add(Life(100, 100))
                elif picked == 2:
                    arrows.add(Arrow(100, 100))
                elif picked == 3:
                    powerups.add(Powerup(100,100))

            pygame.display.flip()

        pygame.quit()