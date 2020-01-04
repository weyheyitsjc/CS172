#File: Block.py
#Purpose: Derived Block class to draw the block and make the surrounding bound for collision
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 17, 2019

from Drawable import Drawable
import pygame

class Block(Drawable):
    #initialize location (x, y), the color, and visibility of the block
    def __init__(self, x, y, color, visible = True):
        super().__init__(x, y, visible = True)
        self.__color = color
    
    #method to draw the block and the border around it
    def draw(self, surface):
        pygame.draw.rect(surface, [0, 0, 0], [int((super().getX()-2)), int((super().getY()-2)), 34, 34])
        pygame.draw.rect(surface, self.__color, [int(super().getX()), int(super().getY()), 30, 30])
        
    #method to make rectangle object for collision detection
    def get_rect(self):
        return pygame.Rect((super().getX()-2), (super().getY()-2), 34, 34)