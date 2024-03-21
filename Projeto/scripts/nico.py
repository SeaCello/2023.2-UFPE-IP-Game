import time
import pygame
import numpy
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
        self.life = 20
        self.speed = 300
        self.vel_x = 0
        self.vel_y = 0
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
        self.images_jump_right = []
        self.image_atual = []
        self.cooldownArrow = 300 
        self.lastArrow = 0
        self.powered = False
        self.lastPower = 0
        self.cooldownPower = 5000
        self.jump_sound = pygame.mixer.Sound('Projeto/assets/SFX_Jump_02.wav')
        self.arrow_sound = pygame.mixer.Sound('Projeto/assets/Som de flechas.ogg')
        self.damage_sound = pygame.mixer.Sound('Projeto/assets/Som de dano.mp3')

        for c in range(0, 64, 16):
            left = load_crop_image(personagem, c, 96, 16, 20, False)
            left = pygame.transform.scale(left, (48, 72))
            self.images_left.append(left)
            
            up = load_crop_image(personagem, c, 64, 16, 20, False)
            up = pygame.transform.scale(up, (48,72))
            self.images_up.append(up)
            
            right = load_crop_image(personagem, c, 32, 16, 20, False)
            right = pygame.transform.scale(right, (48,72))
            self.images_right.append(right)
            
            down = load_crop_image(personagem, c, 0, 16, 20, False)
            down = pygame.transform.scale(down, (48,72))
            self.images_down.append(down)

        for i in range(0, 160, 16):
            jump_right = load_crop_image(personagem, i, 32, 16, 30, False)
            jump_right = pygame.transform.scale(jump_right, (48,96))
            self.images_jump_right.append(jump_right)

        self.i = 0
        self.image_atual = self.images_down
        self.image = self.images_down[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (100, 500)

    def update(self, boxes, life, arrows, powerups, grupo_arrows, grupo_bullet, grupo_enemies):

        dt = clock.tick(60) / 1000

        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.image_atual[int(self.i)]

        colidiu = self.check_ground_collision(0, 1, boxes)
        collisionLife = pygame.sprite.spritecollideany(self, life)
        collisionArrows = pygame.sprite.spritecollideany(self, arrows)
        collisionPowerups = pygame.sprite.spritecollideany(self, powerups)
        collisionBullets = pygame.sprite.spritecollideany(self, grupo_bullet)
        collisionEnemies = pygame.sprite.spritecollideany(self, grupo_enemies)

        if collisionLife:
            self.life += 1
            collisionLife.kill()
        if collisionArrows:
            self.arrows += 100
            collisionArrows.kill()
        if collisionPowerups:
            self.powered = True
            self.lastPower = pygame.time.get_ticks()
            collisionPowerups.kill()
        if collisionBullets or collisionEnemies:
            self.damage_sound.play(0)
            self.life -= 1
            if self.life <= 0:
                self.kill()
        
        if self.powered:
            nowPower = pygame.time.get_ticks()
            if nowPower - self.lastPower >= self.cooldownPower:
                self.last = nowPower
                self.powered = False

        key = pygame.key.get_pressed()

        if key[pygame.K_w] and colidiu:
            self.vel_y = -self.jumpSpeed*dt
            self.image_atual = self.images_jump_right
            self.jump_sound.play(0)
            self.jump_sound.set_volume(0.1)
        if key[pygame.K_SPACE] and self.arrows > 0:
            nowArrow = pygame.time.get_ticks()
            if nowArrow - self.lastArrow >= self.cooldownArrow:
                self.lastArrow = nowArrow
                self.arrows -= 1
                self.shootArrows(grupo_arrows)
                self.arrow_sound.play(0)
                self.arrow_sound.set_volume(0.3)
        if key[pygame.K_a]:
            self.vel_x = -self.speed*dt 
            self.image_atual = self.images_left
        elif key[pygame.K_d]:
            self.vel_x = self.speed*dt
            self.image_atual = self.images_right
        else:
            self.vel_x = 0
            self.image_atual = [self.images_down[0], self.images_down[0], self.images_down[0], self.images_down[0]]
        
        #Gravidade
        if self.vel_y < 10:
            self.vel_y += 1
        
        if colidiu and self.vel_y > 0 :
            self.vel_y = 0

        self.movimenta(self.vel_x, self.vel_y, boxes)
    
    def shootArrows(self, grupo_arrows):
        if self.powered:
            grupo_arrows.add(arrowShot(self.rect.x-32, self.rect.y))
            grupo_arrows.add(arrowShot(self.rect.x, self.rect.y))
            grupo_arrows.add(arrowShot(self.rect.x+32, self.rect.y))
        else:
            grupo_arrows.add(arrowShot(self.rect.x, self.rect.y))
            

    def check_ground_collision(self, x, y, boxes):
        self.rect.move_ip([x,y])
        collide = pygame.sprite.spritecollideany(self, boxes)
        self.rect.move_ip([-x,-y])
        return collide

    def movimenta(self, x, y, boxes):
        while self.check_ground_collision(0, y, boxes):
            y -= numpy.sign(y)  
        while self.check_ground_collision(x, y, boxes):
            x -= numpy.sign(x)
        self.rect.move_ip([x,y])
        if self.rect.x < 0:
                self.rect.x = 0
        elif self.rect.x > WIDTH - 32:
                self.rect.x = WIDTH - 32

arrowShotImage = pygame.image.load('Projeto/assets/arrowShot.png')
class arrowShot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = arrowShotImage
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 10
    
    def update(self, ground):
        self.rect.move_ip([0, -self.speed])
        collisionGround = pygame.sprite.spritecollideany(self, ground)
        if collisionGround:
            self.kill()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

