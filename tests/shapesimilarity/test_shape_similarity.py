from shapesimilarity import shape_similarity
import unittest

class TestShapeSimilarity(unittest.TestCase):
  def test_returns_close_to_1_if_curves_have_similar_shapes(self):
    curve1 = [[0, 0], [2, 4], [18, -3]]
    curve2 = [[0.3, -0.2], [2.2, 4.5], [16, -4]]
    self.assertEqual(shape_similarity(curve1, curve2), 0.9127)

  def test_returns_low_numbers_for_curves_with_dissimilar_shapes(self):
    curve1 = [[0, 0], [2, 4], [4, 0], [0, 0]]
    curve2 = [[0, 0], [2, 2], [2, 2], [1, 1]]
    self.assertEqual(shape_similarity(curve1, curve2), 0.4792)

  def test_should_be_really_close_to_0_for_very_dissimilar_shapes(self):
    curve1 = [[0, 0], [0.1, 0.1], [0.1, 0.1], [1, 1]]
    curve2 = [[7, 7], [4, 4], [4, 4], [5, 5]]
    self.assertEqual(shape_similarity(curve1, curve2), 0)