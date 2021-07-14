
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

