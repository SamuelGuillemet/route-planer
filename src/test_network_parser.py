from node import Node


def test_name_definition(sample_network_parser) -> bool:
    assert len(sample_network_parser.network_name) > 0


def test_lines_loading(sample_network_parser) -> bool:
    assert len(sample_network_parser.get_lines()) > 0


def test_stops_loading(sample_network_parser) -> bool:
    assert len(sample_network_parser.get_stops()) > 0


def test_stop_node_initializing(sample_network_parser) -> bool:
    for stop in sample_network_parser.get_stops():
        if not isinstance(stop, Node):
            assert False
    assert True


def test_string_conversion(sample_network_parser) -> bool:
    assert str(sample_network_parser).startswith("Parser of ")
