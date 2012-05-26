from pygame.rect import Rect
from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE

import pygame
import sys
import random

from dungeon import generate_dungeon

COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)


class TileSet(object):
    TILE_SIZE = 32

    def __init__(self):
        self.tiles_image = pygame.image.load('tileset.png')

    def blit_tile(self, target_surface, tile_index, dest):
        x, y = map(lambda coord: coord * self.TILE_SIZE, tile_index)
        transformed_dest = map(lambda coord: coord * self.TILE_SIZE, dest)
        target_surface.blit(self.tiles_image, transformed_dest,
                            Rect(x, y, self.TILE_SIZE, self.TILE_SIZE))


class Cow(object):
    def __init__(self, tile_set, dungeon):
        self.tile_set = tile_set
        self.dungeon = dungeon
        self.pos = (0, 0)

    def draw(self, surface):
        self.tile_set.blit_tile(surface, COW_TILE, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y


class Hunter(object):
    def __init__(self, tileset, dungeon):
        self.tileset = tileset
        self.dungeon = dungeon
        self.pos = (7, 7)

    def draw(self, surface):
        self.tileset.blit_tile(surface, HUNTER_TILE, self.pos)

    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (self.dungeon.walkable(new_pos_x, new_pos_y)):
            self.pos = new_pos_x, new_pos_y


def handle_input(cow, hunter):
    ev = pygame.event.poll()
    if ev.type == KEYUP:
        if ev.key == K_DOWN:
            cow.move(0, 1)
        if ev.key == K_UP:
            cow.move(0, -1)
        if ev.key == K_LEFT:
            cow.move(-1, 0)
        if ev.key == K_RIGHT:
            cow.move(1, 0)
        if ev.key == K_ESCAPE:
            sys.exit(0)
        hunter.move(random.randint(-1, 1), random.randint(-1, 1))


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()

    tile_set = TileSet()
    dungeon = generate_dungeon(tile_set)

    cow = Cow(tile_set, dungeon)
    hunter = Hunter(tile_set, dungeon)

    running = True
    while running:
        handle_input(cow, hunter)

        screen.fill((0, 0, 0))
        dungeon.draw(screen)
        cow.draw(screen)
        hunter.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
