from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_a

import pygame
import sys

from area import generate_dungeon
from character import Character
from tileset import TileSet
from ai import RandomAI

COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)
WOLF_TILE = (6, 1)
CAT_TILE = (28, 1)
CHEST_TILE = (30, 16)

LEFT = (-1, 0)


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
        if ev.key == K_a:
            cow.attack(LEFT)
        return True
    return False


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()

    tile_set = TileSet("tileset.png")
    dungeon = generate_dungeon()

    # create characters
    Character(WOLF_TILE, dungeon)
    cow = Character(COW_TILE, dungeon)
    hunter = Character(HUNTER_TILE, dungeon)
    Character(CAT_TILE, dungeon)
    Character(CHEST_TILE, dungeon)

    # set character AI
    hunter.set_ai(RandomAI())

    running = True
    while running:
        run_turn = handle_input(cow)

        if run_turn:
            dungeon.run_turn()

        screen.fill((0, 0, 0))
        dungeon.draw(screen, tile_set)

        pygame.display.flip()

if __name__ == '__main__':
    main()
