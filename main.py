import sys
import pygame

# import everything from constants
# into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                sys.exit()


        screen.fill("black")

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = game_clock.tick(60)/1000





if __name__ == "__main__":
    main()
