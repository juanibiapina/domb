import logging
from pygame.font import SysFont
from pygame import font, Surface, Color, SRCALPHA


class Console(object):
    def __init__(self, screen):
        font.init()
        self.console = Surface((600, 85), SRCALPHA, 32)
        self.console.fill(Color(255, 255, 255, 50))
        self.font = SysFont('Arial', 14)
        screen.blit(self.console, (20, 390))

    def log(self, message):
        text_surface = self.font.render(message, False, Color(255, 255, 255))
        self.console.blit(text_surface, (10, 5))


class ConsoleLogHandler(logging.StreamHandler):
    def __init__(self, console):
        self.console = console

    def emit(self, record):
        self.console.log(record)
