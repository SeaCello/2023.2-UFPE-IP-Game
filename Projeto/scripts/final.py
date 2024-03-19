import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

fundo_menu = pygame.image.load("Projeto/assets/Background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Projeto/assets/font.ttf", size)

def final():
    running = True

    while running:
        screen.blit(fundo_menu, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        title_mes = pygame.font.SysFont('rockwell', 40).render("Vanin te enviou uma mensagem:", True, "Red")
        title_rect = title_mes.get_rect(center=(640, 100))

        paragraph1 = pygame.font.SysFont('rockwell', 28).render("Cara, você tá achando que curso superior é fácil?", False, "#000000")
        paragraph1_rect = paragraph1.get_rect(center=(640, 300))

        paragraph2 = pygame.font.SysFont('rockwell', 28).render("Quer facilidade, volta pra o FUNDAMENTAL e seja feliz, porque aqui você só vai ter sofrimento!", False, "#000000")
        paragraph2_rect = paragraph2.get_rect(center=(640, 390))

        quit_button = Button(  pos=(640, 550), 
                            text_input="Sair e aceitar a Final de MD", font=get_font(30), base_color="#f4f4a6", hovering_color="Orange")

        screen.blit(title_mes, title_rect)
        screen.blit(paragraph1, paragraph1_rect)
        screen.blit(paragraph2, paragraph2_rect)

        for button in [quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        
        if running:
            pygame.display.flip()