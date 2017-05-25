from Game_piece_2 import *
import math
import pygame
import time
from Vec2d import *
from Bullet_2 import *


class Cannon(Game_piece):
    def __init__(self):
        Game_piece.__init__(self)
        self.speed = 1
        self.size = 15
        self.health = C_HEALTH
        self.attack = C_ATTACK
        self.radius = C_RANGE

    def draw(self, image):
        if self.activation:
            cannon = pygame.Rect(self.x, self.y, self.size, self.size)
            pygame.draw.circle(image, self.range_color, (
                int(self.x + (self.size / 2)), int(self.y + (self.size / 2))),
                               int(self.radius))
            pygame.draw.rect(image, self.color, cannon)
            if self.bullet.activation:
                self.bullet.draw(image)
        return image

    def activate(self, x, y, building, range_color):
        self.x = x
        self.y = y
        self.color = building.color
        self.dx = 0
        self.dy = 0
        self.bullet = Bullet()
        self.health = C_HEALTH
        self.activation = True
        self.range_color = range_color

    def launch(self, target):
        if self.in_range(target):
            if not self.bullet.activation:
                self.bullet.activate(target, self)

    def in_range(self, target):
        if self.activation and target.activation:
            return (
                abs(target.x - (self.x + (self.size / 2)))**2 + abs(
                    (self.y + (self.size / 2) -
                     (target.y + target.size))**2) <= self.radius**2 or
                abs((self.x + (self.size / 2)) - (target.x + target.size))**2 +
                abs((self.y + (self.size / 2)) - (target.y + target.size))**2
                <= self.radius**2 or
                abs(target.x - (self.x + (self.size / 2)))**2 +
                abs(target.y - (self.y + (self.size / 2)))**2 <= self.radius**2
                or abs((self.x + (self.size / 2)) - (target.x + target.size))**
                2 + abs(target.y - (self.y + (self.size / 2)))**2 <=
                self.radius**2)

    def calculate_lead(self, target):
        #tower
        tower_loc = Vec2d(self.x, self.y)
        #target
        target_loc = Vec2d(target.x, target.y)
        target_vel = Vec2d(target.dx, target.dy)
        target_speed = target_vel.get_length()
        dist_to_target = target_loc - tower_loc
        #alpha = (dist_to_target.dot(target_vel) / (dist_to_target.get_length() * target_speed))
        a = target_vel[0]**2 + target_vel[1]**2 - self.bullet.speed**2
        b = 2 * target_vel[0] * (
            target_loc[0] - tower_loc[0]) + target_vel[1] * (
                target_loc[1] - tower_loc[1])
        c = (target_loc[0] - tower_loc[0])**2 + (
            target_loc[1] - tower_loc[1])**2
        #Now we can look at the discriminant to determine if we have a possible solution
        #If the discriminant is less than 0, forget about hitting your target -- your projectile can never get there in time. Otherwise, look at two candidate solution
        if b**2 - 4 * a * c >= 0:
            p = -b / (2 * a)
            q = math.sqrt((b * b) - 4 * a * c) / (2 * a)
            t1 = p - q
            t2 = p + q
            if t1 > t2 and t2 > 0:
                t = t2
            else:
                t = t1
            aimX = t * target_vel[0] + target_loc[0]
            aimY = t * target_vel[1] + target_loc[1]
            return (aimX, aimY, t)
        else:
            print("no solution")
