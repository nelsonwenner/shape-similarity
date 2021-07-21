from shapesimilarity import array_average
import unittest

class TestArrayAverage(unittest.TestCase):
  def test_returns_the_average_of_all_elements_in_the_array(self):
    self.assertEqual(array_average([1, 3, 5]), 3)