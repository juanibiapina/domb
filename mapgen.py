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

    def random(self):
        return randint(self.min, self.max)
    
class Room(object):
    ROOM_SIZE = Range(2, 50)
    ROOM_DISTANCE = Range(10, 50)


    def __init__(self, pos):
        self.boundary = Rect(0, 0, self.ROOM_SIZE.random(), self.ROOM_SIZE.random())
        self.boundary.center = pos

    def draw(self, surface):
        draw.rect(surface, Color("green"), self.boundary)

    def create_new_room_at_east(self):
        new_room = Room(self.boundary.center)
        new_room.boundary.left = self.boundary.right + self.ROOM_DISTANCE.random()
        return new_room

def generate_rooms():
    room_list = []
    room = Room(AREA.center)
    new_room = room.create_new_room_at_east()

    room_list.append(room)
    room_list.append(new_room)

    return room_list

def preview():
    import pygame
    screen = pygame.display.set_mode(AREA.size)

    for room in generate_rooms():
        room.draw(screen)

    pygame.display.flip()

    while True:
        ev = pygame.event.poll()
        if ev.type == KEYUP:
            sys.exit(0)

if __name__ == '__main__':
    preview()
