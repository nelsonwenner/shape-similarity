import unittest
import math
import src

class TestProcrustesNormalizeRotation(unittest.TestCase):
  def test_rotates_a_normalized_curve_to_match_the_rotation_of_another_normalized_curve(self):
    curve = src.procrustesanalysis.procrustes_normalize_curve([[0, 0], [1, 0]])
    relative_curve = src.procrustesanalysis.procrustes_normalize_curve([[0, 0], [0, 1]])
    rotated_curve = src.procrustesanalysis.procrustes_normalize_rotation(curve, relative_curve)
    self.assertEqual(
      list(map(lambda item: [round(item[0], 4), round(item[1], 4)], rotated_curve)),
      list(map(lambda item: [round(item[0], 4), round(item[1], 4)], rotated_curve))
    )