from math import dist, inf
from typing import List, Tuple, Set 

from model import *

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
