from mock import Mock
from domb.ai import ChaseAI
from domb import directions

room = Mock(name="room")
target = Mock(name="target")
chaser = Mock(name="chaser")

target.get_room.return_value = room
chaser.get_room.return_value = room

def test_chase_north():
    target.pos = (0, 0)
    chaser.pos = (0, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.N)

def test_chase_south():
    target.pos = (0, 4)
    chaser.pos = (0, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.S)

def test_chase_west():
    target.pos = (0, 0)
    chaser.pos = (2, 0)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.W)

def test_chase_east():
    target.pos = (4, 0)
    chaser.pos = (2, 0)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.E)


def test_chase_northwest():
    target.pos = (0, 0)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.NW)

def test_chase_northeast():
    target.pos = (4, 0)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.NE)
    
def test_chase_southwest():
    target.pos = (0, 4)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.SW)

def test_chase_southeast():
    target.pos = (4, 4)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(directions.SE)

