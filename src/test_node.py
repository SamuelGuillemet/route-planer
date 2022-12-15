import pytest
from node import Node, NeighborError

def test_nodes(node_samples):
    node_1: Node = node_samples[0]
    assert node_1.id == 1
    assert node_1.name == "station01"
    assert node_1.id_lines == [1, 2]
    assert node_1.lat == 48.861675
    assert node_1.lon == 2.346786
    node_2: Node = node_samples[1]
    assert node_2.id == 2
    assert node_2.name == "station02"
    assert node_2.id_lines == [1]
    assert node_2.lat == 48.854921
    assert node_2.lon == 2.347367


def test_neighbors(node_samples):
    node_1: Node = node_samples[0]
    node_2: Node = node_samples[1]
    # test Add
    node_1.add_neighbor(node_2)
    assert node_2 in node_1.get_neighbors_list()
    assert node_1 in node_2.get_neighbors_list()
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_2)
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_1)


def test_invalid_neighbors(node_samples):
    node_1: Node = node_samples[0]
    node_2: Node = node_samples[1]
    node_1.id_lines = ["1"]
    node_2.id_lines = ["2"]
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_2)
    with pytest.raises(NeighborError):
        node_2.add_neighbor(node_1)
