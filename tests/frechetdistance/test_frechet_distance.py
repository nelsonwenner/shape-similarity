from shapesimilarity import frechet_distance
import unittest

class TestFrechetDistance(unittest.TestCase):
  def test_is_zero_if_the_curves_are_the_same(self):
    curve1 = [[0, 0], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertEqual(frechet_distance(curve1, curve2), 0)
    self.assertEqual(frechet_distance(curve2, curve1), 0)

  def test_will_be_the_dist_of_the_starting_points_if_those_are_the_only_difference(self):
    curve1 = [[1, 0], [4, 4]]
    curve2 = [[0, 0], [4, 4]]
    self.assertEqual(frechet_distance(curve1, curve2), 1)
    self.assertEqual(frechet_distance(curve2, curve1), 1)
  
  def test_gives_correct_result_one(self):
    curve1 = [[1, 0], [2.4, 43], [-1, 4.3], [4, 4]]
    curve2 = [[0, 0], [14, 2.4], [4, 4]]
    self.assertEqual(
      round(frechet_distance(curve1, curve2), 4), 
      39.03
    )

  def test_gives_correct_results_two(self):
    curve1 = [
      [63.44852183813086, 24.420192387119634],
      [19.472881275654252, 77.306125067647],
      [22.0150089075698, 5.115699052924483],
      [90.85925658487311, 80.37914225209231],
      [96.81784894898642, 81.33960258698878],
      [75.45756084113779, 96.87017085629488],
      [87.77706429291412, 15.70163068744641],
      [37.36893642596093, 44.86136460914203],
      [37.35720453846581, 90.65479959420186],
      [41.28185352889147, 34.02195976325355],
      [27.65820587389076, 12.382281496757997],
      [42.43674529129338, 33.38959395979349],
      [3.377463737709774, 52.387593489371966],
      [50.93481600582428, 16.868378936261696],
      [68.46675900966153, 52.04265123799294],
      [1.9235036598383326, 55.87935516876048],
      [28.02334783421687, 98.08317663407114],
      [53.74539146366855, 33.27918237496243],
      [49.39670128874036, 47.59663728140997],
      [47.51990428391566, 11.23339071630216],
      [53.31256301680558, 55.4279696833061],
      [38.797168750480026, 26.172634107810833],
      [45.604650160570515, 71.69212699940685],
      [36.83931368726911, 38.74324014933978],
      [68.76987877419623, 1.2518741233677577],
      [91.27606575268427, 96.2141050404784],
      [24.407614843135406, 76.20115332073458],
      [8.764170623754097, 37.003392529458104],
      [52.97112238152346, 9.76631343977752],
      [88.85357966283867, 60.767524033054144]
    ]
    curve2 = [[0, 0], [14, 2.4], [4, 4]]
    self.assertEqual(
      round(frechet_distance(curve1, curve2), 4), 
      121.54
    )
  
  def test_not_overflow_the_node_stack_if_the_curves_are_very_long(self):
    curve1 = [[x**0.2, x**0.2] for x in range(5000)]
    curve2 = [[x**0.4, x**0.4] for x in range(5000)]
    self.assertEqual(frechet_distance(curve1, curve2), 34.9)