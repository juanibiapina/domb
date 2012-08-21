import pygame
from pygame.locals import KEYUP
from console import Console, ConsoleLogHandler
from domb.view.hud import Hud
import logging

import monsters
from monsters import WolfIsDead
from hero import Hero, HeroIsDead
from domb.generation.area import generate_dungeon
import tiles
from ai import ChaseAI, RandomAI
from view.inventory import InventoryView
from domb.item.items import Potion
from domb.item.weapons import Longsword
from controls.inputhandler import InputHandler
from domb.view.camera import Camera
from domb.view.dungeon import DungeonView
from domb.generation.placement import place_hero, place_monster, place_item


def main():
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.init()
    pygame.font.init()

    show_title_screen(screen)

    play_game(screen)


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


def show_win_screen(screen):
    screen_copy = screen.copy().convert_alpha()
    screen_copy.fill((0, 0, 0, 128))
    font = pygame.font.SysFont('Arial', 15)
    text_surface = font.render("The princess is in another castle.", False, (255, 255, 255))
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

    # Camera
    camera = Camera(screen)

    # hud
    hud = Hud()

    # console
    console = Console()
    logger = logging.getLogger('console')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(ConsoleLogHandler(console))
    logger.info('Welcome to Dungeons of my Benga')

    # create characters
    hero = Hero()
    wolf = monsters.Wolf()
    dog = monsters.Dog()
    cat = monsters.Cat()
    constrictor_snake = monsters.ConstrictorSnake()

    camera.follow(hero)

    # place hero and monsters
    place_hero(dungeon, hero)
    place_monster(dungeon, wolf)
    place_monster(dungeon, dog)
    place_monster(dungeon, cat)
    place_monster(dungeon, constrictor_snake)

    # create items
    for i in xrange(10):
        place_item(dungeon, Potion())
    place_item(dungeon, Longsword())

    # set character AI
    dog.set_ai(ChaseAI(hero))
    cat.set_ai(RandomAI())
    wolf.set_ai(ChaseAI(hero))

    # add some itens to see inventory
    hero.inventory.add_item(Potion())

    # create view
    inventory_view = InventoryView(hero.inventory)

    # create input handler
    input_handler = InputHandler(hero, inventory_view, camera)

    dungeon_view = DungeonView(dungeon)

    def draw():
        screen.fill((0, 0, 0))
        dungeon_view.draw(screen, camera)
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
        show_death_screen(screen)
    except WolfIsDead:
        draw()
        show_win_screen(screen)


if __name__ == '__main__':
    main()
