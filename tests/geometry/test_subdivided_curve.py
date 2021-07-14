import unittest
import math
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

  def test_breaks_up_segments_so_that_each_segment_is_less_than_max_len_length(self):
    curve = [[0, 0], [4, 4], [0, 8]]
    self.assertEqual(
      src.geometry.subdivided_curve(curve, math.sqrt(2)), 
      [
        [0, 0], 
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4],
        [3, 5],
        [2, 6],
        [1, 7],
        [0, 8]
      ]
    )