from typing import Hashable, List
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show() #plt.savefig()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    draw_graph(g)
    path_nodes = []  # сгоревшие узлы по порядку их горения
    visited_nodes = {node: False for node in
                     g.nodes}  # посещенные узлы (которые уже сгорели полностью или которые еще горят)

    wait_nodes = deque() # очередь из горящих узлов, ожидающих поджечь своих соседей
    wait_nodes.append(start_node) # добавляем в конец очереди узел
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.popleft() # забираем горящий узел с начала очереди
        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour) # конец очереди справа
                visited_nodes[neighbour] = True
        path_nodes.append(current_node)

    print(g, start_node)
    return path_nodes

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    draw_graph(graph)
    print(bfs(graph, 'A'))