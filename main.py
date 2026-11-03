import pygame
import sys
from logger import log_state
from logger import log_event
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from player import Player
from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating Groups to manage game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Keeping track of delta time
    clock = pygame.time.Clock()
    dt = 0.0

    # Instantiating player
    xPos = SCREEN_WIDTH / 2
    yPos = SCREEN_HEIGHT / 2
    player = Player(xPos, yPos)

    # Instantiating Asteroids
    AsteroidField()

    running = True

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game loop
    while running == True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing appplication...")
                running = False
                break
        
        screen.fill("black")
        dt = clock.tick(60) / 1000 # we're dividing by 1000 to convert from miliseconds to seconds

        updatable.update(dt)
        for object in drawable:
            object.draw(screen)

        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")

                running = False
                break

            for shot in shots:
                if object.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    object.split()

        pygame.display.flip()
        # print(dt, flush=True)

    pygame.quit()


if __name__ == "__main__":
    main()
