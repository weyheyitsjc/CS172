#File: Drawable.py
#Purpose: Drawable parent class for the other child classes to inherit
#Name: Jacy Yu
#Drexel ID: jy529
#Date: May 17, 2019

import pygame
import abc

#Abstract Drawable class
class Drawable(metaclass = abc.ABCMeta):
    #Set up attributes of x, y, and visibility
    def __init__(self, x, y, visible = True):
        self.__x = x
        self.__y = y
        self.__v = visible
     
    #setter for x
    def setX(self, x):
        self.__x = x
    
    #setter for y
    def setY(self, y):
        self.__y = y
    
    #setter for visibility, change the visibility
    def setV(self, v):
        self.__v = v
    
    #getter to get x so child classes can get it when it is mutated
    def getX(self):
        return self.__x
    
    #getter to get x so child classes can get it when it is mutated
    def getY(self):
        return self.__y
    
    #getter to get visibility so child classes can get it when it is mutated
    def getV(self):
        return self.__v
    
    #abstract draw method
    @abc.abstractmethod
    def draw(self, surface):
        pass
    
    #abstract rectangle method
    @abc.abstractmethod
    def get_rect(self):
        pygame.draw.rect(surface, color, [self.__x, self.__y, self.__width, self.__height])