import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    #Initializing pygame and setting screen mode
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Setting up clock
    game_clock = pygame.time.Clock()
    dt = 0


    #Lets make some groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()




    #Setting up a player
    Player.containers = (updatable,drawable,shots) #setting static container for player
    p1 = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,PLAYER_RADIUS)
    Shot.containers = (shots,updatable,drawable)

    #Setting up the asteroid and asteroid field
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    afield = AsteroidField()

    

    while True:
        #Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Draw our screen
        screen.fill("black")
        
        #Updating all updatables
        updatable.update(dt)

        #Checking asteroid collisions14
        for asteroid in asteroids:
            if asteroid.check_collisions(p1):
                print("Game over!")
                return
            
        #drawing all drawables
        for object in drawable:
            object.draw(screen)

        #Refreshing screen and calling clock to pause game
        pygame.display.flip()

        dt = game_clock.tick(60)/1000





if __name__ == "__main__":
    main()
