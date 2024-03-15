import pygame

levelDesign = [[0,0,1],[1,0,0],[0,1,0],[1, 1, 1]]

class Platform(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/platform_temp.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Ground(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super().__init__()
        self.width = 500
        self.height = 32
        self.image = pygame.image.load("Projeto/assets/ground_temp.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)