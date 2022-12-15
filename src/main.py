import sys
from graph import Graph
from network_parser import NetworkParser


def path_to_string(_res):
    path = _res[0].name + " \n-> "
    for i in range(1, len(_res)):
        path += _res[i].name + " (via "
        for line in _res[i].id_lines:
            if i == len(_res) - 1:
                path += line + ")"
                break
            if line in _res[i - 1].id_lines:
                path += line + ") \n-> "
                break
        else:
            path += "Unknown line -> "
    return path


if __name__ == "__main__":
    DEPART = sys.argv[1]
    ARRIVE = sys.argv[2]

    graph = Graph()
    parser = NetworkParser("Paris", "../fixtures/lines.json", "../fixtures/stops.json")
    gares = parser.get_stops()
    for station in gares:
        graph.add_node(station)

    start_node = graph.get_node_in_graph(DEPART)
    stop_node = graph.get_node_in_graph(ARRIVE)

    res = graph.dijkstra_algorithm(start_node, stop_node)

    print(path_to_string(res))
