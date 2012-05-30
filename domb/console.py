import logging
from pygame.font import SysFont
from pygame import font, Surface, Color, SRCALPHA


class Console(object):
    def __init__(self):
        font.init()
        self.console = Surface((600, 85), SRCALPHA, 32)
        self._clear_log()
        self.font = SysFont('Arial', 14)
        self.messages = []

    def log(self, message):
        self.messages.append(message)
        self._clear_log()
        i = 5
        for msg in reversed(self.messages):
            text_surface = self.font.render(msg, False, Color(255, 255, 255))
            self.console.blit(text_surface, (10, i))
            i += 20

    def draw(self, screen):
        screen.blit(self.console, (20, 390))

    def _clear_log(self):
        self.console.fill(Color(255, 255, 255, 50))


class ConsoleLogHandler(logging.StreamHandler):
    def __init__(self, console):
        super(ConsoleLogHandler, self).__init__()
        self.console = console

    def emit(self, record):
        self.console.log(self.format(record))
