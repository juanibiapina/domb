from domb.character.xp import XP
from mock import Mock

class TestXP:

  def test_xp_level_up_using_decimal(self):
    xp = XP(1)
    xp.increase(1.0/4)
    assert xp.xp == 75
  
  def test_xp_level_up(self):
    xp = XP(1)
    xp.increase(1)
    assert xp.xp == 300

  def test_xp_level_up_even_more(self):
    xp = XP(5)
    xp.increase(2)
    assert xp.xp == 500


