# Zaimportowanie modułu pygame
import pygame

# Zaimportowanie pygame.locals do łatwiejszego dostępu przez koordynaty klawiszów
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# inicjalizacja stałych dla szerokości i wysokości ekranu
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Inicjalizacja pygame
pygame.init()

# Utworzenie obiektu 'screen'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instancja klasy Player - player.
player = Player()

# Zmienna utrzymująca program w działaniu
running = True

# Pętla główna
while running:

    # Obserwuj każdy element w kolejece zdarzeń
    for event in pygame.event.get():
        # Czy użytkownik nacisnął przycisk?
        if event.type == KEYDOWN:
            # Czy został naciśnięty klawisz Escape? Jeśli tak, zatrzymaj pętle.
            if event.key == K_ESCAPE:
                running = False

        # Czy użytkownik nacisnął przycisk wyjścia? Jeśli tak, zatrzymaj pętle.
        elif event.type == QUIT:
            running = False

    # Wypełnienie tła kolorem czarnym
    screen.fill((0, 0, 0))

    # Narysuj player'a na ekranie
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # rysowanie obiektu w lewym qórnym rogu
    # screen.blit(player.surf, player.rect)

    # Odśwież widok
    pygame.display.flip()




