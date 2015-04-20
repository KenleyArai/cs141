from .. import nearest_neighbor
import bisect

def test_dist():
    point_a = (1,2)
    point_b = (3,4)
    assert nearest_neighbor.euclidean_dist(point_a,point_b) == 2.82843

def test_bf():
    points = [(5.1, 8.7),
              (-1.2, 3.7),
              (-4.5, -6.1),
              (12.7, 14.21),
              (1.6, 3.1),
              (7.9, 15.13),
              (18.4, -25.3),
              (11.2, -6.3),
              (7.1, -3.9),
              (4.6, 2.9)]
    assert nearest_neighbor.closest_pair_bf(points) == 2.86356

def test_rec():
    points = []
    bisect.insort_right(points, (5.1, 8.7))
    bisect.insort_right(points, (-1.2, 3.7))
    bisect.insort_right(points, (-4.5, -6.1))
    bisect.insort_right(points, (12.7, 14.21))
    bisect.insort_right(points, (1.6, 3.1))
    bisect.insort_right(points, (7.9, 15.13))
    bisect.insort_right(points, (18.4, -25.3))
    bisect.insort_right(points, (11.2, -6.3))
    bisect.insort_right(points, (7.1, -3.9))
    bisect.insort_right(points, (4.6, 2.9))
    assert nearest_neighbor.closest_pair_d_and_c(points) == 2.86356


def test_rec2():
    points = []
    bisect.insort_right(points, (2,3))
    bisect.insort_right(points, (12, 30))
    bisect.insort_right(points, (40, 50))
    bisect.insort_right(points, (5, 1))
    bisect.insort_right(points, (12, 10))
    bisect.insort_right(points, (3, 4))

    assert nearest_neighbor.closest_pair_d_and_c(points) == 1.41421


