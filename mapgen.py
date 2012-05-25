import sys
from random import randint

import pygame
from pygame.locals import *
from pygame import draw

AREA = Rect(0, 0, 500, 500)

class Range(object):
    def __init__(self, min, max):
        self.min = min
        self.max = max

class Room(object):
    ROOM_SIZE = Range(2, 50)

    def __init__(self, pos):
        self.boundary = Rect(0, 0, 
                             randint(self.ROOM_SIZE.min, self.ROOM_SIZE.max), 
                             randint(self.ROOM_SIZE.min, self.ROOM_SIZE.max))
        self.boundary.center = pos

    def draw(self, surface):
        draw.rect(surface, Color("green"), self.boundary)

def preview():
    import pygame
    screen = pygame.display.set_mode(AREA.size)

    Room(AREA.center).draw(screen)
    pygame.display.flip()

    while True:
        ev = pygame.event.poll()
        if ev.type == KEYUP:
            sys.exit(0)

if __name__ == '__main__':
    preview()
