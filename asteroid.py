import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width = 2)

    def update(self, dt):
        #self.velocity += (self.velocity/100) -- this was a speed up test
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_angle = random.uniform(20,50)

        ast_1_vel = self.velocity.rotate(rand_angle) 
        ast_2_vel = self.velocity.rotate(-rand_angle) 

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y,new_radius)
        new_asteroid1.velocity = ast_1_vel * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y,new_radius)
        new_asteroid2.velocity = ast_2_vel * 1.2
