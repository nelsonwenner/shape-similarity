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

  def test_can_be_configured_to_rebalance_with_a_custom_number_of_points(self):
    curve = [[0, 0], [4, 4]]
    result = src.procrustesanalysis.procrustes_normalize_curve(curve, estimationPoints=3)
    self.assertEqual(
      [
        [round(result[0][0], 4), round(result[0][1], 4)],
        [result[1][0], result[1][1]],
        [round(result[2][0], 4), round(result[2][1], 4)]
      ],
      [
        [round((-1 * math.sqrt(3)) / 2, 4), round((-1 * math.sqrt(3)) / 2, 4)],
        [0, 0],
        [round((math.sqrt(3)) / 2, 4), round((math.sqrt(3)) / 2, 4)]
      ]
    )

  def test_gives_identical_results_for_identical_curves_with_different_numbers_of_points_after_rebalancing(self):
    curve1 = [[0, 0], [4, 4]]
    curve2 = [[0, 0], [3, 3], [4, 4]]
    result1 = src.procrustesanalysis.procrustes_normalize_curve(curve1)
    result2 = src.procrustesanalysis.procrustes_normalize_curve(curve2)
    self.assertEqual(
      list(map(lambda item: [round(item[0], 4), round(item[1], 4)], result1)),
      list(map(lambda item: [round(item[0], 4), round(item[1], 4)], result2))
    )