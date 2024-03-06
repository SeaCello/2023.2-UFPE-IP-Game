import pygame

from pygame.locals import *

from default import *

pygame.init()

def load_crop_image(img, x, y, w, h, transform=True):
    img_original = img.subsurface((x,y),(w,h))
    if transform:
        img_scaled = pygame.transform.scale(img_original, (LARGURA_BLOCO, ALTURA_BLOCO))
        return img_scaled
    else:
        return img_original

personagem = pygame.image.load('Projeto/assets/character.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.jumpSpeed = 2
        self.life = 1

        self.vel_x = 0
        self.vel_y = 0
        self.images_down = []
        self.images_up = []
        self.images_left = []
        self.images_right = []
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
    
        self.i = 0
        self.image_atual = self.images_down
        self.image = self.images_down[self.i]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_inicial = 120 - 64 - 96//2
        self.rect.topleft = (100, 500) #368   416(centro y)

    def update(self):   
        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.image_atual[int(self.i)]

    def movimenta(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.vel_y = -dt
            self.vel_x = 0
            self.image_atual = self.images_up
            self.rect.x += 300 * self.vel_x
            self.rect.y += 300 * self.vel_y
        if keys[pygame.K_s]:
            self.vel_y = dt
            self.vel_x = 0
            self.image_atual = self.images_down
            self.rect.x += 300 * self.vel_x
            self.rect.y += 300 * self.vel_y
        if keys[pygame.K_a]:
            self.vel_x = -dt
            self.vel_y = 0
            self.image_atual = self.images_left
            self.rect.x += 300 * self.vel_x
            self.rect.y += 300 * self.vel_y
        if keys[pygame.K_d]:
            self.vel_x = dt
            self.vel_y = 0
            self.image_atual = self.images_right
            self.rect.x += 300 * self.vel_x
            self.rect.y += 300 * self.vel_y

# Renderizar sprite
# Criar máscara de colisão 
# Criar código de movimento do Player (fazer pulo referenciando jumpSpeed)
# Referência
