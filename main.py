import pygame
from logger import log_state
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Keeping track of delta time
    clock = pygame.time.Clock()
    dt = 0.0

    # Instantiating player
    xPos = SCREEN_WIDTH / 2
    yPos = SCREEN_HEIGHT / 2
    player = Player(xPos, yPos)

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt = clock.tick(60) / 1000 # we're dividing by 1000 to convert from miliseconds to seconds
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        # print(dt, flush=True)

if __name__ == "__main__":
    main()
