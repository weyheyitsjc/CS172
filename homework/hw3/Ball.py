#File: Ball.py
#Purpose: Derived Ball class to draw the ball and make the rectangle that surrounds it, inherits from Drawable
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 17, 2019

from Drawable import Drawable
import pygame

class Ball(Drawable):
    #initialize the location (x, y), color and visibility of the ball
    def __init__(self, x, y, color, visible = True):
        super().__init__(x, y, visible = True)
        self.__color = color
    
    #method to draw the ball method
    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, [int(super().getX()), int(super().getY())], 10, 0)
        
    #method to make rectangle object that surrounds the ball for collision detection
    def get_rect(self):
        return pygame.Rect((super().getX()-10), (super().getY()-10), 20, 20)