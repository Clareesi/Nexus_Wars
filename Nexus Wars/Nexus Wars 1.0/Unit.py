from Game_piece import *
import math
import pygame

class Unit(Game_piece):
    
    def __init__(self):
        Game_piece.__init__(self)
        self.speed = 900
        self.size = 5
        self.health = UNIT_HEALTH
        self.attack = UNIT_ATTACK
        
    def draw(self, image):
        if self.activation:
            unit = pygame.Rect(self.x,self.y,self.size,self.size)
            pygame.draw.rect(image, self.color, unit)
        return image        
    
    def activate(self, target, building):
        self.x = building.x + center(building.size, self.size)
        self.y = building.y + center(building.size, self.size)      
        self.dx = ((target.x+center(building.size, self.size)) - self.x)/self.speed
        self.dy = ((target.y+center(building.size, self.size)) - self.y)/self.speed 
        self.color = building.color  
        self.health = UNIT_HEALTH
        self.activation = True
        self.stop = False