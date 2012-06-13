import logging
from pygame.font import SysFont
from pygame import font, Surface, Color, SRCALPHA


class Console(object):
    def __init__(self):
        self.console = Surface((600, 85), SRCALPHA, 32)
        self._clear_log()
        font.init()
        self.font = SysFont('Arial', 14)
        self.messages = []

    def log(self, message):
        self.messages.append(message)

    def draw(self, screen):
        msgs = self.messages[-4:len(self.messages)]
        msgs.reverse()
        self._clear_log()
        i = 65
        for msg in msgs:
            text_surface = self.font.render(msg, False, Color(255, 255, 255))
            self.console.blit(text_surface, (10, i))
            i -= 20
        screen.blit(self.console, (20, 670))

    def _clear_log(self):
        self.console.fill(Color(255, 255, 255, 50))


class ConsoleLogHandler(logging.StreamHandler):
    def __init__(self, console):
        super(ConsoleLogHandler, self).__init__()
        self.console = console

    def emit(self, record):
        self.console.log(self.format(record))
