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