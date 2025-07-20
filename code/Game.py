import pygame

from code.Const import TEL_HEIGHT, TEL_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size = (TEL_WIDTH, TEL_HEIGHT))

    def run(self):
        while (True):
            menu = Menu(self.tela)
            menu.run()
            pass
            