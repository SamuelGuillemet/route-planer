import pytest

from graph import Graph, GraphException
from node import Node

def test_dijkstra_algorithm_directly_connected_nodes():
    # Create a graph with two nodes that are directly connected
    graph = Graph()
    node1 = Node(1, "Node 1", ["Line 1", "Line 2"], (0, 0))
    node2 = Node(2, "Node 2", ["Line 2", "Line 3"], (0, 1))
    node1.add_neighbor(node2)
    graph.add_node(node1)
    graph.add_node(node2)

    # Test that the dijkstra_algorithm() method returns the correct path
    # from node1 to node2
    path = graph.dijkstra_algorithm(node1, node2)
    assert path == [node1, node2]

def test_dijkstra_algorithm_indirectly_connected_nodes():
    # Create a graph with three nodes that are indirectly connected
    graph = Graph()
    node1 = Node(1, "Node 1", ["Line 1", "Line 2"], (0, 0))
    node2 = Node(2, "Node 2", ["Line 2", "Line 3"], (0, 1))
    node3 = Node(3, "Node 3", ["Line 3", "Line 4"], (1, 0))
    node1.add_neighbor(node2)
    node2.add_neighbor(node3)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)

    # Test that the dijkstra_algorithm() method returns the correct path
    # from node1 to node3
    path = graph.dijkstra_algorithm(node1, node3)
    assert path == [node1, node2, node3]

def test_dijkstra_algorithm_simple_graph():
    # Create a graph with three nodes that are indirectly connected
    graph = Graph()
    node1 = Node(1, "Node 1", ["Line 1", "Line 2"], (0, 0))
    node2 = Node(2, "Node 2", ["Line 2", "Line 3"], (0, 1))
    node3 = Node(3, "Node 3", ["Line 3", "Line 4"], (1, 0))
    node1.add_neighbor(node2)
    node2.add_neighbor(node3)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)

    # Test that the dijkstra_algorithm() method returns the correct path
    # from node1 to node3
    path = graph.dijkstra_algorithm(node1, node3)
    assert path == [node1, node2, node3]

def test_dijkstra_algorithm_disconnected_nodes():
    # Create a graph with two nodes that are not connected
    graph = Graph()
    node1 = Node(1, "Node 1", ["Line 1", "Line 2"], (0, 0))
    node2 = Node(2, "Node 2", ["Line 3"], (0, 1))
    graph.add_node(node1)
    graph.add_node(node2)

    # Test that the dijkstra_algorithm() method returns None
    # when given a start node and a stop node that are not connected
    with pytest.raises(GraphException):
        path = graph.dijkstra_algorithm(node1, node2)


def test_get_node_in_graph():
    # Create a graph with two nodes
    graph = Graph()
    node1 = Node(1, "Node 1", ["Line 1", "Line 2"], (0, 0))
    node2 = Node(2, "Node 2", ["Line 2", "Line 3"], (0, 1))
    graph.add_node(node1)
    graph.add_node(node2)

    # Test that the get_node_in_graph() method returns the correct node
    assert graph.get_node_in_graph("Node 1") == node1
    with pytest.raises(GraphException):
        graph.get_node_in_graph("Node 3")
