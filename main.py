from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_a

import pygame
import sys

from area import generate_dungeon
from character import Character
from tileset import TileSet
from ai import RandomAI
from d20 import resolve_attack

COW_TILE = (5, 4)
HUNTER_TILE = (18, 16)
WOLF_TILE = (6, 1)
CAT_TILE = (28, 1)
CHEST_TILE = (30, 16)


def handle_input(cow, hunter, cat):
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
            resolve_attack(cow, cat)
        return True
    return False


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()

    tile_set = TileSet()
    dungeon = generate_dungeon()

    # create characters
    wolf = Character(WOLF_TILE, dungeon)
    cow = Character(COW_TILE, dungeon)
    hunter = Character(HUNTER_TILE, dungeon)
    cat = Character(CAT_TILE, dungeon)
    chest = Character(CHEST_TILE, dungeon)

    # set character AI
    hunter.set_ai(RandomAI())

    # add characters to dungeon
    dungeon.add_character(cat)
    dungeon.add_character(hunter)
    dungeon.add_character(wolf)
    dungeon.add_character(chest)

    # add player character
    dungeon.add_character(cow)

    running = True
    while running:
        run_turn = handle_input(cow, hunter, cat)

        if run_turn:
            dungeon.run_turn()

        screen.fill((0, 0, 0))
        dungeon.draw(screen, tile_set)

        pygame.display.flip()

if __name__ == '__main__':
    main()
