import unittest
import src

class TestFrechetDistance(unittest.TestCase):
  def test_is_zero_if_the_curves_are_the_same(self):
    curve1 = [[0, 0], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertEqual(src.frechetdistance.frechet_distance(curve1, curve2), 0)
    self.assertEqual(src.frechetdistance.frechet_distance(curve2, curve1), 0)