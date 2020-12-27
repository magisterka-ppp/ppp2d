# Klasa 'Player' do obsługi działań gracza

# Zaimportowanie biblioteki pygame
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL

pygame.mixer.init()
# Załaduj wszystkie pliki dźwiękowe
# Źródła dźwięków: Jon Fincher
move_up_sound = pygame.mixer.Sound("./sound_effects/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("./sound_effects/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("./sound_effects/Collision.ogg")

# Zdefiniowanie klasy Player obiektu rozszerzonego przez pygame.sprite.Sprite
# Powierzchnia narysowana na ekranie jest atrybutem obiektu 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./graphics/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Przenieś gracza bazując na kliknięciach klawiszy użytkownika
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
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