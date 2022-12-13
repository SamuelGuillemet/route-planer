import json
from typing import List
from node import NeighborError, Node


class NetworkParser:

    def __init__(self, network_name: str, lines_path: str, stops_path: str):
        self.network_name = network_name
        
        self.dict_lines = {}

        self._lines = None
        with open(lines_path, "r", encoding="utf-8") as lines:
            self._lines = json.load(lines)

        self._stops: List[Node] = []
        with open(stops_path, "r", encoding="utf-8") as stops:
            stops = json.load(stops)
            for i in range(len(stops)):
                name = stops[i]["name"] if stops[i]["name"] else "Unknown Station"
                lines_for_neighbor = stops[i]["lines"]
                lines = [stops[i]["lines"][j]["line"]
                         for j in range(len(stops[i]["lines"]))] if stops[i]["lines"] else []
                location = (stops[i]["longitude"], stops[i]["latitude"]) if (
                    stops[i]["longitude"] or stops[i]["latitude"]) else (0, 0)

                node = Node(i, name, lines, location)
                for line_i in lines_for_neighbor:
                    if line_i["line"] not in self.dict_lines:
                        self.dict_lines[line_i["line"]] = []
                    self.dict_lines[line_i["line"]].append((node, line_i["position"]))
                self._stops.append(node)
            # print(dict_lines)
            # We sort the lines by position
            for line in self.dict_lines:
                self.dict_lines[line].sort(key=lambda x: x[1])
            #print(dict_lines)
            # We add the neighbors
            for line in self.dict_lines:
                for i in range(len(self.dict_lines[line]) - 1):
                    try:
                        # We check if the position is the next one
                        self.dict_lines[line][i][0].add_neighbor(self.dict_lines[line][i + 1][0])
                    except NeighborError:
                        pass

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
