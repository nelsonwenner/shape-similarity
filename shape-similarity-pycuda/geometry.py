import cupy as cp


def euclidean_distance(point1, point2):
    point1 = cp.array(point1)
    point2 = cp.array(point2)
    return cp.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2).item()


def pairwise_distance(curve_slice):
    return euclidean_distance([curve_slice[0], curve_slice[1]], [curve_slice[2], curve_slice[3]])


def curve_length(curve):
    consecutive_points = cp.hstack((curve[:-1], curve[1:]))
    distances = cp.apply_along_axis(pairwise_distance, 1, consecutive_points)
    return cp.sum(distances)


def extend_point_on_line(point1, point2, distance):
    point1 = cp.array(point1)
    point2 = cp.array(point2)
    norm = round(distance / euclidean_distance(point1, point2), 2)
    new_point_x = point2[0] + norm * (point1[0] - point2[0])
    new_point_y = point2[1] + norm * (point1[1] - point2[1])
    return cp.array([new_point_x, new_point_y])


def rotate_point(point, cos_theta, sin_theta):
    x_cord = cos_theta * point[0] - sin_theta * point[1]
    y_cord = sin_theta * point[0] + cos_theta * point[1]
    return cp.array([x_cord, y_cord])


def rotate_curve(curve, thetaRad):
    cos_theta = cp.cos(-1 * thetaRad)
    sin_theta = cp.sin(-1 * thetaRad)
    rot_curve = cp.apply_along_axis(rotate_point, 1, curve, cos_theta, sin_theta)
    return rot_curve