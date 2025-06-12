# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

import asteroidfield
import player
from asteroidfield import AsteroidField
from constants import *
from player import *
from asteroid import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock=pygame.time.Clock()
    dt=0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    group_astero=pygame.sprite.Group()

    group_updatable=pygame.sprite.Group()#put that before player because bobby is not getting updated if not
    group_drawable=pygame.sprite.Group()
    Player.containers=(group_updatable,group_drawable)#it s all Players not only bobby

    Asteroid.containers=(group_astero,group_drawable,group_updatable)
    AsteroidField.containers=group_updatable

    bobby=player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    group_shots=pygame.sprite.Group()
    Shot.containers=(group_shots,group_updatable,group_drawable)
    field1=asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        group_updatable.update(dt)
        for asteroid in group_astero:
            if asteroid.collision_detection(bobby):
                sys.exit("Game Over")
            for bullets in group_shots:#kill feature from pygame on object
                if asteroid.collision_detection(bullets):
                    bullets.kill()
                    asteroid.kill()

        for players in group_drawable:
            players.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000

    pygame.quit()

if __name__=="__main__":
   main()