from Game_piece_2 import *
import math
import pygame
import time

#add your classes here
from Unit_2 import *

class Building(Game_piece):
    i = 0
    def __init__(self):
        Game_piece.__init__(self)
        self.speed = 1
        self.size = 100
        self.health = B_HEALTH
        self.attack = B_ATTACK

    def draw(self, image):
        if self.activation:
            building = pygame.Rect(self.x,self.y,self.size,self.size)
            pygame.draw.rect(image, self.color, building)
            for unit in self.army:
                unit.draw(image)
        return image

    def activate(self, x, y, color, game):
        self.x = x
        self.y = y
        self.color = color
        self.dx = 0
        self.dy = 0        
        self.army = [Unit() for x in range(50)]
        self.health = B_HEALTH
        self.activation = True    
    
    def spawn_unit(self, target):
        for unit in self.army:
            if not unit.activation:
                unit.activate(target, self)
                return
          
    def lead_unit(self):
        if not self.army[Building.i].activation:
            self.army.append(self.army[Building.i])
            self.army.pop(Building.i)
        return self.army[Building.i] 
        
    def move_units(self, game):
        for i in range(len(self.army)):
            unit = self.army[i]
            prev_unit = self.army[i-1]
            if unit.activation and i == 0:
                unit.move(game)
            elif unit.activation and prev_unit.activation and abs(prev_unit.x-unit.x) > 10:
                unit.move(game)
            else:
                pass