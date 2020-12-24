# zaimportowanie klasy random dla generowania losowych liczb
import random
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Zdefiniowanie obiektu enemy rozszerzającej pygame.sprite.Sprite
# Powierzchnia narysowana na ekranie jest teraz atybutem klasy 'Enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = random.randint(5, 20)

    # Poruszaj wrogiem bazując na prędkości
    # Usuń wroga, kiedy osiągnie lewą stronę krawędzi ekranu
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()