import pygame
from console import Console, ConsoleLogHandler
from domb.view.hud import Hud
import logging

import monsters
from area import generate_dungeon
import tiles
from ai import ChaseAI, RandomAI
from view.inventory import InventoryView
from items import Potion
from vec2d import Vec2d
from controls.inputhandler import InputHandler


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
    cow.inventory.add_item(Potion())

    # create views
    inventory_view = InventoryView(cow.inventory)

    # create input handler
    input_handler = InputHandler(cow, inventory_view)

    # run game loop
    running = True
    while running:
        run_turn = input_handler.handle_input()

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
