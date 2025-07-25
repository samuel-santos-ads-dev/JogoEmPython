import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, tela, name, game_mode):
        self.tela = tela
        self.name = name
        self.game_mode = game_mode 
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while(True):
            for ent in self.entity_list:
                self.tela.blit(source = ent.surf, dest = ent.rect)
                ent.move()
            pygame.display.flip()
        pass