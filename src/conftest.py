import pytest
from network_parser import NetworkParser
from node import Node


@pytest.fixture
def sample_network_parser():
    test_network_parser = NetworkParser(
        "Test Network", "../fixtures/lines.json", "../fixtures/stops.json")
    return test_network_parser

@pytest.fixture
def node_samples():
    id_node = 1
    name = "station01"
    id_lines = [1, 2]
    lat, lon = [48.861675, 2.346786]
    node_1 = Node(id_node, name, id_lines, [lon, lat])
    id_node = 2
    name = "station02"
    id_lines = [1]
    lat, lon = [48.854921, 2.347367]
    node_2 = Node(id_node, name, id_lines, [lon, lat])
    return (node_1, node_2)
