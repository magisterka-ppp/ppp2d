
import pygame

from game import Game

if __name__ == '__main__':
    clock = pygame.time.Clock()
    game = Game()
    tps = 60
    dt = 0

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        dt += clock.tick()/1000

        if dt > 1/tps:
            dt -= 1/tps
            game.logicLoop()
        game.drawLoop()
