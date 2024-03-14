import pygame
import level
from level import Platform



# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
blocks = pygame.sprite.Group()
levelMap = level.levelDesign

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for blockY in range(len(levelMap)):
        for blockX in range(len(levelMap[blockY])):
            if(levelMap[blockY][blockX] == 1):            
                blocks.add(Platform(blockX*32+16, blockY*32+16))
    blocks.draw(screen)
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()