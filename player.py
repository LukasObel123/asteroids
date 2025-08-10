import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self,x,y,PLAYER_RADIUS):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        self.shot_cooldown -= dt
        print(self.shot_cooldown)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown< 0:
            self.shoot()
        

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        x = self.position[0]
        y = self.position[1]
        s = Shot(x,y,1)
        s.velocity = PLAYER_SHOOT_SPEED*pygame.Vector2(0,1).rotate(self.rotation)



    
