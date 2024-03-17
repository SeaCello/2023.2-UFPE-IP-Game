# Criar classe de inimigo
# Inicializar valores
# Renderizar sprite
# Definir máscara de colisão
# Definir poder de cada item e jogar em nico.py
import pygame

class Life():
    def __init__(self, posX, posY):
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("2023.2-UFPE-IP-Game/Projeto/assets/platform_temp.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.life = 1
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Arrow():
    def __init__(self, posX, posY):
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("2023.2-UFPE-IP-Game/Projeto/assets/platform_temp.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.life = 1
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Powerup():
    def __init__(self, posX, posY):
        self.width = 32
        self.height = 32
        self.image = pygame.image.load("2023.2-UFPE-IP-Game/Projeto/assets/platform_temp.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.life = 1
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)