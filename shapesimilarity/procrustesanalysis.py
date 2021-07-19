from .geometry import *
from .utils import *
import math

'''
from https://en.wikipedia.org/wiki/Procrustes_analysis
'''

def procrustes_normalize_curve(curve):
  '''
  Args:
    curve: type array [[x, y]], [x, y]].
  Returns:
    procrustes_normalize_curve: procrustes_normalize_curve
  Descriptions:
    Translate and scale curve by Procrustes Analysis
  '''
  
  curve_length = len(curve)
  mean_x = array_average(list(map(lambda item: item[0], curve)))
  mean_y = array_average(list(map(lambda item: item[1], curve)))
  curve = list(map(lambda item: [item[0]-mean_x, item[1]-mean_y], curve))
  
  squared_sum = 0
  for i in range(curve_length):
    squared_sum += (curve[i][0])**2 + (curve[i][1])**2
  scale = round(squared_sum / curve_length, 2)
  return list(map(lambda item: [item[0]/scale, item[1]/scale], curve))

def find_procrustes_rotation_angle(curve, relativeCurve):
  '''
  Args:
    curve: type array [[x, y]], [x, y]].
    relativeCurve: type array [[x, y]], [x, y]].
  Warnings:
    `curve` and `relativeCurve` must have the same number of points
    `curve` and `relativeCurve` should both be run through [[procrustesNormalizeCurve]] first
  Returns:
    find_procrustes_rotation_angle: the angle to rotate
  Descriptions:
    Find the angle to rotate `curve` to match the rotation
    of `relativeCurve` using procrustes analysis
  '''
  
  assert len(curve) == len(relativeCurve), 'curve and relativeCurve must have the same length'
  numerator, denominator = 0, 0
  for i in range(len(curve)):
    numerator += relativeCurve[i][0]*curve[i][1] - relativeCurve[i][1]*curve[i][0]
    denominator += relativeCurve[i][0]*curve[i][0] + relativeCurve[i][1]*curve[i][1]
  return math.atan2(numerator, denominator)

def procrustes_normalize_rotation(curve, relativeCurve):
  '''
  Args:
    curve: type array [[x, y]], [x, y]].
    relativeCurve: type array [[x, y]], [x, y]].
  Warnings:
    `curve` and `relativeCurve` must have the same number of points
    `curve` and `relativeCurve` should both be run through [[procrustesNormalizeCurve]] first
  Returns:
    procrustes_normalize_rotation: rotate
  Descriptions:
    Rotate `curve` to match the rotation of 
    `relativeCurve` using procrustes analysis
  '''

  angle = find_procrustes_rotation_angle(curve, relativeCurve)
  return rotate_curve(curve, angle)