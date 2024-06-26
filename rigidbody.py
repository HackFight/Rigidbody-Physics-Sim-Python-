import time
import vectors
from vectors import Vector2D
from vectors import Magnitude
import pygame

class Rigidbody2D():
    def __init__(self, pos, mass):
        self.pos = pos
        self.mass = mass
        self.forces = []
        self.velocity = Vector2D(0.0, 0.0)
    
    def AddForce(self, force):
        self.forces.append(force)
    
    def ResultantForce(self):
        resultantForce = Vector2D(0.0, 0.0)

        for force in self.forces:
            resultantForce = vectors.Add(resultantForce, force)

        return resultantForce
    
    def SetPostion(self, vector):
        self.pos = vector
    
    def SetVelocity(self, vector):
        self.velocity.x = vector.x
        self.velocity.y = vector.y
    
    def Move(self, time):
        a = vectors.Multiply(self.ResultantForce(), 1/self.mass)

        s = Vector2D(0.0, 0.0)
        s.x = self.velocity.x * time + 0.5 * a.x * time**2
        s.y = self.velocity.y * time + 0.5 * a.y * time**2

        v = Vector2D(0.0, 0.0)
        v.x = self.velocity.x + a.x * time
        v.y = self.velocity.y + a.y * time

        self.pos = vectors.Add(self.pos, s)
        self.velocity = v


ball = Rigidbody2D(Vector2D(0.0, 0.0), 1.0)
ball.SetPostion(Vector2D(5.0, 0.0))
ball.SetVelocity(Vector2D(0.0, -3.0))

f_centripetal = Vector2D(0.0, 0.0)

#initialise pygame
pygame.init()
#screen size
scr = (width, height) = (960, 960)
screen = pygame.display.set_mode((width, height))
#prepare game loop
game = True
#init clock for fps manipulation
clock = pygame.time.Clock()
fps = 60

while game:
    clock.tick(fps)

    print(time.clock())

    forces = []

    F = (ball.mass * Magnitude(ball.velocity)**2) / 5
    f_centripetal = vectors.Multiply(vectors.Normalize(vectors.Subtract(Vector2D(0.0, 0.0), ball.pos)), F)
    forces.append(f_centripetal)

    ball.forces = forces

    ball.Move(deltatime)
    #print(str(ball.pos.x) + ", " + str(ball.pos.y))

    time.sleep(1/60)
    #end of loop
    pygame.display.flip()

pygame.quit()