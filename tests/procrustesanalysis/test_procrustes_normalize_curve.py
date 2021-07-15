import unittest
import math
import src

class TestProcrustesNormalizeCurve(unittest.TestCase):
  def test_normalizes_the_scale_and_translation_of_the_curve(self):
    curve = [[0, 0], [4, 4]]
    result = src.procrustesanalysis.procrustes_normalize_curve(curve, rebalance=False)
    self.assertEqual(
      [
        [round(result[0][0], 4), round(result[0][1], 4)],
        [round(result[1][0], 4), round(result[1][1], 4)]
      ],
      [
        [round((-1 * math.sqrt(2)) / 2, 4), round((-1 * math.sqrt(2)) / 2, 4)],
        [round((math.sqrt(2)) / 2, 4), round((math.sqrt(2)) / 2, 4)]
      ]
    )
  
  def test_rebalances_with_fifty_points_by_default(self):
    curve = [[0, 0], [4, 4]]
    result = src.procrustesanalysis.procrustes_normalize_curve(curve)
    self.assertEqual(len(result), 50)
