import sys
from random import randint

import pygame
from pygame.locals import *
from pygame import draw

AREA = Rect(0, 0, 500, 500)

class Room(object):
    MIN_ROOM_SIZE = 2
    MAX_ROOM_SIZE = 50

    def __init__(self, pos):
        self.boundary = Rect(0, 0, 
                             randint(self.MIN_ROOM_SIZE, self.MAX_ROOM_SIZE), 
                             randint(self.MIN_ROOM_SIZE, self.MAX_ROOM_SIZE))
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
