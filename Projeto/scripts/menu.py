import pygame, sys
from button import Button

class menu():
    def __init__(self):
        pygame.init()
   
        pygame.mixer.music.load('Projeto/assets/Música fase mais ou menos.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
 
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
 
        self.fundo_menu = pygame.image.load("Projeto/assets/Background.jpg")
 
    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Projeto/assets/font.ttf", size)
 
    def play(self):
        from main import game
        pygame.display.flip()
        jornada = game()
        jornada.play()
 
    def options(self):
        while True:
            options_mouse_pos = pygame.mouse.get_pos()
 
            self.screen.fill("purple")
 
            title_credits = self.get_font(45).render("Créditos:", True, "Red")
            title_rect = title_credits.get_rect(center=(640, 100))
 
            person1 = self.get_font(20).render("Aline Acioly", True, "Black")
            person1_rect = person1.get_rect(center=(640, 240))
 
            person2 = self.get_font(20).render("Guilherme Rigaud", True, "Black")
            person2_rect = person2.get_rect(center=(640, 290))
 
            person3 = self.get_font(20).render("Heitor Felipe", True, "Black")
            person3_rect = person3.get_rect(center=(640, 340))
 
            person4 = self.get_font(20).render("João Guilherme Ohashi", True, "Black")
            person4_rect = person4.get_rect(center=(640, 390))
 
            person5 = self.get_font(20).render("Marcello Menezes", True, "Black")
            person5_rect = person5.get_rect(center=(640, 440))
 
            person6 = self.get_font(20).render("Tiago Quaresma", True, "Black")
            person6_rect = person6.get_rect(center=(640, 490))
 
            self.screen.blit(title_credits, title_rect)
 
            self.screen.blit(person1, person1_rect)
            self.screen.blit(person2, person2_rect)
            self.screen.blit(person3, person3_rect)
            self.screen.blit(person4, person4_rect)
            self.screen.blit(person5, person5_rect)
            self.screen.blit(person6, person6_rect)
 
            options_back = Button(pos=(640, 590), 
                                text_input="BACK", font=self.get_font(60), base_color="Black", hovering_color="lightblue")
 
            options_back.changeColor(options_mouse_pos)
            options_back.update(self.screen)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(options_mouse_pos):
                        self.main_menu()
 
            pygame.display.flip()
 
    def main_menu(self):
        running = True
 
        while running:
            self.screen.blit(self.fundo_menu, (0, 0))
 
            menu_mouse_pos = pygame.mouse.get_pos()
 
            menu_text = self.get_font(50).render("Uma Jornada Discreta", True, "#e4de20")
            menu_rect = menu_text.get_rect(center=(640, 100))
 
            play_button = Button(pos=(640, 250),
                                text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            options_button = Button(  pos=(640, 400), 
                                text_input="CRÉDITOS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(  pos=(640, 550), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
 
            self.screen.blit(menu_text, menu_rect)
 
            for button in [play_button, options_button, quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.screen)
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        running = False
                        self.play()
                    if options_button.checkForInput(menu_mouse_pos):
                        self.options()
                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
 
            if running:
                pygame.display.flip()
 
menu().main_menu()
