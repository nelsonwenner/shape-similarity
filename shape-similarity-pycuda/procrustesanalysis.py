import cupy as cp
from geometry import *


def calculate_procrustes_components(pair):
  rc, c = [pair[0], pair[1]], [pair[2], pair[3]]
  numerator_component = rc[0] * c[1] - rc[1] * c[0]
  denominator_component = rc[0] * c[0] + rc[1] * c[1]
  return cp.array([numerator_component, denominator_component])


def find_procrustes_rotation_angle(curve, relativeCurve):
  assert len(curve) == len(relativeCurve), 'curve and relativeCurve must have the same length'
  pairs = cp.hstack((relativeCurve, curve))
  components = cp.apply_along_axis(calculate_procrustes_components, 1, pairs)
  numerator = cp.sum(components[:, 0])
  denominator = cp.sum(components[:, 1])
  return cp.arctan2(numerator, denominator)


def compute_scale(curve):
  return cp.sum(curve[:, 0] ** 2 + curve[:, 1] ** 2)


def scale_point(point, scale):
  return cp.array([point[0] / scale, point[1] / scale])


def procrustes_normalize_curve(curve):
  curve = cp.asarray(curve)
  curve_length = len(curve)
  mean = cp.mean(curve, axis=0)
  curve = curve - mean

  squared_sum = compute_scale(curve)
  scale = squared_sum / curve_length
  normalized_curve = cp.apply_along_axis(scale_point, 1, curve, scale)

  return normalized_curve


def procrustes_normalize_rotation(curve, relativeCurve):
  assert len(curve) == len(relativeCurve), 'curve and relativeCurve must have the same length'
  curve = cp.asarray(curve)
  relativeCurve = cp.asarray(relativeCurve)
  angle = find_procrustes_rotation_angle(curve, relativeCurve)
  return rotate_curve(curve, angle)