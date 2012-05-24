from pygame.locals import *
import pygame
import time
import sys
import random

from map import *

COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)

class TileSet(object):
    TILE_SIZE = 32
    
    def __init__(self):
        self.tiles_image = pygame.image.load('tileset.png')

    def blit_tile(self, target_surface, tile_index, dest):
        x, y = map(lambda coord: coord*self.TILE_SIZE, tile_index)
        transformed_dest = map(lambda coord: coord*self.TILE_SIZE, dest)
        target_surface.blit(self.tiles_image, transformed_dest, 
                            Rect(x, y, self.TILE_SIZE, self.TILE_SIZE))

class Cow(object):
    def __init__(self, tile_set, screen):
        self.tile_set = tile_set
        self.screen = screen
        self.pos = (0, 0)

    def draw(self, surface):
        self.tile_set.blit_tile(surface, COW_TILE, self.pos)
    
    def move(self, dx, dy):
        screen = self.screen
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (new_pos_x >= 0 and new_pos_y >= 0 and new_pos_x < screen.get_width()/32 and new_pos_y < screen.get_height()/32): 
            self.pos = new_pos_x, new_pos_y

class Hunter(object):
    def __init__(self, tileset, screen):
        self.tileset = tileset
        self.screen = screen
        self.pos = (7, 7)

    def draw(self, surface):
        self.tileset.blit_tile(self.screen, HUNTER_TILE, self.pos)
    
    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (new_pos_x >= 0 and new_pos_y >= 0 and new_pos_x < self.screen.get_width()/32 and new_pos_y < self.screen.get_height()/32): 
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
    the_map = generate_map(tile_set)
    cow = Cow(tile_set, screen)
    hunter = Hunter(tile_set, screen)

    running = True
    while running:
        handle_input(cow, hunter)

        screen.fill((0,0,0))
        the_map.draw(screen)
        cow.draw(screen)
        hunter.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
