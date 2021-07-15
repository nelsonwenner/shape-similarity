import unittest
import src

class TestFrechetDistance(unittest.TestCase):
  def test_is_zero_if_the_curves_are_the_same(self):
    curve1 = [[0, 0], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertEqual(src.frechetdistance.frechet_distance(curve1, curve2), 0)
    self.assertEqual(src.frechetdistance.frechet_distance(curve2, curve1), 0)

  def test_less_than_then_max_length_of_any_segment_if_curves_are_identical(self):
    curve1 = [[0, 0], [2, 2], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertLess(
      src.frechetdistance.frechet_distance(
        src.geometry.subdivided_curve(curve1, 0.5),
        src.geometry.subdivided_curve(curve2, 0.5)
      ),
      0.5
    )
    self.assertLess(
      src.frechetdistance.frechet_distance(
        src.geometry.subdivided_curve(curve1, 0.1),
        src.geometry.subdivided_curve(curve2, 0.1)
      ),
      0.1
    )
    self.assertLess(
      src.frechetdistance.frechet_distance(
        src.geometry.subdivided_curve(curve1, 0.01),
        src.geometry.subdivided_curve(curve2, 0.01)
      ),
      0.01
    )

  def test_will_be_the_dist_of_the_starting_points_if_those_are_the_only_difference(self):
    curve1 = [[1, 0], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertEqual(src.frechetdistance.frechet_distance(curve1, curve2), 1)
    self.assertEqual(src.frechetdistance.frechet_distance(curve2, curve1), 1)

  def test_gives_correct_result_one(self):
    curve1 = [[1, 0], [2.4, 43], [-1, 4.3], [4, 4]]
    curve2 = [[0, 0], [14, 2.4], [4, 4]]
    self.assertEqual(
      round(src.frechetdistance.frechet_distance(curve1, curve2), 4), 
      39.0328
    )
