import random as r
from math import sin, cos

size = 3
speed = 2


class Orb:
    def __init__(self):
        self.x = r.randint(1 + size, 499 - size)
        self.y = r.randint(1 + size, 499 - size)
        self.topLeft = [self.x - size, self.y - size]
        self.bottomRight = [self.x + size, self.y + size]
        self.angle = r.randint(0, 360)
        self.vel = [speed * sin(self.angle), speed * cos(self.angle)]

    def updatePos(self):
        self.topLeft[0] += self.vel[0]
        self.topLeft[1] += self.vel[1]
        self.bottomRight[0] += self.vel[0]
        self.bottomRight[1] += self.vel[1]
        self.x += self.vel[0]
        self.y += self.vel[1]
