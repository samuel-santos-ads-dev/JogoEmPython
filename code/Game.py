import pygame

from code.Const import MENU_OPTION, TEL_HEIGHT, TEL_WIDTH
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode(size = (TEL_WIDTH, TEL_HEIGHT))

    def run(self):
        while (True):
            menu = Menu(self.tela)
            menu_return = menu.run()
            
            if(menu_return in MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]):
                player_score = [0, 0] #[Player1, Player2]
                level = Level(self.tela, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if(level_return):
                    level = Level(self.tela, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif(menu_return == MENU_OPTION[4]):
                pygame.quit() #fechar janela
                quit() #fechar pygame
                
            else:
                pass