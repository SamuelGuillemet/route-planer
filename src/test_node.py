from node import Node, NeighborError
import pytest


@pytest.fixture
def node_samples():
    id = 1
    name = "station01"
    lignes = ["ligne1", "ligne2"]
    lon, lat = [13.2, 10.1]
    node_1 = Node(id, name, lignes, lon, lat)
    id = 2
    name = "station02"
    lignes = ["ligne1"]
    lon, lat = [13.2, 10.0]
    node_2 = Node(id, name, lignes, lon, lat)
    return (node_1, node_2)


def test_nodes(node_samples):
    node_1 = node_samples[0]
    assert node_1.id == 1
    assert node_1.name == "station01"
    assert node_1.lignes == ["ligne1", "ligne2"]
    assert node_1.lon == 13.2
    assert node_1.lat == 10.1
    node_2 = node_samples[1]
    assert node_2.id == 2
    assert node_2.name == "station02"
    assert node_2.lignes == ["ligne1"]
    assert node_2.lon == 13.2
    assert node_2.lat == 10.0


def test_neighbors(node_samples):
    node_1, node_2 = node_samples
    # test Add
    node_1.add_neighbor(node_2)
    assert node_2 in node_1.neighbors
    assert node_1 in node_2.neighbors
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_2)
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_1)
    # test Remove
    node_2.remove_neighbor(node_1)
    assert node_2 not in node_1.neighbors
    assert node_1 not in node_2.neighbors
    with pytest.raises(NeighborError):
        node_1.remove_neighbor(node_2)


def test_invalid_neighbors(node_samples):
    node_1, node_2 = node_samples
    node_1.lignes = ["ligne1"]
    node_2.lignes = ["ligne2"]
    with pytest.raises(NeighborError):
        node_1.add_neighbor(node_2)
    with pytest.raises(NeighborError):
        node_2.add_neighbor(node_1)
