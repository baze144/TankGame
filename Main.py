#import pygame,sys
#import os
import pygame
import sys
import os

class Window:
    title = ""
    def __init__(self,a,b):
        pygame.init()
    screen = pygame.display.set_mode((v.x,v.y))  
    def Title():
        input(title)
        pygame.display.set_caption(title)
    def setSize(x,y):
        input(v.x)
        input(v.y)
        


class Vector:
    x = 0
    y = 0

    
class Entity:
        pass



Status = False

while not Status:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Status = True
                    
        



