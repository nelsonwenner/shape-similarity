from shapesimilarity import extend_point_on_line
import unittest

class TestExtendPointOnLine(unittest.TestCase):
  def test_returns_a_point_distance_away_from_the_end_point(self):
    point1, point2 = [0, 0], [8, 6]
    self.assertEqual(
      extend_point_on_line(point1, point2, 5), 
      [4.0, 3.0]
    )
  
  def test_works_with_negative_distances(self):
    point1, point2 = [0, 0], [8, 6]
    self.assertEqual(
      extend_point_on_line(point1, point2, -5), 
      [12.0, 9.0]
    )

  def test_works_when_p2_is_before_p1_in_the_line(self):
    point1, point2 = [12, 9], [8, 6]
    self.assertEqual(
      extend_point_on_line(point1, point2, 10), 
      [16.0, 12.0]
    )

  def test_works_with_vertical_lines(self):
    point1, point2 = [2, 4], [2, 6]
    self.assertEqual(
      extend_point_on_line(point1, point2, 7), 
      [2.0, -1.0]
    )

  def test_works_with_vertical_lines_where_p2_is_above_p1(self):
    point1, point2 = [2, 6], [2, 4]
    self.assertEqual(
      extend_point_on_line(point1, point2, 7), 
      [2.0, 11.0]
    )