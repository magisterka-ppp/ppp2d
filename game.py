import pygame

from ground import Ground
from player import Player


class Game(object):

    def __init__(self):
        pygame.init()
        self.ground = Ground()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.player = Player()

    def logicLoop(self):
        self.player.logic(self)

    def drawLoop(self):
        self.screen.fill(0)
        self.player.draw(self.screen)
        self.ground.draw(self.screen)
        pygame.display.flip()

