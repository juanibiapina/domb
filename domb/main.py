import pygame
from pygame.locals import KEYUP
from console import Console, ConsoleLogHandler
from domb.view.hud import Hud
import logging

import monsters
from hero import Hero, HeroIsDead
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
    show_death_screen(screen)


def wait_for_key():
    while pygame.event.poll().type != KEYUP:
        pass


def show_death_screen(screen):
    screen_copy = screen.copy().convert_alpha()
    screen_copy.fill((0, 0, 0, 128))
    font = pygame.font.SysFont('Arial', 15)
    text_surface = font.render("You're a warm blood gushing corpse.", False, (255, 255, 255))
    text_x = screen_copy.get_width() / 2 - text_surface.get_width() / 2
    text_y = screen_copy.get_height() / 2 - text_surface.get_height() / 2
    screen_copy.blit(text_surface, (text_x, text_y))

    screen.blit(screen_copy, (0, 0))
    pygame.display.flip()
    wait_for_key()


def show_title_screen(screen):
    def display_title():
        font = pygame.font.SysFont('Arial', 46)
        text_surface = font.render('Dungeons of my Benga', False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width() / 2 - text_surface.get_width() / 2, 50))
        pygame.display.flip()

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
    hero = Hero(dungeon)
    dog = monsters.Dog(dungeon)
    cat = monsters.Cat(dungeon)
    monsters.ConstrictorSnake(dungeon)

    # create items
    dungeon.add_item(Potion(), Vec2d(3, 3))

    # set character AI
    dog.set_ai(ChaseAI(hero))
    cat.set_ai(RandomAI())

    # add some itens to see inventory
    hero.inventory.add_item(Potion())

    # create view
    inventory_view = InventoryView(hero.inventory)

    # create input handler
    input_handler = InputHandler(hero, inventory_view)

    def draw():
        screen.fill((0, 0, 0))
        dungeon.draw(screen)
        console.draw(screen)
        inventory_view.draw(screen)
        hud.draw(hero, screen)
        pygame.display.flip()

    try:
        while True:
            run_turn = input_handler.handle_input()
            if run_turn:
                dungeon.run_turn()
                draw()
    except HeroIsDead:
        draw()

if __name__ == '__main__':
    main()
