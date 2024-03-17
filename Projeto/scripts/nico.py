import time
import pygame

from pygame.locals import *

from default import *

from math import *

from item import *

pygame.init()

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

personagem = pygame.image.load('Projeto/assets/character.png')

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.jumpSpeed = 1200
        self.arrows = 0
        self.life = 3
        self.speed = 300
        self.vel_x = 0
        self.vel_y = 0
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
        self.images_jump_right = []
        self.image_atual = []

        for c in range(0, 64, 16):
            left = load_crop_image(personagem, c, 96, 16, 32, False)
            left = pygame.transform.scale(left, (48,96))
            self.images_left.append(left)
            
            up = load_crop_image(personagem, c, 64, 16, 32, False)
            up = pygame.transform.scale(up, (48,96))
            self.images_up.append(up)
            
            right = load_crop_image(personagem, c, 32, 16, 32, False)
            right = pygame.transform.scale(right, (48,96))
            self.images_right.append(right)
            
            down = load_crop_image(personagem, c, 0, 16, 32, False)
            down = pygame.transform.scale(down, (48,96))
            self.images_down.append(down)

        for i in range(0, 160, 16):
            jump_right = load_crop_image(personagem, i, 32, 16, 32, False)
            jump_right = pygame.transform.scale(jump_right, (48,96))
            self.images_jump_right.append(jump_right)

        self.i = 0
        self.image_atual = self.images_down
        self.image = self.images_down[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (100, 500)

    def update(self, boxes, life, arrows, powerups):

        dt = clock.tick(60) / 1000

        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.image_atual[int(self.i)]

        colidiu = pygame.sprite.spritecollideany(self, boxes)
        collisionLife = pygame.sprite.spritecollideany(self, life)
        collisionArrows = pygame.sprite.spritecollideany(self, arrows)
        collisionPowerups = pygame.sprite.spritecollideany(self, powerups)

        if collisionLife:
            self.life += 1
            collisionLife.kill()
        if collisionArrows:
            self.arrows += 1
            collisionArrows.kill()
        if collisionPowerups:
            collisionPowerups.kill()

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.vel_x = -self.speed*dt 
            self.image_atual = self.images_left
        elif key[pygame.K_d]:
            self.vel_x = self.speed*dt
            self.image_atual = self.images_right
        else:
            self.vel_x = 0
            self.image_atual = [self.images_down[0], self.images_down[0], self.images_down[0], self.images_down[0]]
        if key[pygame.K_SPACE] and colidiu:
            self.vel_y = -self.jumpSpeed*dt
            self.image_atual = self.images_jump_right
        else:
            self.image_atual = [self.images_down[0], self.images_down[0], self.images_down[0], self.images_down[0]]
        
        #Gravidade
        if self.vel_y < 10:
            self.vel_y += 1
        
        if colidiu and self.vel_y > 0 :
            self.vel_y = 0

        self.movimenta(self.vel_x,self.vel_y)

    def movimenta(self, x, y):  
        self.rect.move_ip([x,y])
        if self.rect.x < 0:
                self.rect.x = 0
        elif self.rect.x > WIDTH - 32:
                self.rect.x = WIDTH - 32
        
            

# Renderizar sprite
# Criar máscara de colisão 
# Criar código de movimento do Player (fazer pulo referenciando jumpSpeed)
# Referência
