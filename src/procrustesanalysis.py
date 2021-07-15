from .geometry import *
from .utils import *
import math

'''
from https://en.wikipedia.org/wiki/Procrustes_analysis
'''
def procrustes_normalize_curve(curve, rebalance=True, estimationPoints=50):
  '''
  Args:
    curve: type array [[x, y]], [x, y]].
    rebalance: Optionally runs default True
    estimationPoints: Optionally runs default 50
  Returns:
    procrustes_normalize_curve: procrustes_normalize_curve
  Descriptions:
    Translate and scale curve by Procrustes Analysis
  '''
  balanced_curve = rebalance_curve(curve, estimationPoints) if rebalance else curve
  mean_x = array_average(list(map(lambda item: item[0], balanced_curve)))
  mean_y = array_average(list(map(lambda item: item[1], balanced_curve)))
  mean = [mean_x, mean_y]
  translated_curve = list(map(lambda point: substract(point, mean), balanced_curve))
  scale = math.sqrt(array_average(list(map(lambda item: item[0]*item[0] + item[1]*item[1], translated_curve))))
  return list(map(lambda item: [item[0] / scale, item[1] / scale], translated_curve))

'''
from https://en.wikipedia.org/wiki/Procrustes_analysis
'''
def find_procrustes_rotation_angle(curve, relativeCurve):
  '''
  Args:
    curve: type array [[x, y]], [x, y]].
    relativeCurve: type array [[x, y]], [x, y]].
  Warnings:
    `curve` and `relativeCurve` must have the same number of points
    `curve` and `relativeCurve` should both be run through [[procrustesNormalizeCurve]] first
  Returns:
    find_procrustes_rotation_angle: rotation_angle
  Descriptions:
    Find the angle to rotate `curve` to match the rotation
    of `relativeCurve` using procrustes analysis
  '''
  assert len(curve) == len(relativeCurve), 'curve and relativeCurve must have the same length'
  numerator, denominator = 0, 0
  for i in range(0, len(curve)):
    numerator += curve[i][1] * relativeCurve[i][0] - curve[i][0] * relativeCurve[i][1]
    denominator += curve[i][0] * relativeCurve[i][0] + curve[i][1] * relativeCurve[i][1]
  return math.atan2(numerator, denominator)