class player():
    def __init__(self):
        self.jumpSpeed = 2
        self.life = 1

nico = player()
print(nico)

# Renderizar sprite
# Criar máscara de colisão 
# Criar código de movimento do Player (fazer pulo referenciando jumpSpeed)
# Referência
# keys = pygame.key.get_pressed()
    # if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        # player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
        # player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
        # player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
        # player_pos.x += 300 * dt

