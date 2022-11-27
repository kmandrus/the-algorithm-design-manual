import pytest
from math import sqrt

from model import compute_tour_length

@pytest.fixture()
def horizontal_tour():
    return [(1,1), (1,2), (1,3)]


@pytest.fixture()
def horizontal_tour_length():
    return 4


@pytest.fixture()
def diagonal_tour():
    return [(1,1), (2,2), (3,3)]


@pytest.fixture()
def diagonal_tour_length():
    return sqrt(2) * 4


def test_horizontal_compute_tour_length(horizontal_tour, horizontal_tour_length):
    assert compute_tour_length(horizontal_tour) == horizontal_tour_length


def test_diagonal_compute_tour_length(diagonal_tour, diagonal_tour_length):
    assert compute_tour_length(diagonal_tour) == diagonal_tour_length
