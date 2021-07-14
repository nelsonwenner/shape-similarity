import unittest
import src

class TestExtendPointOnLine(unittest.TestCase):
  def test_returns_a_point_distance_away_from_the_end_point(self):
    point1, point2 = [0, 0], [8, 6]
    self.assertEqual(
      src.geometry.extend_point_on_line(point1, point2, 5), 
      [12, 9]
    )
  
  def test_works_with_negative_distances(self):
    point1, point2 = [0, 0], [8, 6]
    self.assertEqual(
      src.geometry.extend_point_on_line(point1, point2, -5), 
      [4, 3]
    )

  def test_works_when_p2_is_before_p1_in_the_line(self):
    point1, point2 = [12, 9], [8, 6]
    self.assertEqual(
      src.geometry.extend_point_on_line(point1, point2, 10), 
      [0, 0]
    )