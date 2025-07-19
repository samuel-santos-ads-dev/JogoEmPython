import pygame

from code.Const import TEL_HEIGHT, TEL_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size = (TEL_WIDTH, TEL_HEIGHT))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while (True):
            menu = Menu(self.tela)
            menu.run()
            pass
            # #checando todos os eventos
            # for event in pygame.event.get():
            #     if(event.type == pygame.QUIT):
            #         pygame.quit() #fechar janela
            #         quit() #fechar pygame