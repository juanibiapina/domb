import sys
from random import randint

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
    SIZE = Range(4, 50)
    DISTANCE = Range(10, 20)
    OFFSET = Range(-10, 10)

    SIDES_TO_ALIGN = {
        "east": ("left", "right", 1),
        "west": ("right", "left", -1),
        "north": ("bottom", "top", -1),
        "south": ("top", "bottom", 1),
    }

    SIDE_TO_OFFSET = {
        "east": "top",
        "west": "top",
        "north": "right",
        "south": "right",
    }

    def __init__(self, pos):
        self.boundary = Rect(0, 0, self.SIZE.random(), self.SIZE.random())
        self.boundary.center = pos

    def draw(self, surface):
        draw.rect(surface, Color("green"), self.boundary)

    def create_new_room_at(self, side):
        new_room = Room(self.boundary.center)

        new_room_side, room_side, sign = self.SIDES_TO_ALIGN[side]
        new_side_pos = (getattr(self.boundary, room_side)
                        + sign * self.DISTANCE.random())
        setattr(new_room.boundary, new_room_side, new_side_pos)

        side_to_offset = self.SIDE_TO_OFFSET[side]
        offset_side_pos = getattr(new_room.boundary, side_to_offset) + self.OFFSET.random()
        setattr(new_room.boundary, side_to_offset, offset_side_pos)
        return new_room


def generate_rooms():
    room_list = []
    room = Room(AREA.center)

    def gen(room, i):
        if i <= 0:
            return
        else:
            for direction in ["east", "west", "north", "south"]:
                new_room = room.create_new_room_at(direction)
                if new_room.boundary.collidelist([room.boundary for room
                                                  in room_list]) == -1:
                    room_list.append(new_room)
                    gen(new_room, i - 1)

    room_list.append(room)
    gen(room, 5)
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
