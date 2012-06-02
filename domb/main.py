from pygame.locals import (KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE,
                           K_a, K_s, K_w, K_d, K_i, K_e)
import pygame
import sys
from console import Console, ConsoleLogHandler
from hud import Hud
import logging

import monsters
from area import generate_dungeon
import tiles
from ai import ChaseAI, RandomAI
from view.inventory import InventoryView
import directions
from items import Potion
from vec2d import Vec2d

LEFT = directions.W
RIGHT = directions.E
TOP = directions.N
DOWN = directions.S


def handle_input(cow, inventory_view):
    ev = pygame.event.poll()
    if ev.type == KEYUP:
        if ev.key == K_DOWN:
            cow.move(DOWN)
        if ev.key == K_UP:
            cow.move(TOP)
        if ev.key == K_LEFT:
            cow.move(LEFT)
        if ev.key == K_RIGHT:
            cow.move(RIGHT)
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
        if ev.key == K_e:
            cow.pick_up_item()
        if ev.key == K_i:
            inventory_view.toggle()
            return False
        return True
    return False


def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.init()
    pygame.font.init()

    # dungeon
    dungeon = generate_dungeon(tiles)

    # hud
    hud = Hud()

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

    # create items
    dungeon.add_item(Potion(), Vec2d(3, 3))

    # set character AI
    dog.set_ai(ChaseAI(cow))
    cat.set_ai(RandomAI())

    # add some itens to see inventory
    cow.inventory.add_item("foo")
    cow.inventory.add_item("bar")
    cow.inventory.add_item("baz")

    inventory_view = InventoryView(cow.inventory)

    running = True
    while running:
        run_turn = handle_input(cow, inventory_view)

        if run_turn:
            dungeon.run_turn()

        screen.fill((0, 0, 0))
        dungeon.draw(screen)
        console.draw(screen)
        inventory_view.draw(screen)
        hud.draw(cow, screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
