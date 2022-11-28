import pdb
from math import dist, inf
from random import randrange
from typing import List, Tuple, Set, Optional


# Helpers
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
        

class Link:
    """
    A node for a doubly linked list. I think - it's been awhile since I've messed with these.
    """
    def __init__(self, value, previous = None, next = None):
        self.value = value
        self.previous = previous
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


# Heuristics - split these into their own file
def nearest_neighbor(points: Set[Tuple[int,int]]) -> List[Tuple[int,int]]:
    remaining_points = points.copy()
    current_point = remaining_points.pop()
    tour = [current_point]
    while len(remaining_points) > 0:
        selected_point = None
        min_distance = inf
        for point in remaining_points: 
            if not selected_point: 
                selected_point = point 
                min_distance = dist(current_point, point)
            else:
                distance = dist(current_point, point)
                if distance < min_distance:
                    selected_point = point
                    min_distance = distance
        tour.append(selected_point)
        remaining_points.remove(selected_point)
        current_point = selected_point
    return tour
            

def find_shortest_new_edge(chains: List[Link]) -> Edge:
    min_edge = Edge(chains[0].head, chains[-1].head)
    for i, chain in enumerate(chains):
        for next_chain in chains[i+1:]:
            for edge in [
                Edge(chain.head, next_chain.head), 
                Edge(chain.head, next_chain.tail), 
                Edge(chain.tail, next_chain.head), 
                Edge(chain.tail, next_chain.tail),
            ]:
                if edge.length < min_edge.length:
                    min_edge = edge
    return min_edge
             

def closest_pair(points: Set[Tuple[int, int]]) -> List[Tuple[int,int]]:
    chains = { Link(point) for point in points }
    # tweak condition for new "graph" object
    while len(chains) > 1:
        new_edge = find_shortest_new_edge(list(chains))
        remove_list = []
        for chain in chains:
            if chain.is_member(new_edge.start) or chain.is_member(new_edge.end):
                remove_list.append(chain)
        for chain in remove_list:
            chains.remove(chain)
        chains.add(new_edge.connect())
    return chains.pop().to_list()
            
        
