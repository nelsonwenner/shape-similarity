from .procrustesanalysis import *
from .frechetdistance import *
from .geometry import *
import math

def shape_similarity(shape1, shape2, rotations=10, checkRotation=True):
  procrustes_normalized_curve1 = procrustes_normalize_curve(shape1)
  procrustes_normalized_curve2 = procrustes_normalize_curve(shape2)
  geo_avg_curve_len = math.sqrt(
    curve_length(procrustes_normalized_curve1) * 
    curve_length(procrustes_normalized_curve2)
  )

  thetas_to_check = [0]
  if checkRotation:
    procrustes_theta = find_procrustes_rotation_angle(
      procrustes_normalized_curve1, 
      procrustes_normalized_curve2
    )
    # use a negative rotation rather than a large positive rotation
    if procrustes_theta > math.pi:
      procrustes_theta = procrustes_theta - 2 * math.pi
    if procrustes_theta != 0 and abs(procrustes_theta) < math.pi:
      thetas_to_check.append(procrustes_theta)
    for i in range(0, rotations):
      theta = -1 * math.pi + (2 * i * math.pi) / (rotations - 1)
      # 0 and Math.PI are already being checked, no need to check twice
      if theta != 0 and theta != math.pi:
        thetas_to_check.append(theta)

  # Using Frechet distance to check the similarity level 
  min_frechet_distance = float('inf')
  # check some other thetas here just in case the procrustes theta isn't the best rotation
  for theta in thetas_to_check:
    rotated_curve1 = rotate_curve(procrustes_normalized_curve1, theta)
    frechet_dist = frechet_distance(rotated_curve1, procrustes_normalized_curve2)
    if frechet_dist < min_frechet_distance:
      min_frechet_distance = frechet_dist
  # divide by Math.sqrt(2) to try to get the low results closer to 
  result = max(1 - min_frechet_distance / (geo_avg_curve_len / math.sqrt(2)), 0)
  return round(result, 4)