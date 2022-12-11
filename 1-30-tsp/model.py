from math import dist
from random import randrange
from typing import List, Tuple


# Helpers
def get_random_points(plane_size: int, number_of_points: int) -> set:
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


def compute_tour_length(tour: List[Tuple[int, int]]) -> float:
    tour_length = 0
    # start with previous_point set the final point b/c this is a closed tour
    previous_point = tour[-1]
    for point in tour:
        tour_length += dist(point, previous_point)
        previous_point = point
    return tour_length


class Link:
    """
    A node for a linked list.
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    @property
    def head(self):
        current_link = self
        while current_link.previous:
            current_link = current_link.previous
        return current_link

    @property
    def tail(self):
        current_link = self
        while current_link.next:
            current_link = current_link.next
        return current_link

    def to_list(self):
        current_node = self.head
        node_list = [current_node]
        while current_node.next:
            node_list.append(current_node.value)
        return node_list

    def is_member(self, other) -> bool:
        current = self.head
        while current.next:
            if current.value == other.value:
                return True
        return False


class LinkedList:
    def __init__(self):
        pass


# I think we should delete this, in favor of a list or dictionary. If the graph doesn't
# use this Edge class, it will confuse me down the line.
class Edge:
    def __init__(self, start: Link, end: Link):
        self.start = start
        self.end = end
        self.length = dist(self.start.value, self.end.value)

    def connect(self):
        if not self.start.previous and not self.end.next:
            self.start.previous = self.end
            self.end.next = self.start
        elif not self.start.next and not self.end.previous:
            self.start.next = self.end
            self.end.previous = self.start
        else:
            raise RuntimeError("cannot connect edge, no empty connection points")
        return self.start.head


class Graph:
    """
    Represents a collection of verticies and edges.

    A 'vertex' is a tuple of integers.
    An 'edge' is a set of two vertices.
    A 'chain' is a set of connected vertices without branches.
    """

    def __init__(self, verticies, edges=None):
        self._verticies = verticies
        self._edges = edges

    @property
    def verticies(self):
        return self._verticies

    @property
    def edges(self):
        return self._edges

    @property
    def chains(self):
        pass

    def add(self, vertex):
        pass

    def remove(self, vertex):
        pass

    def connect(self, vertex_1, vertex_2):
        pass

    def disconnect(self, vertex_1, vertex_2):
        pass

    def are_adjacent(self, vertex_1, vertex_2):
        pass

    def get_adjacent(self, vertex):
        pass
