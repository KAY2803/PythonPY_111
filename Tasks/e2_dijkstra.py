from typing import Hashable, Mapping, Union
import networkx as nx
import matplotlib.pyplot as plt

# graph = nx.Graph()  # ненаправленный и немультиграф
# graph.add_weighted_edges_from([
#     (1,2,7),
#     (1,3,9),
#     (1,6,14),
#     (2,3,10),
#     (2,4,15),
#     (3,4,11),
#     (3,6,2),
#     (4,5,6),
#     (5,6,9),
# ])


def dijkstra_algo(g: nx.Graph, starting_node) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """

    visited_nodes = {node: False for node in g.nodes}
    total_coasts = {node: float('inf') for node in g.nodes}
    current_node = starting_node
    total_coasts[current_node] = 0

    #while not all([v for v in visited_nodes.values()]):
    for _ in range(len(g)):
        not_visited_total_coasts = {node: coast for node, coast in total_coasts.items() if not visited_nodes[node]}
        min_v = float('inf')
        for k, v in not_visited_total_coasts.items():
            if v < min_v:
                min_v = v
                current_node = k
        visited_nodes[current_node] = True
        for neighbour_node in g[current_node]:
            weight = g[current_node][neighbour_node]['weight']
            total_coasts[neighbour_node] = min(total_coasts[neighbour_node], total_coasts[current_node] + weight)

    return total_coasts


