import pygame, random

class Life(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/life.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.vel_y = 0
    
    def update(self, ground):
        collision = pygame.sprite.spritecollideany(self, ground)
        if self.vel_y < 10:
            self.vel_y += 1
        
        if collision and self.vel_y > 0 :
            self.vel_y = 0
        
        self.rect.move_ip([0,self.vel_y])
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Arrow(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/arrows.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.vel_y = 0
    
    def update(self, ground):

        collision = pygame.sprite.spritecollideany(self, ground)
        if self.vel_y < 10:
            self.vel_y += 1
        
        if collision and self.vel_y > 0 :
            self.vel_y = 0
        
        self.rect.move_ip([0,self.vel_y])
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Powerup(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/powerup.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.vel_y = 0
    
    def update(self, ground):
        collision = pygame.sprite.spritecollideany(self, ground)
        if self.vel_y < 10:
            self.vel_y += 1
        
        if collision and self.vel_y > 0 :
            self.vel_y = 0
        
        self.rect.move_ip([0,self.vel_y])
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)