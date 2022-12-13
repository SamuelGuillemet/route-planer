import json
from node import Node, NeighborError


class NetworkParser:

    def __init__(self, network_name: str, lines_path: str, stops_path: str):
        self.network_name = network_name

        self._lines = None
        with open(lines_path, "r", encoding="utf-8") as lines:
            self._lines = json.load(lines)

        self._stops = []
        with open(stops_path, "r", encoding="utf-8") as stops:

            stops = json.load(stops)
            for i in range(len(stops)):
                name = stops[i]["name"] if stops[i]["name"] else "Unknown Station"
                lines = [stops[i]["lines"][j]["line"]
                         for j in range(len(stops[i]["lines"]))] if stops[i]["lines"] else []
                location = (stops[i]["longitude"], stops[i]["latitude"]) if (
                    stops[i]["longitude"] or stops[i]["latitude"]) else (0, 0)

                node = Node(i, name, lines, location)

                self._stops.append(node)

    def get_lines(self):
        return self._lines

    def get_stops(self):
        return self._stops

    def __str__(self) -> str:
        number_of_lines = len(self._lines)
        number_of_stops = len(self._stops)

        return ("Parser of " +
                self.network_name +
                " with " +
                str(number_of_lines) +
                " lines" +
                str(number_of_stops) +
                " stops.")
