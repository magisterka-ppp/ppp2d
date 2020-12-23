# Prosty program pygame
import pygame
pygame.init()

# Ustaw okno do rysowania zawartosci gry
screen = pygame.display.set_mode([500, 500])

# Uruchom dopóki użytkownik nie zamknie okna
running = True
while running:

    # Czy użytkownik kliknął przycisk wyjścia z apk.?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełnij background kolorem białym
    screen.fill((255, 255, 255))

    # Narysuj niebieski koło na środku
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Odwróć wyświetlanie
    pygame.display.flip()

# Wyjście z aplikacji
pygame.quit()
