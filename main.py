# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()     
    asteroids = pygame.sprite.Group()     
    shots = pygame.sprite.Group()     

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:            
            if asteroid.collides(player):
                print("Game over!")
                raise SystemExit()

            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()                    

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()        
        
        dt = clock.tick(60) / 1000        
        

if __name__ == "__main__":
    main()
