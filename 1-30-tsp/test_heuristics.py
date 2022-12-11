from heuristics import nearest_neighbor, closest_pair, find_shortest_new_edge


def test_nearest_neighbor():
    points = {(3, 1), (1, 1), (2, 1), (4, 1)}
    expected_tour = [(3, 1), (4, 1), (2, 1), (1, 1)]
    assert nearest_neighbor(points) == expected_tour


def test_closest_pair():
    points = {(3, 1), (1, 1), (2, 1), (4, 1)}
    expected_tour = [(3, 1), (4, 1), (2, 1), (1, 1)]
    assert closest_pair(points) == expected_tour
