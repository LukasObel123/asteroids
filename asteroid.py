import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,color="white",center=self.position,radius=self.radius,width=2)
    
    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)

        new_vel1 = self.velocity.rotate(angle)
        new_vel2 = self.velocity.rotate(-angle)

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        x = self.position[0]
        y = self.position[1]
        a1 = Asteroid(x,y,new_rad)
        a2 = Asteroid(x,y,new_rad)

        a1.velocity = new_vel1*1.5
        a2.velocity = new_vel2*1.5

        

