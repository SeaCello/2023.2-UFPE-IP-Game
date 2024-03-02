import pygame

pygame.init()

class player():
    def __init__(self):
        self.jumpSpeed = 2
        self.life = 1
        self.player_posy = 400
        self.player_posx = 420

    def movimenta(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            self.player_posy -= 10 * dt
        if keys[pygame.K_s]:
            self.player_posy += 10 * dt
        if keys[pygame.K_a]:
            self.player_posx -= 10 * dt
        if keys[pygame.K_d]:
            self.player_posx += 10 * dt

# Renderizar sprite
# Criar máscara de colisão 
# Criar código de movimento do Player (fazer pulo referenciando jumpSpeed)
# Referência
