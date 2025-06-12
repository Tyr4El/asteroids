
from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position+=(self.velocity*dt)#don't need to get anything more to access circleshape velo,right?
    def split(self):
        self.kill()#intermediary step
        if self.radius<=ASTEROID_MIN_RADIUS:#predetermined by boot.dev then
            return
        else:
            angle=random.uniform(20,50)
            vector_aster1=self.velocity.rotate(angle)
            vector_aster2=self.velocity.rotate(-angle)
            new_radius=self.radius-ASTEROID_MIN_RADIUS
            aster1=Asteroid(self.position.x,self.position.y,new_radius)
            aster2=Asteroid(self.position.x,self.position.y,new_radius)
            aster1.velocity=vector_aster1*1.2
            aster2.velocity=vector_aster2*1.2