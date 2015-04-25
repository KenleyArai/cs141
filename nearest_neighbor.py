"""
Name: Kenley Arai
"""
"""
Closest_pair
"""
# import bisect
from math import sqrt
import sys
import time
import random
import bisect
import csv

def file_input(filename):
    return csv.reader(open(filename), delimiter=" ")

def euclidean_dist(point_a, point_b):
    """
    Solves euclidean distance
    """
    return round(sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2), 100)

def closest_pair_bf(points):
    number_of_points = len(points)
    if number_of_points <= 1:
        return -1
    smallest = float("inf")
    for point_indx in range(number_of_points):
        for compare_point_indx in range(point_indx+1, number_of_points):
            smallest = min(smallest, euclidean_dist(points[point_indx], points[compare_point_indx]))
    return smallest

def closest_pair_d_and_c(points):
    if len(points) < 4:
        return closest_pair_bf(points)

    mid_point = int(len(points)/2)
    mid_x = points[mid_point][0]

    smallest_left = closest_pair_d_and_c(points[mid_point:])
    smallest_right = closest_pair_d_and_c(points[:mid_point])

    smallest = min(smallest_left, smallest_right)

    between_2_d = sorted([item for item in points if \
                        mid_x - smallest < item[0] < mid_x + smallest], key=lambda x: x[1])

    y_smallest = smallest
    for i in range(len(between_2_d) - 1):
        if(between_2_d[i+1][1] - between_2_d[i][1] < y_smallest):
            y_smallest = euclidean_dist(between_2_d[i], between_2_d[i+1])

    return min(y_smallest, smallest)

def main(argv):
    file_points = file_input(argv[0])
    points = []
    for point in file_points:
        points += [(float(point[0]), float(point[1]))]
    points = sorted(points, key=lambda x: x[0])
    with open(argv[0].split(".")[0] + "_result.txt",'w') as f:
        f.write(str(closest_pair_d_and_c(points)) + '\n')

if __name__ == "__main__":
    main(sys.argv[1:])
