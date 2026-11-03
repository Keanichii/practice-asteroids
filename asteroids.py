import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS

class Asteroids(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        # Too small to split
        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotation = (-angle, angle)
        for i in range(0, 2):
            # Calculating new Asteroid
            # Rotate by angle and scale up 1.2x
            new_velocity = self.velocity.rotate(rotation[i]) * 2
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Spawning new Asteroid
            new_asteroid = Asteroids(self.position.x, self.position.y, new_radius)
            new_asteroid.velocity = new_velocity