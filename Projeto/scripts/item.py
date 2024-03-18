import pygame

class Life(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/life.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
    
    def update(self):
        pass
    
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
    
    def update(self):
        pass
    
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
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)