#importando pygame e livraria necessaria
import pygame
from pygame.locals import *
from default import *
import threading
import time
import math
import random

pygame.init()

#inicializando variáveis
clock = pygame.time.Clock()
width_screen = 1280
width = 1050
height = 200
cont = []
shoot_cooldown = 5
bullet_scale = 1.4
bullet_speed = 10
bullet_lifetime = 500

# Criar classe de inimigo
enemy_img = pygame.image.load('Projeto/assets/R-Sheet-Sheet.png')
bullet_image = pygame.image.load('Projeto/assets/bullet.png')
bullet_image = pygame.transform.rotozoom(bullet_image, 0, bullet_scale)

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

class Base_enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, x_change):
        #renderizando sprite
        pygame.sprite.Sprite.__init__(self)
        self.life = 2
        self.shoot_cooldown = 0

        #Variável que muda a direção do movimento da coruja
        self.x_change = x_change

        self.images_left = []
        self.images_right = []

        self.image_atual = []

        for c in range(0, 256, 64):
            if c <= 128:
                right = load_crop_image(enemy_img, c, 64, 64, 64, False)
                right = pygame.transform.scale(right, (96,128))
                self.images_right.append(right)
            
            left = load_crop_image(enemy_img, c, 0, 64, 64, False)
            left = pygame.transform.scale(left, (96,128))
            self.images_left.append(left)

        self.i = 0
        self.image_atual = self.images_left
        self.image = self.image_atual[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = y
        self.rect.topleft = (x, y)
    
    def update(self, grupo_bullet, arrows):
        self.i += 0.20
        if self.i >= len(self.images_left):
            self.i = 0
            self.image = self.images_left[int(self.i)]
        elif self.i >= len(self.images_right):
            self.i = 0
            self.image = self.images_right[int(self.i)]

        self.image = self.image_atual[int(self.i)]

        collided = pygame.sprite.spritecollideany(self, arrows)

        if collided:
            self.life -= 1
            collided.kill()
        
        if self.life <= 0:
            self.kill()

        x = threading.Thread(target=self.movement, args=(grupo_bullet,))
        x.start()

        # self.colisao(arrows)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    # Definir moviment
    def movement(self, grupo_bullet):
        x = self.rect.x
        x_change = self.x_change

        if x <= 100:
            x_change = 5
        elif x >= 1000:
            x_change = -5

        if (x == 1000) and (len(cont) == 0):
            cont.append(1)
        elif (x == 1000) and (len(cont) > 0):
            self.image_atual = self.images_left
            time.sleep(2)
        elif x == 100 :
            self.image_atual = self.images_right
            time.sleep(2)

        x += x_change

        self.rect.x = x
        self.x_change = x_change

    #definindo colisao
    # def colisao(self, arrows):
    #     collided = pygame.sprite.spritecollideany(self, arrows)

    #     if collided:
    #         self.life -= 1
    #         time.sleep(1)

    #     return collided
    
    # #Função que realiza o tiro da coruja com base na sua posição e na do personagem
    # def shoot(self, person_rect):
    #     cateto_x = abs(self.rect.x - person_rect.x)
    #     cateto_y = abs(self.rect.y - person_rect.y)
    #     if cateto_x != 0:
    #         tangente = cateto_y / cateto_x
    #         angle = math.atan(tangente)*360/math.pi
    #     else:
    #         angle = 0
    #     angle += random.randrange(-10, 10)
    #     self.municao = 2
    #     return angle


#definindo classe do tiro da coruja 
bullet_image = pygame.image.load('Projeto/assets/bullet.png')
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.angle = angle
        self.image = bullet_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 5


    def bullet_movement(self):
        
        self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
        self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed


    def update(self):
        self.bullet_movement()

        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Criar classe de inimigo
# Inicializar valores
# Renderizar sprite
# Definir máscara de colisão
# Definir movimento