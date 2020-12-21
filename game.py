import pygame

from ground import Ground
from player import Player
from pygame.math import Vector2

screenWidth = 1280
screenHeight = 720

class Game(object):
    def __init__(self):
        pygame.init()
        self.camera = Vector2(400, 0)
        self.ground = Ground()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.player = Player()

    def logicLoop(self):
        self.camera_control()
        self.player.logic(self)


    def camera_control(self):
        lerp = 0.1
        self.camera.x += (self.player.bounds.x - screenWidth/2 - self.camera.x) * lerp
        self.camera.y += (self.player.bounds.y - screenHeight/2 - self.camera.y) * lerp



    def drawLoop(self):
        self.screen.fill(0)
        self.player.draw(self.screen, self.camera)
        self.ground.draw(self.screen, self.camera)
        pygame.display.flip()

