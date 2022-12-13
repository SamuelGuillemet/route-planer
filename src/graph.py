from typing import List
from node import Node

class GraphException(Exception):
    pass


class Graph:
    def __init__(self):
        self.nodes: List[Node] = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def get_node_in_graph(self, node_name: str) -> Node:
        for _node in self.nodes:
            if _node.name == node_name:
                return _node
        raise GraphException("Node not found in graph")

    def get_neighbors(self, node: Node) -> List[Node]:
        return node.get_neighbors_list()

    def get_weight(self, node1: Node, node2: Node) -> float:
        if node2 in self.get_neighbors(node1):
            return node1.get_distance(node2)
        return float('inf')

    def dijkstra_algorithm_distance(self, start_node: Node):
        visited = {}
        distance = {}
        parents = {}

        # Initial distance to all nodes is infinity
        for _node in  self.nodes:
            if _node != start_node:
                distance[_node] = float('inf')
                visited[_node] = False
            else:
                distance[_node] = 0
                visited[_node] = True

        # Compteur
        compteur = 0

        current_node = start_node
        initial_distance = 0


        while compteur < len(self.nodes) -1:
            # Find the node with the smallest distance
            min_distance = float('inf')
            next_possible_node = None
            for test_node in self.nodes:
                if visited[test_node] is False:
                    ditance_between_nodes = self.get_weight(current_node, test_node)
                    total_distance = initial_distance + ditance_between_nodes

                    if total_distance < distance[test_node]:
                        distance[test_node] = total_distance
                        parents[test_node] = current_node

                    if distance[test_node] < min_distance:
                        min_distance = distance[test_node]
                        next_possible_node = test_node


            compteur += 1

            if next_possible_node is None:
                raise GraphException("Unable to find a path")

            current_node = next_possible_node
            visited[current_node] = True
            initial_distance = distance[current_node]

        return parents

    def dijkstra_algorithm(self, start_node: Node, stop_node: Node) -> List[Node]:
        parents = self.dijkstra_algorithm_distance(start_node)

        path = []

        node = stop_node
        path.append(node)

        while node != start_node:
            node = parents[node]
            path.append(node)

        return list(reversed(path))
