from domb.character.xp import XP
from mock import Mock

class TestXP:

  def test_xp_level_up_using_decimal(self):
    xp = XP(1)
    xp.increase(1.0/4)
    assert xp.xp == 300
    
    xp.increase(2)
    assert xp.xp == 1200



