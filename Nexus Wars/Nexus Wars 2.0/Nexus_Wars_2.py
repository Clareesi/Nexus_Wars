from pygamehelper import *
from Game_piece_2 import *
from pygame import *
from pygame.locals import *
from math import e, pi, cos, sin, sqrt
import random
from Vec2d import *

#add your classes here
from Building_2 import *
from Unit_2 import *
from Cannon_2 import *

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
        self.p_cannon = Cannon()
        self.e_cannon = Cannon()
        self.e_cannon.activate((random.randrange((self.p_building.x + self.p_building.size + self.e_cannon.radius),(self.e_building.x - self.e_cannon.radius)), random.randrange(self.h)), self.e_building, pygame.Color("light pink"))   
        self.player = [self.p_building, self.p_cannon] + self.p_building.army 
        self.enemy = [self.e_building, self.e_cannon] + self.e_building.army
        self.myfont=pygame.font.SysFont("curlz", 100)

    def keyUp(self, key):
        if self.state == "play":
            if key == K_a:
                self.p_building.spawn_unit(self.e_building)
            #if key == K_LEFT:
                #self.e_building.spawn_unit(self.p_building)
            if key == K_w:
                for unit in self.p_building.army:
                    unit.health += 1
            #if key == K_UP:
                #for unit in self.e_building.army:
                    #unit.health += 1
            if key == K_SPACE:
                self.state = "pause"
        elif self.state == "pause":
            if key == K_SPACE:
                self.state = "play"
        
    def update(self):
        if self.state=="play":
            self.p_building.move_units(self)
            self.e_building.move_units(self)
            for item in self.enemy:
                self.p_building.lead_unit().battle(item)
            for item in self.player:
                self.e_building.lead_unit().battle(item)
            if self.p_cannon.activation:
                self.p_cannon.launch(self.e_building.lead_unit())
                self.p_cannon.bullet.move(self)
                self.p_cannon.bullet.battle(self.e_building.lead_unit())
            if self.e_cannon.activation:
                self.e_cannon.launch(self.p_building.lead_unit())
                self.e_cannon.bullet.move(self)
                self.e_cannon.bullet.battle(self.p_building.lead_unit())     
            if self.p_building.health<=0:
                self.state="over"
            elif self.e_building.health<=0:
                self.state="win"
        elif self.state == "pause":
            pass
        else:
            pass

        if Nexus_wars.i%10 == 0:
            self.e_building.spawn_unit(self.p_building)
            for unit in self.e_building.army:
                unit.health += 1
        Nexus_wars.i+=1

    def mouseUp(self, button, pos):
        if not self.p_cannon.activation:
            if pygame.mouse.get_pressed():
                self.p_cannon.activate(pygame.mouse.get_pos(), self.p_building, pygame.Color("light green"))

    def draw(self):
        if self.state=="play":
            self.screen.fill(self.bkg_color) #clear screen
            self.p_cannon.draw(self.screen)
            self.e_cannon.draw(self.screen)
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

