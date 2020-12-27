import random

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, RLEACCEL
# Zdefiniowanie obiektu chmury rozszerzając klase pygame.sprite.Sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("./graphics/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # Pozycja startowa jest generowana losowo
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Poruszaj chmurą bazując na stałej prędkości
    # Usuń chmurę, jęśli przekroczy lewą krawędź okna gry
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
