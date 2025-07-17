import pygame

from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size = (700, 480))

    def run(self):
        while (True):
            menu = Menu(self.tela)
            menu.run()
            pass
            # #checando todos os eventos
            # for event in pygame.event.get():
            #     if(event.type == pygame.QUIT):
            #         pygame.quit() #fechar janela
            #         quit() #fechar pygame