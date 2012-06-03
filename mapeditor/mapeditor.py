import sys
import pygame
from pygame.locals import KEYUP, K_ESCAPE, K_t

from tilepicker import TilePicker
from mapcreator import MapCreator


def handle_input(mapcreator, tilepicker):
    ev = pygame.event.poll()

    # general shortcuts
    if ev.type == KEYUP:
        if ev.key == K_ESCAPE:
            sys.exit(0)

        # toggle tile picker
        if ev.key == K_t:
            tilepicker.toggle()

    if tilepicker.handle_input(ev):
        return

    if mapcreator.handle_input(ev):
        return


def main():
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.init()

    # create widgets
    tilepicker = TilePicker()
    mapcreator = MapCreator(tilepicker)

    # run game loop
    running = True
    while running:
        handle_input(mapcreator, tilepicker)

        # clear screen
        screen.fill((0, 0, 0))

        # do drawing
        mapcreator.draw(screen)
        tilepicker.draw(screen)

        # flip to screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
