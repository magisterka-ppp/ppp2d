# Klasa 'Player' do obsługi działań gracza

# Zaimportowanie biblioteki pygame
import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Zdefiniowanie klasy Player obiektu rozszerzonego przez pygame.sprite.Sprite
# Powierzchnia narysowana na ekranie jest atrybutem obiektu 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    # Przenieś gracza bazując na kliknięciach klawiszy użytkownika
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Utrzymuj położenie gracza w oknie
        if self.rect.left < 0:
            self.rect.left = 0;
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT