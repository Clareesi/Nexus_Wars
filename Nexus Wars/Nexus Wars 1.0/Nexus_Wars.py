from pygamehelper import *
from Game_piece import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
import random

#add your classes here
from Building import *
from Unit import *

#constants
FPS = 100

class Nexus_wars(PygameHelper):
    i=0
    def __init__(self, state="play"):
        self.state = state
        self.w, self.h = 1000, 400
        self.bkg_color = (255,255,255)
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(self.bkg_color))
        #create walls for the game
        self.LEFT_WALL = 0
        self.RIGHT_WALL = self.w
        self.TOP_WALL = 0
        self.BOTTOM_WALL = self.h
        #create two buildings
        self.p_building = Building()
        self.e_building = Building()
        self.p_building.activate(0, 150, pygame.Color("forest green"), self)
        self.e_building.activate(self.w-self.e_building.size, 150, pygame.Color("red"), self)
        self.myfont=pygame.font.SysFont("curlz", 100)
    
    def update(self):
        if self.state=="play":
            self.p_building.move_units(self)
            self.e_building.move_units(self)
            self.p_building.lead_unit().battle(self.e_building.lead_unit())
            self.p_building.lead_unit().battle(self.e_building)
            self.e_building.lead_unit().battle(self.p_building)
            if self.p_building.health<=0:
                self.state="over"
            elif self.e_building.health<=0:
                self.state="win"
        elif self.state == "pause":
            pass
        else:
            pass

    def keyUp(self, key):
        if self.state == "play":
            if key == K_a:
                self.p_building.spawn_unit(self.e_building)
            if key == K_LEFT:
                self.e_building.spawn_unit(self.p_building)
            if key == K_w:
                for unit in self.p_building.army:
                    unit.health += 1
            if key == K_UP:
                for unit in self.e_building.army:
                    unit.health += 1
            if key == K_SPACE:
                self.state = "pause"
        elif self.state == "pause":
            if key == K_SPACE:
                self.state = "play"
             
    def draw(self):
        if self.state=="play":
            self.screen.fill(self.bkg_color) #clear screen
            self.p_building.draw(self.screen)
            self.e_building.draw(self.screen)     
        elif self.state=="over":
            self.screen.fill(self.e_building.color)
            self.label=self.myfont.render("You're Dead", 10, (255, 255, 255))
            self.screen.blit(self.label,(center(self.w, self.label.get_width()), center(self.h, self.label.get_height())))
        elif self.state=="win":
            self.screen.fill(self.p_building.color)
            self.label=self.myfont.render("You Win", 10, (255, 255, 255))
            self.screen.blit(self.label, (center(self.w, self.label.get_width()), center(self.h, self.label.get_height())))

s = Nexus_wars()
s.mainLoop(FPS)

