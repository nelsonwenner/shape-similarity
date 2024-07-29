from shapesimilarity import procrustes_normalize_curve
import unittest
import cupy as cp
import cupy.testing as cpt

class TestProcrustesNormalizeCurve(unittest.TestCase):
  def test_normalizes_the_scale_and_translation_of_the_curve(self):
    curve = [[0, 0], [4, 4]]
    result = procrustes_normalize_curve(curve)
    print(result)
    cpt.assert_array_equal(result, cp.asarray([[-0.25, -0.25], [0.25, 0.25]]))
    


if __name__ == '__main__':
    unittest.main()