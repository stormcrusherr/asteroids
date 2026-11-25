import sys

import pygame
from logger import log_state
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from logger import log_event
from asteroid import Asteroid
from asteroidfeild import AsteroidField
from shot import Shot

def main() -> None:
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable, )
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
                elif asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()

                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)



        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
