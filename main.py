# Zaimportowanie modułu pygame
import pygame


# inicjalizacja stałych dla szerokości i wysokości ekranu
from cloud import Cloud
from constants import QUIT, KEYDOWN, K_ESCAPE

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from player import Player, move_up_sound, move_down_sound, collision_sound

# Inicjalizacja dla dźwięków. Domyślne wartości są wystarczające.
pygame.mixer.init()
# Inicjalizacja czcionek
pygame.font.init()
# Inicjalizacja pygame
pygame.init()

# Stworzenie domyślnej czcionki
myfont = pygame.font.SysFont('Comic Sans MS', 40)

# Załaduj i odtwórz muzykę w tle
# Źródła dźwięków: http://ccmixter.org/files/Apoxode/59262
# Licencja: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load("./sound_effects/Apoxode_-_Electric_1.mp3")
pygame.mixer.music.play(loops=-1)

# Utworzenie obiektu 'screen'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Ustawienia zegara, aby generował odpowiednią liczbę klatek na sekundę
clock = pygame.time.Clock()

# Stworzenie niestandardowego wydarzenia w celu dodania nowego wroga
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Instancja klasy Player - player. Prostokąt
player = Player()

# Stwórz grupy aby utrzymywać przeszkody i chmury
# - 'enemies': używane są do wykrywania kolizji i aktualizowania pozycji
# - 'clouds': grupa wykorzystywana do aktualizacji pozycji
# - 'all_sprites' wykorzystywana do renderowania
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
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

        # Dodanie nowej przeszkody?
        elif event.type == ADDENEMY:
            # Stworzenie nowej przeszkody i dodanie jej do grupy 'all_sprites'
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Dodanie nowej chmury?
        elif event.type == ADDCLOUD:
            # Stworzenie nowej chmury i dodanie do grupy
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Pobierz wszystkie aktualne wciśnięte klawisze
    pressed_keys = pygame.key.get_pressed()
    # Odśwież położenie gracza bazująć na kliknięcich klawiszy użytkownika
    player.update(pressed_keys)

    # Aktualizacja pozycji przeszkód i chmur
    enemies.update()
    clouds.update()

    # Wypełnienie tła kolorem niebieskim
    screen.fill((135, 206, 250))

    # Rysowanie wszystkich przeszkód
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Sprawdź czy jaka kolwiek przeszkoda zderzyła się z graczem
    if pygame.sprite.spritecollideany(player, enemies):
        # Jeśli tak, usuń gracza i zatrzymaj pętle
        player.kill()

        text_gameover = myfont.render('Game over', False, (0, 0, 0))
        text_rect = text_gameover.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text_gameover, text_rect)
        # Zatrzymaj wszystkie odtwarzane dźwięki i odtwórz dźwięk kolizji
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()


        running = False

    # Narysuj player'a na ekranie
    #screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # rysowanie obiektu w lewym qórnym rogu
    screen.blit(player.surf, player.rect)

    # Odśwież widok
    pygame.display.flip()

    # Zapewnij odświeżanie programu na poziomie 60 klatek na sekundę
    clock.tick(60)

# Poczekaj 3 sekundy na zakończenie gry
pygame.time.delay(3000)
# Gra zakończona! Zatrzymaj i zamknij mixer
pygame.mixer.music.stop()
pygame.mixer.quit()




