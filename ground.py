import pygame
from pygame import Vector2, Rect


class Ground(object):
    def __init__(self):
        self.platforms = [
            Rect(0, 700, 500, 20),
            Rect(210, 300, 200, 100),
            Rect(550, 500, 200, 100),
            Rect(550, 200, 200, 100),
            Rect(550, 700, 100, 20),
            Rect(1000, 700, 100, 20),
            Rect(0, 0, 10, 720)]
        self.color = (0, 155, 0)

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, self.color, Rect(
                platform.x,
                platform.y,
                platform.width,
                platform.height))

