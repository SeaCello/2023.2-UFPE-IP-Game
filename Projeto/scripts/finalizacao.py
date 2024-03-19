import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ending")

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definindo background

background_image = pygame.image.load("Projeto/assets/Background.jpg").convert()

# Carregando a fonte
def get_font(size):
    return pygame.font.Font("Projeto/assets/font.ttf",size)
font = get_font(32)
font_parabens = get_font(48)

def ending_screen():
    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))

    text1 = font_parabens.render("Parabéns!!", True, WHITE)
    text2 = font.render("Você completou o desafio e se tornou", True, WHITE)
    text3 = font.render("mestre discreto.", True, WHITE)

    text1_rect = text1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    text2_rect = text2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    text3_rect = text3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))

    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)

    pygame.display.flip()

# Loop principal
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        ending_screen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
