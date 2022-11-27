from math import dist
from random import randrange
from typing import List, Tuple


def get_random_points(plane_size: int, number_of_points:int) -> set:
    """ 
    A collection of randomly generated points for the Traveling Salesman Problem.
    
    Inputs: size (edge length) the containing square plane, number of points to generate.
    Output: set of points 
    Points are unique tuples of integers.
    """
    points = set()
    while len(points) < number_of_points:
        points.add((randrange(plane_size), randrange(plane_size)))
    return points


def compute_tour_length(tour: List[Tuple[int,int]]) -> float:
    tour_length = 0
    # start with previous_point set the final point b/c this is a closed tour 
    previous_point = tour[-1]
    for point in tour:
        tour_length += dist(point, previous_point)
        previous_point = point 
    return tour_length
        

# Heuristics
def nearest_neighbor(points: set) -> List[Tuple[int,int]]:
    pass


def closest_pair(points: set) -> List[Tuple[int,int]]:
    pass
