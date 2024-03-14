import pygame

from pygame.locals import *

from default import *

from math import *

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

        self.jumpSpeed = 2
        self.life = 1
        self.on_move = False

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
        self.pos_y_inicial = 100 - 64 - 96//2
        self.rect.topleft = (100, 500) #368   416(centro y)
    
    def colisao(self, retangulo):

        x_retangulo = retangulo.x
        x_person = self.rect.x
        y_retangulo = retangulo.y
        y_person = self.rect.y

        # distanciax = x_retangulo - x_person

        # if distanciax <= 0:
        #     self.rect.x = x_retangulo
        #     self.vel_x = 0
        # elif distanciax <= (x_retangulo - retangulo.width):
        #     self.rect.x = (x_retangulo - retangulo.width)

        distanciay = y_retangulo - y_person

        if distanciay <= 0:
            self.rect.y = y_retangulo
        elif distanciay <= (y_retangulo - retangulo.height):
            self.rect.y = (y_retangulo - retangulo.height - 32)



    def update(self):   

        dt = clock.tick(60) / 1000

        self.i += 0.20
        if self.i >= len(self.images_down):
            self.i = 0
        self.image = self.image_atual[int(self.i)]

        self.movimenta(dt)

        #Gravidade
        if self.vel_y < 10:
            self.vel_y += 1
            self.rect.y += self.vel_y

        if self.on_move:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y
        
        if self.rect.y == 568:
            self.on_move = False

    def movimenta(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.vel_y = -7
            self.image_atual = self.images_jump_right
            self.on_move = True
        elif keys[pygame.K_a]:
            self.vel_x = -10
            self.image_atual = self.images_left
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > WIDTH - 32:
                self.rect.x = WIDTH - 32
            self.on_move = True
        elif keys[pygame.K_d]:
            self.vel_x = 10
            self.image_atual = self.images_right
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > WIDTH - 32:
                self.rect.x = WIDTH - 32
            self.on_move = True
        else:
            self.image_atual = self.images_down

# Renderizar sprite
# Criar máscara de colisão 
# Criar código de movimento do Player (fazer pulo referenciando jumpSpeed)
# Referência
