import sys
from pygame.locals import (KEYUP, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE,
                           K_a, K_s, K_w, K_d, K_t, K_e,
                           K_h, K_j, K_k, K_l,
                           K_u, K_i, K_y, K_o)
import pygame
from domb.vec2d import Vec2d

import directions

LEFT = directions.W
RIGHT = directions.E
TOP = directions.N
DOWN = directions.S


class InputHandler(object):
    def __init__(self, player_character, inventory_view, camera):
        self.player_character = player_character
        self.inventory_view = inventory_view
        self.camera = camera

    def handle_input(self):
        ev = pygame.event.poll()
        if ev.type == KEYUP:

            # exit game
            if ev.key == K_ESCAPE:
                sys.exit(0)

            # toggle inventory
            if ev.key == K_t:
                self.inventory_view.toggle()
                return False

            if self.inventory_view.is_active():  # inventory controls
                if ev.key == K_LEFT:
                    self.inventory_view.previous_item()
                if ev.key == K_RIGHT:
                    self.inventory_view.next_item()
                if ev.key == K_e:
                    self.player_character.use_current_item()
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
                    self.player_character.do_attack(LEFT)
                if ev.key == K_s:
                    self.player_character.do_attack(DOWN)
                if ev.key == K_d:
                    self.player_character.do_attack(RIGHT)
                if ev.key == K_w:
                    self.player_character.do_attack(TOP)
                if ev.key == K_e:
                    self.player_character.pick_up_item()
                if ev.key == K_u:
                    self.player_character.open_door(DOWN)
                if ev.key == K_i:
                    self.player_character.open_door(TOP)
                if ev.key == K_y:
                    self.player_character.open_door(LEFT)
                if ev.key == K_o:
                    self.player_character.open_door(RIGHT)
                return True
        return False
