import unittest
import src

class TestSubdividedCurve(unittest.TestCase):
  def test_leave_the_curve_the_same_if_segment_lengths_are_less_than_max_len_apart(self):
    curve = [[0, 0], [4, 4]]
    self.assertEqual(
      src.geometry.subdivided_curve(curve, 10), 
      [
        [0, 0], 
        [4, 4]
      ]
    )