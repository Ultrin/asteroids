import sys
import pygame
import pygame.font

# import everything from constants
# into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()

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
    score = 0

    while True:
        font = pygame.font.Font(None, 36)
        game_over_font = pygame.font.Font(None, 108)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.collision(player):
                print("Game over!")
                #game_over_text = game_over_font.render(f'Game Over!', True, (255, 255, 255))
                #screen.blit(game_over_text, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
                sys.exit()
                #pygame.display.flip()
                
            for s in shots:
                if s.collision(a):
                    score += 1
                    s.kill()
                    a.split()


        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = game_clock.tick(60)/1000





if __name__ == "__main__":
    main()
