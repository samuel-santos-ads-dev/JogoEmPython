import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW, MENU_OPTION, TEL_WIDTH

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while(True):
            # desenha as imagens(fundo, texto)
            self.tela.blit(source=self.surf, dest=self.rect)
            # de 50 pra 70
            self.menu_text(70, "Mountain", COLOR_ORANGE, ((TEL_WIDTH/2), 70))
            self.menu_text(70, "Shooter", COLOR_ORANGE, ((TEL_WIDTH/2), 120))

            for i in range(len(MENU_OPTION)):
                # de 20 pra 30
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], COLOR_YELLOW, ((TEL_WIDTH/2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((TEL_WIDTH/2), 200 + 25 * i))
            pygame.display.flip()

            #checando todos os eventos
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit() #fechar janela
                    quit() #fechar pygame
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_DOWN): # tecla para baixo
                        if(menu_option < len(MENU_OPTION) - 1):
                            menu_option += 1
                        else:
                            menu_option = 0
                    if(event.key == pygame.K_UP): # tecla pra cima
                        if(menu_option > 0):
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if(event.key == pygame.K_RETURN): # tecla enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf, dest=text_rect)