import sys
from pygame.locals import (KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE,
                           K_a, K_s, K_w, K_d, K_i, K_e)
import pygame

import directions

LEFT = directions.W
RIGHT = directions.E
TOP = directions.N
DOWN = directions.S


class InputHandler(object):
    def __init__(self, player_character, inventory_view):
        self.player_character = player_character
        self.inventory_view = inventory_view

    def handle_input(self):
        ev = pygame.event.poll()
        if ev.type == KEYUP:

            # exit game
            if ev.key == K_ESCAPE:
                sys.exit(0)

            # toggle inventory
            if ev.key == K_i:
                self.inventory_view.toggle()
                return False

            if self.inventory_view.is_active():  # inventory controls
                return False
            else:
                if ev.key == K_DOWN:
                    self.player_character.move(DOWN)
                if ev.key == K_UP:
                    self.player_character.move(TOP)
                if ev.key == K_LEFT:
                    self.player_character.move(LEFT)
                if ev.key == K_RIGHT:
                    self.player_character.move(RIGHT)
                if ev.key == K_a:
                    self.player_character.attack(LEFT)
                if ev.key == K_s:
                    self.player_character.attack(DOWN)
                if ev.key == K_d:
                    self.player_character.attack(RIGHT)
                if ev.key == K_w:
                    self.player_character.attack(TOP)
                if ev.key == K_e:
                    self.player_character.pick_up_item()
                return True
        return False
