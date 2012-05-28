from random import randint
from math import fabs


class RandomAI(object):
    def update(self, character):
        character.move(randint(-1, 1), randint(-1, 1))


class ChaseAI(object):
    def __init__(self, hero):
        self.hero = hero

    def update(self, character):
        heroX = self.hero.pos[0]
        heroY = self.hero.pos[1]
        enemyX = character.pos[0]
        enemyY = character.pos[1]

        dirX = heroX - enemyX
        dirY = heroY - enemyY

        dirX = 0 if (dirX == 0) else dirX / fabs(dirX)
        dirY = 0 if (dirY == 0) else dirY / fabs(dirY)

        character.move(dirX, dirY)
        
