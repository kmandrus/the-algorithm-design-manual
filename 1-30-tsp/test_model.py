import pytest
from math import sqrt

from model import compute_tour_length, Graph


@pytest.fixture
def line_slope_1():
    return {"verticies": [(1,1), (2,2), (3,3)], "edges": [{(1,1), (2,2)}, {(2,2), (3,3)}]}

def test_horizontal_compute_tour_length():
    tour = [(1,1), (1,2), (1,3)]
    expected_length = 4
    assert compute_tour_length(tour) == expected_length


def test_diagonal_compute_tour_length():
    tour = [(1,1), (2,2), (3,3)]
    expected_length = sqrt(2) * 4
    assert compute_tour_length(tour) == expected_length


def test_init_graph_verticies(line_slope_1):
    graph = Graph(line_slope_1["verticies"])
    
    assert graph.verticies == line_slope_1["verticies"]


def test_init_graph_edges(line_slope_1):
    graph = Graph(line_slope_1["verticies"], line_slope_1["edges"])
    
    assert graph.edges == line_slope_1["edges"]
