from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_a, K_s, K_w, K_d
from pygame.font import SysFont
from pygame import Surface, Color, SRCALPHA
import pygame
import sys

import monsters
from area import generate_dungeon
from character import Character
from tileset import TileSetManager
from ai import ChaseAI, RandomAI

LEFT = (-1, 0)
RIGHT = (1, 0)
TOP = (0, -1)
DOWN = (0, 1)

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
        if ev.key == K_s:
            cow.attack(DOWN)
        if ev.key == K_d:
            cow.attack(RIGHT)
        if ev.key == K_w:
            cow.attack(TOP)
        return True
    return False


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()
    pygame.font.init()

    # tiles
    tiles = TileSetManager("resources/tiles.yaml")
    blood_tile = tiles.get("BLOOD")

    # dungeon
    dungeon = generate_dungeon(tiles)

    # console
    console = Surface((600, 85), SRCALPHA, 32)
    console.fill(Color(255, 255, 255, 50))
    console_font = SysFont('Arial', 14)

    # create characters
    monsters.Wolf(dungeon)
    cow = monsters.Cow(dungeon)
    hunter = monsters.Hunter(dungeon)
    cat = monsters.Cat(dungeon)

    # set character AI
    hunter.set_ai(ChaseAI(cow))
    cat.set_ai(RandomAI())

    running = True
    while running:
        run_turn = handle_input(cow)

        if run_turn:
            dungeon.run_turn()

        screen.fill((0, 0, 0))
        dungeon.draw(screen)
        screen.blit(console, (20, 390))
        welcome_text = console_font.render('Welcome to Dungeons of my Benga', False, Color(255, 255, 255))
        console.blit(welcome_text, (10, 5))

        pygame.display.flip()

if __name__ == '__main__':
    main()
