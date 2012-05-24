from pygame.locals import *
import pygame
import time
import sys

GROUND_TILE = (9, 31)
COW_TILE = (5, 4)

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
    def __init__(self, tileset):
        self.tileset = tileset
        self.pos = (0, 0)

    def draw(self, surface):
        tile_set.blit_tile(screen, COW_TILE, self.pos)
    
    def move(self, dx, dy):
        new_pos_x = self.pos[0] + dx
        new_pos_y = self.pos[1] + dy
        if (new_pos_x >= 0 and new_pos_y >= 0 and new_pos_x < screen.get_width()/32 and new_pos_y < screen.get_height()/32): 
            self.pos = new_pos_x, new_pos_y

class Map(object):
    def __init__(self, data):
        self._data = data

    def draw(self, screen):
        for pos, tile in self._data.iteritems():
            tile_set.blit_tile(screen, tile, pos)

def handle_input(cow):
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

if __name__ == '__main__':
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()

    the_map = Map(dict(((i, 0), GROUND_TILE) for i in range(10)))
    tile_set = TileSet()
    cow = Cow(tile_set)
    
    running = True
    while running:
        handle_input(cow)

        screen.fill((0,0,0))
        the_map.draw(screen)
        cow.draw(screen)

        pygame.display.flip()
