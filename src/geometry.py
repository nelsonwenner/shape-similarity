
def magnitude(point):
  '''
  Args:
    point: type array two values [x, y].
  Returns:
    Magnitude.
  Descriptions:
    The magnitude of a vector AB is the distance
    between start point A and endpoint B.
  '''
  return math.sqrt(point[0]*point[0] + point[1]*point[1])

def substract(point1, point2):
  '''
  Args:
    point1: type array two values [x, y].
    point2: type array two values [x, y].
  Returns:
    A new point [x, y]
  Descriptions:
    Subtraction is the operation of taking 
    the difference between two numbers.
  '''
  return [point1[0] - point2[0], point1[1] - point2[1]]
def point_distance(point1, point2):
  '''
  Args:
    point1: type array two values [x, y].
    point2: type array two values [x, y].
  Returns:
    Magnitude.
  Descriptions:
    Calculate the distance between 2 points.
  '''
  return magnitude(substract(point1, point2))

def curve_length(points):
  '''
  Args:
    points: type arrays two values [[x, y], [x, y]].
  Returns:
    acc_length: curve length.
  Descriptions:
    Calculate the length of the curve.
  '''
  acc_length = 0
  for index in range(0, len(points) - 1):
    acc_length += point_distance(points[index], points[index + 1])
  return acc_length
def extend_point_on_line(point1, point2, distance):
  '''
  Args:
    point1: type array two values [x, y].
    point2: type array two values [x, y].
    distance: type float.
  Returns:
    A new point, point3, which is on the same
    line generated by point1 and point2.
  '''
  vector = substract(point2, point1)
  norm = distance / magnitude(vector)
  new_point_x = point2[0] + norm * vector[0]
  new_point_y = point2[1] + norm * vector[1]
  return [new_point_x, new_point_y]

def subdivided_curve(curve, maxLen=0.05):
  '''
  Args:
    curve: type array two values [[x, y], [x, y]].
    maxLen: max length
  Returns:
    new_curve: new curve
  Descriptions:
    Break up long segments in the curve into 
    smaller segments of len maxLen or smaller
  '''
  new_curve = [curve[0]]
  for idx in range(1, len(curve)):
    prev_point = new_curve[len(new_curve) - 1]
    segment_length = point_distance(curve[idx], prev_point)
    if segment_length > maxLen:
      num_new_points = int(math.ceil(segment_length / maxLen))
      new_segment_length = segment_length / num_new_points
      for idj in range(num_new_points):
        new_curve.append(
          extend_point_on_line(
            curve[idx], prev_point, 
            -1 * new_segment_length * (idj+1)
          )
        )
    else:
      new_curve.append(curve[idx])
  return new_curve
