import pygame
import random
from Drawable import Drawable

class Rectangle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, [super().getX(), super().getY(), self.__width, self.__height])
        
class Snowflake(Drawable):
    def __init__(self, x, y, color = (255, 255, 255), width = 1):
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        
    def draw(self, surface):
        pygame.draw.line(surface, self.__color, ((super().getX() - 5), super().getY()), ((super().getX() + 5), super().getY()), self.__width)
        pygame.draw.line(surface, self.__color, (super().getX(), (super().getY() - 5)), (super().getX(), (super().getY() + 5)), self.__width)
        pygame.draw.line(surface, self.__color, ((super().getX() - 5), (super().getY() - 5)), ((super().getX() + 5), (super().getY() + 5)), self.__width)
        pygame.draw.line(surface, self.__color, ((super().getX() - 5), (super().getY() + 5)), ((super().getX() + 5), (super().getY() - 5)), self.__width)
       

pygame.init()
width = 500
height = 500
random.seed(150)

surface = pygame.display.set_mode((width, height))

ground = Rectangle(0, 200, 500, 300, (0, 170, 0))

sky = Rectangle(0, 0, 500, 300, (0, 0, 255))

fpsClock = pygame.time.Clock()

snow = []

paused = False

while (True):
    ground.draw(surface)
    sky.draw(surface)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__["key"] == pygame.K_q):
            pygame.quit()
            exit()
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            if paused == True:
                paused = False
            else:
                paused = True
    ground.draw(surface)
    sky.draw(surface)
    
    for snowflake in snow:
            snowflake.draw(surface)  

    if paused == False:
        snowflake = Snowflake(random.randint(1, 500),0)
        snow.append(snowflake)         
        for snowflake in snow:
                snowflake.moveSnow()
                snowflake.draw(surface)
        

    pygame.display.update()
    fpsClock.tick(30)

