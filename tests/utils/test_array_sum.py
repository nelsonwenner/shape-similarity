from shapesimilarity import array_sum
import unittest

class TestArraySum(unittest.TestCase):
  def test_returns_the_sum_of_all_elements_in_the_array(self):
    self.assertEqual(array_sum([1, 3, 5]), 9)

  def test_returns_0_for_empty_arrays(self):
    self.assertEqual(array_sum([]), 0)