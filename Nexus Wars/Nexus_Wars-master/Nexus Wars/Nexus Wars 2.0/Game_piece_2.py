from math import e, pi, cos, sin, sqrt
import pygame

#constants
B_HEALTH = 20
B_ATTACK = 0
UNIT_HEALTH = 1
UNIT_ATTACK = 1
C_HEALTH = 1000
C_ATTACK = 1
C_RANGE = 100


def center(self, target):
    return (self / 2) - (target / 2)


class Game_piece:
    x = 0

    def __init__(self):
        self.activation = False
        self.stop = True

    def die(self):
        self.activation = False
        self.health = 0

    def collide(self, target):
        if self.activation and target.activation:
            return not (self.x > target.x + target.size or
                        self.x + self.size < target.x or
                        self.y + self.size < target.y or
                        self.y > target.y + target.size)

    def battle(self, target):
        if self.collide(target):
            self.stop = True
            target.stop = True
            target.health = target.health - self.attack
            self.health = self.health - target.attack
        if target.health <= 0:
            target.die()
            self.stop = False
        if self.health <= 0:
            self.die()
            target.stop = False

    def move(self, game):
        if self.activation and not self.stop:
            self.move_horz(game)
            self.move_vert(game)

    def move_horz(self, game):
        self.x = self.x + self.dx
        if self.x + self.size > game.RIGHT_WALL:
            self.x = 0
            self.activation = False
        elif self.x < game.LEFT_WALL:
            self.x = 0
            self.activation = False
        else:
            pass

    def move_vert(self, game):
        self.y = self.y + self.dy
        if self.y <= game.TOP_WALL:
            self.y = 0
            self.activation = False
        elif self.y >= game.BOTTOM_WALL:
            self.y = 0
            self.activation = False
        else:
            pass
