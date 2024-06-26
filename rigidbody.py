import vectors
from vectors import Vector2D
from vectors import Magnitude
import pygame

#initialise pygame
pygame.init()
#screen size
scr = (width, height) = (1000, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Physics Simulator")

# Colors
white = (252, 251, 244)
black = (20, 25, 24)
purple = (186, 85, 255)

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
    
    def Draw(self):
        pygame.draw.circle(screen, purple, (self.pos.x, self.pos.y), 5)


ball = Rigidbody2D(Vector2D(0.0, 0.0), 1.0)
ball.SetPostion(Vector2D(600.0, 500.0))
ball.SetVelocity(Vector2D(0.0, 50.0))

f_centripetal = Vector2D(0.0, 0.0)

#prepare game loop
game = True
#init clock for fps manipulation
clock = pygame.time.Clock()
fps = 60

while game:
    deltaTime = clock.tick(fps) / 1000

    ############# Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # ends the game, can be a different key if desired. The program will run fine without this
                game = False
                break
    
    ############# Simulation
    # Reset the forces
    forces = []

    # Calculate the centripetal force F=(mv^2)/r
    F = (ball.mass * Magnitude(ball.velocity)**2) / 100
    f_centripetal = vectors.Multiply(vectors.Normalize(vectors.Subtract(Vector2D(500.0, 500.0), ball.pos)), F)
    forces.append(f_centripetal)

    # Set the forces of the rb
    ball.forces = forces

    #Tick the rb
    ball.Move(deltaTime)

    ########## Render
    #Clear screen
    screen.fill(black)

    #Draw rb
    ball.Draw()

    #end of loop
    pygame.display.flip()

pygame.quit()