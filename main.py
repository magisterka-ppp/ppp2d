# Zaimportowanie modułu pygame
import pygame


# inicjalizacja stałych dla szerokości i wysokości ekranu
from constants import QUIT, KEYDOWN, K_ESCAPE

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from player import Player


# Inicjalizacja pygame
pygame.init()

# Utworzenie obiektu 'screen'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Stworzenie niestandardowego wydarzenia w celu dodania nowego wroga
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instancja klasy Player - player. Prostokąt
player = Player()

# Stwórz grupy aby utrzymywać wrogie duchy i wszystkie duchy
# - 'enemies': używane są do wykrywania kolizji i aktualizowania pozycji
# - 'all_sprites' wykorzystywana do renderowania
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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

        # Dodanie nowego wroga?
        elif event.type == ADDENEMY:
            # Stworzenie nowego wroga i dodanie go do grupy 'all_sprites'
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    # Pobierz wszystkie aktualne wciśnięte klawisze
    pressed_keys = pygame.key.get_pressed()
    # Odśwież położenie gracza bazująć na kliknięcich klawiszy użytkownika
    player.update(pressed_keys)

    # Aktualizacja pozycji wroga
    enemies.update()

    # Wypełnienie tła kolorem czarnym
    screen.fill((0, 0, 0))

    # Rysowanie wszystkich wrogów
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Sprawdź czy którykolwiek z wrogów zderzył się z graczem
    if pygame.sprite.spritecollideany(player, enemies):
        # Jeśli tak, usuń gracza i zatrzymaj pętle
        player.kill()
        running = False

    # Narysuj player'a na ekranie
    #screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # rysowanie obiektu w lewym qórnym rogu
    screen.blit(player.surf, player.rect)

    # Odśwież widok
    pygame.display.flip()




