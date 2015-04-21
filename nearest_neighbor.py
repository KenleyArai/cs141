#!/usr/bin/env python

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

def makeData(num):
    points = []
    for _ in xrange(num):
        bisect.insort_right(points, (random.uniform(0,100), random.uniform(0,100)))
    return points

def file_input(filename):
    return csv.reader(open(filename), delimiter=" ")

def euclidean_dist(point_a, point_b):
    """
    Solves euclidean distance
    """
    return round(sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2), 5)

def closest_pair_bf(points):
    """
    This is the brute force version of closest pair
    """
    number_of_points = len(points)
    if number_of_points <= 1:
        return -1
    smallest = float("inf")
    for point_indx in range(number_of_points):
        for compare_point_indx in range(point_indx+1, number_of_points):
            smallest = min(smallest, euclidean_dist(points[point_indx], points[compare_point_indx]))
    return smallest

def closest_pair_d_and_c(points):
    """
    This is the divide and conqour version of closest pair
    """
    if len(points) < 4:
        return closest_pair_bf(points)

    mid_point = int(len(points)/2)
    mid_x = points[mid_point][0]

    smallest_left = closest_pair_d_and_c(points[mid_point:])
    smallest_right = closest_pair_d_and_c(points[:mid_point])

    smallest = min(smallest_left, smallest_right)

    between_2_d = closest_pair_bf([item for item in points if \
                  item[0] > mid_x - smallest and item[0] < mid_x + smallest])

    if between_2_d == -1:
        return smallest
    return min(smallest, between_2_d)


def graph(points):
    print "#>title,Closest Point"
    print "#>xAxis,Number of Points"
    print "#>yAxis,Time in Seconds"
    for i in xrange(0,len(points), 10):
        time1 = time.time()
        result1 = closest_pair_bf(points[:i])
        time2 = time.time()
        print "#>BruteForce,",len(points[:i]),",",time2-time1
        time3 = time.time()
        result2 = closest_pair_d_and_c(points[:i])
        time4 = time.time()
        print "#>DivideAndConquer,",len(points[:i]),",",time4-time3
        sys.stdout.flush() #Needed to make graph update in real time


def main(argv):
    file_points = file_input(argv[0])
    points = []
    for point in file_points:
        bisect.insort_right(points, (float(point[0]), float(point[1])))
    #graph(points)
    print closest_pair_bf(points)

if __name__ == "__main__":
    main(sys.argv[1:])
