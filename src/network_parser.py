import json


class NetworkParser:

    def __init__(self, network_name: str, lines_path: str, stops_path: str):
        self.network_name = network_name

        with open(lines_path, "r", encoding="utf-8") as lines:
            self._lines = json.load(lines)

        with open(stops_path, "r", encoding="utf-8") as stops:
            stops = json.load(stops)
            for i, stop in enumerate(stops):
                stops[i]["id"] = i
            self._stops = stops

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
