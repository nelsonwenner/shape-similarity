import unittest
import src

class TestRebalanceCurve(unittest.TestCase):
  def test_divides_a_curve_into_equally_spaced_segments(self):
    curve1 = [[0, 0], [4, 6]]
    self.assertEqual(
      src.geometry.rebalance_curve(curve1, 3), 
      [
        [0, 0],
        [2, 3],
        [4, 6]
      ]
    )
    curve2 = [[0, 0], [9, 12], [0, 24]]
    self.assertEqual(
      src.geometry.rebalance_curve(curve2, 4),
      [ 
        [0, 0],
        [6, 8],
        [6, 16],
        [0, 24]
      ]
    )