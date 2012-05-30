from mock import Mock
from domb.ai import ChaseAI

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

    chaser.move.assert_called_with(ChaseAI.N.x, ChaseAI.N.y)

def test_chase_south():
    target.pos = (0, 4)
    chaser.pos = (0, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.S.x, ChaseAI.S.y)

def test_chase_west():
    target.pos = (0, 0)
    chaser.pos = (2, 0)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.W.x, ChaseAI.W.y)

def test_chase_east():
    target.pos = (4, 0)
    chaser.pos = (2, 0)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.E.x, ChaseAI.E.y)


def test_chase_northwest():
    target.pos = (0, 0)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.NW.x, ChaseAI.NW.y)

def test_chase_northeast():
    target.pos = (4, 0)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.NE.x, ChaseAI.NE.y)
    
def test_chase_southwest():
    target.pos = (0, 4)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.SW.x, ChaseAI.SW.y)

def test_chase_southeast():
    target.pos = (4, 4)
    chaser.pos = (2, 2)
    
    chase_ai = ChaseAI(target)
    chase_ai.update(chaser)

    chaser.move.assert_called_with(ChaseAI.SE.x, ChaseAI.SE.y)

