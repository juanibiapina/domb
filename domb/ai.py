from random import randint
from vec2d import Vec2d
import directions

class RandomAI(object):
    def update(self, character):
        character.move(randint(-1, 1), randint(-1, 1))


class ChaseAI(object):
    def __init__(self, chase_target):
        self.chase_target = chase_target

    def update(self, chaser):
        chase_target_pos = Vec2d(self.chase_target.pos)
        chaser_pos = Vec2d(chaser.pos)

        intended_dir_to_chase = chase_target_pos - chaser_pos
        actual_dir_to_chase = self._get_dir_to_move(intended_dir_to_chase)

        if self.chase_target.get_room() == chaser.get_room():
            chaser.move(actual_dir_to_chase.x, actual_dir_to_chase.y)
            close = (chase_target_pos - Vec2d(chaser.pos)).get_length()
            if close <= 1.0:
                chaser.attack_pos(self.chase_target.pos)

    def _get_dir_to_move(self, our_vec):
        def dot_to_dir(dir_vec):
            return our_vec.normalized().dot(dir_vec.normalized())
        return max(directions.all, key=dot_to_dir)
