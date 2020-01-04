#File: Text.py
#Purpose: Derived Text class to print the score and instructions, inherits from Drawable
#Cited from lecture example
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 17, 2019

from Drawable import Drawable
import pygame

class Text(Drawable):
    #initialize the message to be written, location (x, y), and the color
    def __init__(self, message = "Score:", x = 0, y = 0, color = [0, 0, 0]):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 25)
        self.__surface = fontObj.render(message, True, color)
    
    def draw(self, surface):
        surface.blit(self.__surface, [super().getX(), super().getY()])

    def get_rect(self):
        pass