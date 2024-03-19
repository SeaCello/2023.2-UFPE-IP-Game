#importando pygame e livraria necessaria
import pygame
from pygame.locals import *
import threading
import time

pygame.init()

#inicializando variáveis
clock = pygame.time.Clock()
width_screen = 1280
width = 1050
height = 200
cont = []
bullet_scale = 1.4
bullet_speed = 10
bullet_lifetime = 500
shoot = False

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
        self.speed = 10
        self.life = 2
        self.arrow_cooldown = 0
        self.x_change = x_change
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
        self.image_atual = []
        self.shoot_cooldown = 900
        self.last = 0

        for c in range(0, 256, 64):
            left = load_crop_image(enemy_img, c, 96, 64, 64, False)
            left = pygame.transform.scale(left, (48,96))
            self.images_left.append(left)
            
            up = load_crop_image(enemy_img, c, 64, 64, 64, False)
            up = pygame.transform.scale(up, (48,96))
            self.images_up.append(up)
            
            if c <= 128:
                right = load_crop_image(enemy_img, c, 64, 64, 64, False)
                right = pygame.transform.scale(right, (96,128))
                self.images_right.append(right)
            
            down = load_crop_image(enemy_img, c, 0, 64, 64, False)
            down = pygame.transform.scale(down, (96,128))
            self.images_down.append(down)

        self.i = 0
        self.image_atual = self.images_down
        self.image = self.image_atual[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.topleft = (x, y)
    
    def update(self, grupo_bullet, arrows):
        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
            self.image = self.images_down[int(self.i)]
        elif self.i >= len(self.images_right):
            self.i = 0
            self.image = self.images_right[int(self.i)]

        self.image = self.image_atual[int(self.i)]

        self.image = self.image_atual[int(self.i)]

        collided = pygame.sprite.spritecollideany(self, arrows)

        if collided:
            self.life -= 1
            collided.kill()
        
        if self.life <= 0:
            self.kill()

        x = threading.Thread(target=self.movement, args=(grupo_bullet,))
        x.start()

        if self.arrow_cooldown > 0:
            self.arrow_cooldown -= 1
    
    # Definir movimento do inimigo
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
            self.image_atual = self.images_down
            time.sleep(1.5)
        elif x == 100 :
            self.image_atual = self.images_right
            time.sleep(1.5)
        elif (self.rect.x > 105) and (self.rect.x < 995) :
            now = pygame.time.get_ticks()
            if now - self.last >= self.shoot_cooldown:
                self.shootBullets(grupo_bullet)
                self.last = now

        x += x_change

        self.rect.x = x
        self.x_change = x_change

    def shootBullets(self, grupo_bullet):
        if self.x_change == 5:
            grupo_bullet.add(enemyShot(self.rect.centerx, self.rect.centery))
        elif self.x_change == -5:
            grupo_bullet.add(enemyShot(self.rect.centerx, self.rect.centery))


enemy_bullet_image = pygame.image.load('Projeto/assets/bullet.png')
class enemyShot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = enemy_bullet_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.x_vel = 0
        self.y_vel = 0
        self.speed = 10
    
    def update(self, boxes):
        self.rect.move_ip([0, self.speed])

        if pygame.sprite.spritecollideany(self, boxes):
            self.kill()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
