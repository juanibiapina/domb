from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE

import pygame
import sys
import random

from dungeon import generate_dungeon
from character import Character
from tileset import TileSet

COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)


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
    dungeon = generate_dungeon()

    cow = Character(COW_TILE, dungeon)
    hunter = Character(HUNTER_TILE, dungeon)

    running = True
    while running:
        handle_input(cow, hunter)

        screen.fill((0, 0, 0))
        dungeon.draw(screen, tile_set)
        cow.draw(screen, tile_set)
        hunter.draw(screen, tile_set)

        pygame.display.flip()

if __name__ == '__main__':
    main()
