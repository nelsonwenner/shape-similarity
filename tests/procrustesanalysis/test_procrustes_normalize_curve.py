from shapesimilarity import procrustes_normalize_curve
import unittest

class TestProcrustesNormalizeCurve(unittest.TestCase):
  def test_normalizes_the_scale_and_translation_of_the_curve(self):
    curve = [[0, 0], [4, 4]]
    result = procrustes_normalize_curve(curve)
    self.assertEqual(result, [[-0.25, -0.25], [0.25, 0.25]])