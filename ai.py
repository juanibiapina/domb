from random import randint
from math import fabs

from vec2d import Vec2d

class RandomAI(object):
    def update(self, character):
        character.move(randint(-1, 1), randint(-1, 1))

class ChaseAI(object):
    N = Vec2d(0, -1)
    S = Vec2d(0, 1)
    W = Vec2d(-1, 0)
    E = Vec2d(1, 0)
    NE = N+E
    SE = S+E
    NW = N+W
    SW = S+W
    DIRECTIONS = [N, S, E, W, NE, NW, SE, SW]

    def __init__(self, chase_target):
        self.chase_target = chase_target

    def update(self, chaser):
        chase_target_pos = Vec2d(self.chase_target.pos)
        chaser_pos = Vec2d(chaser.pos)

        intended_dir_to_chase = chase_target_pos - chaser_pos
        actual_dir_to_chase = self._get_dir_to_move(intended_dir_to_chase)

        chaser.move(actual_dir_to_chase.x, actual_dir_to_chase.y)
        
    def _get_dir_to_move(self, our_vec):
        def dot_to_dir(dir_vec):
            return our_vec.normalized().dot(dir_vec.normalized())
        return max(self.DIRECTIONS, key=dot_to_dir)
