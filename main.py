import pygame 
from constants import *
from player import Player

def main():
    #Initializing pygame and setting screen mode
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Setting up clock
    game_clock = pygame.time.Clock()
    dt = 0

    #Setting up a player
    p1 = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,PLAYER_RADIUS)


    while True:
        #Checking events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Draw our screen
        screen.fill("black")
        
        #Update our player
        p1.update(dt)
        
        #Draw our player
        p1.draw(screen)

        #Refreshing screen and calling clock to pause game
        pygame.display.flip()

        dt = game_clock.tick(60)/1000





if __name__ == "__main__":
    main()
