from random import randint


class RandomAI(object):
    def update(self, character):
        character.move(randint(-1, 1), randint(-1, 1))
