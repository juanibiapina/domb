from pygame import Surface, Color, SRCALPHA
from pygame.font import SysFont


class Hud(object):
    def __init__(self):
        self.hud = Surface((65, 50), SRCALPHA, 32)
        self.font = SysFont('Arial', 14)

    def draw(self, character, screen):
        self._clear()
        hp = character.hp.current_value
        ac = character.get_ac().get_value()
        hp_surface = self.font.render('HP: ' + str(hp), False, Color(255, 255, 255))
        ac_surface = self.font.render('AC: ' + str(ac), False, Color(255, 255, 255))
        self.hud.blit(hp_surface, (10, 5))
        self.hud.blit(ac_surface, (10, 25))
        screen.blit(self.hud, (550, 10))

    def _clear(self):
        self.hud.fill(Color(255, 255, 0, 50))
