import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, TEL_WIDTH

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while(True):
            self.tela.blit(source=self.surf, dest=self.rect)
            # de 50 pra 70
            self.menu_text(70, "Mountain", COLOR_ORANGE, ((TEL_WIDTH/2), 70))
            self.menu_text(70, "Shooter", COLOR_ORANGE, ((TEL_WIDTH/2), 120))

            for i in range(len(MENU_OPTION)):
                # de 20 pra 30
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((TEL_WIDTH/2), 200 + 25 * i))
            
            pygame.display.flip()

            #checando todos os eventos
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit() #fechar janela
                    quit() #fechar pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.tela.blit(source=text_surf, dest=text_rect)