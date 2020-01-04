#File: hw3.py
#Purpose: main file for the game, runs the game
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 17, 2019

import pygame
import random
import sys
from Drawable import Drawable
from Ball import Ball
from Block import Block
from Text import Text

#line class to draw the baseline
class Line(Drawable):
    def __init__(self, x, y, width):
        super().__init__(x, y)
        self.__width = width
        self.__color = [0,0,0]
        
    def draw(self, surface):
        x = super().getX()
        y = super().getY()
        pygame.draw.line(surface, self.__color, [x, y], [500, y], self.__width)

    def get_rect(self, surface):
        pass

#collision detection function
def intersect(rect1, rect2):
    return (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y)
   
#initialize pygame
pygame.init()
width = 500
height = 500

clock = pygame.time.Clock()
#make the screen
surface = pygame.display.set_mode((width, height))

#draw 10 blocks in random places for the ball to hit
blocks = []
for i in range(0, 10):
    x = random.randint(0, 450)
    y = random.randint(0, 350)
    block = Block(x, y, [0, 0, 255], True)
    blocks.append(block)

#make the ball object
ball = Ball(250, 400, [255, 0, 0], True)

#constants for how the ball will move
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5

xv = 0
yv = 0

scoreCounter = 0

while True:
    #fps
    clock.tick(15)

    #refill the screen everytime the game updates
    surface.fill([255, 255, 255])
    
    #draw the ball
    ball.draw(surface)
    
    #draw the line for the base
    line = Line(0, 400, 1)
    line.draw(surface)
    
    #loops to check for events
    for event in pygame.event.get():
        #quit the game, press q
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_q):
            pygame.quit()
            exit()
        #get initial position of the mouse
        if (event.type == pygame.MOUSEBUTTONDOWN):
            positionStart = pygame.mouse.get_pos()
        #get ending position of the mouse
        if (event.type == pygame.MOUSEBUTTONUP):
            positionEnd = pygame.mouse.get_pos()

            xv = positionEnd[0] - positionStart[0]
            yv = positionEnd[1] - positionStart[1]
    
    if abs(yv) > 0.0001:
        #ball move based on where the x and y is
        if ball.getY() > 400:
            yv = -abs(R * yv)
            xv = eta * xv
        #constrains the ball to the screen and doesn't fly off
        elif ball.getY() < 0:
            yv = abs(yv)
        elif ball.getX() < 0:
            xv = abs(xv)
        elif ball.getX() > 500:
            xv = -abs(xv)
            
        #making gravity work so ball will fall down
        yv = yv + g * dt
              
        #update the ball's position
        ball.setX(ball.getX() + xv * dt)
        ball.setY(ball.getY() + yv * dt)
        
        #check for collision and if there is, the block will be removed and not drawn
        for block in blocks:
            collided = intersect(ball.get_rect(), block.get_rect())
            if collided == True:
                block.setV(False)
                blocks.remove(block)
                scoreCounter += 1
            else:
                continue
    
    #printing the score on the screen
    scoreText = "Score:" + str(scoreCounter)
    score = Text(scoreText, 0, 0, [0, 0, 0])
    score.draw(surface)
    
    #printing basic instructions of how the game will work
    instructions = Text("Move the ball to hit the blocks and score!", 0, 460, [0, 0, 0])
    instructions.draw(surface)
    
    #drawing the blocks only if it is declared as visible
    for block in blocks:
        if block.getV() == True:
            block.draw(surface)

    #updating the display
    pygame.display.update()
    

