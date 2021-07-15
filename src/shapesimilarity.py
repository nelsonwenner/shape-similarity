from .procrustesanalysis import *
from .frechetdistance import *
from .geometry import *
import math

def shape_similarity(
  shape1, shape2, 
  estimationPoints=50,
  rotations=10,
  restrictRotationAngle=math.pi,
  checkRotations=True
  ):

  assert abs(restrictRotationAngle) <= math.pi, 'restrictRotationAngle cannot be larger than PI'
  normalized_curve1 = procrustes_normalize_curve(shape1, estimationPoints=estimationPoints)
  normalized_curve2 = procrustes_normalize_curve(shape2, estimationPoints=estimationPoints)
  geo_avg_curve_len = math.sqrt(curve_length(normalized_curve1) * curve_length(normalized_curve2))
  thetas_to_check = [0]
  if checkRotations:
    procrustes_theta = find_procrustes_rotation_angle(normalized_curve1, normalized_curve2)
    # use a negative rotation rather than a large positive rotation
    if procrustes_theta > math.pi:
      procrustes_theta = procrustes_theta - 2 * math.pi
    if procrustes_theta != 0 and abs(procrustes_theta) < restrictRotationAngle:
      thetas_to_check.append(procrustes_theta)
    for i in range(0, rotations):
      theta = -1 * restrictRotationAngle + (2 * i * restrictRotationAngle) / (rotations - 1)
      # 0 and Math.PI are already being checked, no need to check twice
      if theta != 0 and theta != math.pi:
        thetas_to_check.append(theta)

    # Using Frechet distance to check the similarity level 
    min_frechet_distance = float('inf')
    # check some other thetas here just in case the procrustes theta isn't the best rotation
    for theta in thetas_to_check:
      rotated_curve1 = rotate_curve(normalized_curve1, theta)
      distance = frechet_distance(rotated_curve1, normalized_curve2)
      if distance < min_frechet_distance:
        min_frechet_distance = distance
    # divide by Math.sqrt(2) to try to get the low results closer to 
    result = max(1 - min_frechet_distance / (geo_avg_curve_len / math.sqrt(2)), 0)
    return round(result, 4)