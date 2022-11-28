import pdb
import pytest
from math import sqrt

from model import compute_tour_length, nearest_neighbor, closest_pair


def test_horizontal_compute_tour_length():
    tour = [(1,1), (1,2), (1,3)]
    expected_length = 4
    assert compute_tour_length(tour) == expected_length


def test_diagonal_compute_tour_length():
    tour = [(1,1), (2,2), (3,3)]
    expected_length = sqrt(2) * 4
    assert compute_tour_length(tour) == expected_length


def test_nearest_neighbor():
    points = {(3,1), (1,1), (2,1), (4,1)}
    expected_tour = [(3,1), (4,1), (2,1), (1,1)]
    assert nearest_neighbor(points) == expected_tour

def test_closest_pair():
    points = {(3,1), (1,1), (2,1), (4,1)}
    expected_tour = [(3,1), (4,1), (2,1), (1,1)]
    assert closest_pair(points) == expected_tour
