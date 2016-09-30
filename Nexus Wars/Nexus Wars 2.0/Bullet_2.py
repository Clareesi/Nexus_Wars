from Game_piece_2 import *
import math
import pygame

class Bullet(Game_piece):
    
    def __init__(self):
        Game_piece.__init__(self)
        self.speed = 1000
        self.size = 3
        self.health = 1
        self.attack = C_ATTACK    
        
    def draw(self, image):
        if self.activation:
            bullet = pygame.Rect(self.x,self.y,self.size,self.size)
            pygame.draw.rect(image, self.color, bullet)
        return image        
    
    def activate(self, target, cannon):
        self.x = cannon.x + (self.size/2)
        self.y = cannon.y + (self.size/2)   
        (x, y, t) = cannon.calculate_lead(target)
        self.dx = (self.x - x)/(t-5)
        self.dy = (self.y - y)/(t-5)
        self.color = cannon.color  
        self.health = 1
        self.activation = True
        self.stop = False
    
