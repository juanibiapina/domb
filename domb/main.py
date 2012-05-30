from pygame.locals import KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE, K_a, K_s, K_w, K_d
import pygame
import sys
from console import Console, ConsoleLogHandler
import logging

import monsters
from area import generate_dungeon
from tileset import tiles
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

    # dungeon
    dungeon = generate_dungeon(tiles)

    # console
    console = Console()
    logger = logging.getLogger('console')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ConsoleLogHandler(console))
    logger.info('Welcome to Dungeons of my Benga')

    # create characters
    monsters.Wolf(dungeon)
    cow = monsters.Cow(dungeon)
    dog = monsters.Dog(dungeon)
    cat = monsters.Cat(dungeon)

    # set character AI
    dog.set_ai(ChaseAI(cow))
    cat.set_ai(RandomAI())

    running = True
    while running:
        run_turn = handle_input(cow)

        if run_turn:
            dungeon.run_turn()

        screen.fill((0, 0, 0))
        dungeon.draw(screen)
        console.render(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
