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

    plt.show()  # plt.savefig()


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an breadth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node for search
#     :return: list of nodes in the visited order
#     """
#     draw_graph(g)
#
#     path_nodes = []
#     visited_nodes = {node: False for node in g.nodes}  # посещенные узлы
#
#     wait_nodes = []  # стек
#     wait_nodes.append(start_node)  # добавляем в стек  / вершина справа
#     visited_nodes[start_node] = True
#
#     while wait_nodes:
#         current_node = wait_nodes.pop()
#         neighbours = g[current_node]
#
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)
#                 visited_nodes[neighbour] = True
#
#         path_nodes.append(current_node)
#
#     return path_nodes


def dfs(g: nx.Graph, start_node: Hashable):
    """
    от каждого соседа рекурсивно запустить поиск в глубину,
    то есть по факту сосед становится новым стартовым узлом.
    Подумать:
    - что должна возвращать рекурсивная функция
    - какой терминальный случай
    - как контролировать какие узлы уже посещали, чтобы дважды не пройти по тем же узлам
    """
    draw_graph(g)
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}

    def _dfs(current_node: Hashable):
        path_nodes.append(current_node)
        visited_nodes[current_node] = True

        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                _dfs(neighbour)

    _dfs(start_node)

    return path_nodes