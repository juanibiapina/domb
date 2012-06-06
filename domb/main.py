import pygame
from pygame.locals import KEYUP
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

    show_title_screen(screen)
    play_game(screen)


def show_title_screen(screen):
    def display_title():
        font = pygame.font.SysFont('Arial', 46)
        text_surface = font.render('Dungeons of my Benga', False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width() / 2 - text_surface.get_width() / 2, 50))
        pygame.display.flip()

    def wait_for_key():
        while pygame.event.poll().type != KEYUP:
            pass

    display_title()
    wait_for_key()


def play_game(screen):
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
    monsters.ConstrictorSnake(dungeon)

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
