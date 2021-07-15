import unittest
import math
import src

class TestFindProcrustesRotationAngle(unittest.TestCase):
  def test_determines_the_optimal_rotation_angle_to_match_2_curves_on_top_of_each_other(self):
    curve1 = src.procrustesanalysis.procrustes_normalize_curve([[0, 0], [1, 0]])
    curve2 = src.procrustesanalysis.procrustes_normalize_curve([[0, 0], [0, 1]])
    self.assertEqual(
      src.procrustesanalysis.find_procrustes_rotation_angle(curve1, curve2),
      (-1 * math.pi) / 2
    )