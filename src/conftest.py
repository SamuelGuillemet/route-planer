import pytest
from network_parser import NetworkParser


@pytest.fixture
def sample_network_parser():
    test_network_parser = NetworkParser(
        "Test Network", "../fixtures/lines.json", "../fixtures/stops.json")
    print(test_network_parser.network_name + " successfully loaded !")
    return test_network_parser
