from pygame import Surface, Color, SRCALPHA
from pygame.font import SysFont


class Hud(object):
    def __init__(self):
        self.hud = Surface((65, 70), SRCALPHA, 32)
        self.font = SysFont('Arial', 14)

    def draw(self, character, screen):
        self._clear()
        hp = character.hp.value
        ac = character.ac.get_value()
        xp = character.get_xp()
        hp_surface = self.font.render('HP: ' + str(hp), False, Color(255, 255, 255))
        ac_surface = self.font.render('AC: ' + str(ac), False, Color(255, 255, 255))
        xp_surface = self.font.render('XP: ' + str(xp), False, Color(255, 255, 255))
        self.hud.blit(hp_surface, (10, 5))
        self.hud.blit(ac_surface, (10, 25))
        self.hud.blit(xp_surface, (10, 45))
        screen.blit(self.hud, (550, 10))

    def _clear(self):
        self.hud.fill(Color(255, 255, 0, 50))
