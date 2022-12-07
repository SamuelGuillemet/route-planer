import json


class NetworkParser:

    def __init__(self, network_name: str, lines_path: str, stops_path: str):
        self.network_name = network_name

        with open(lines_path, "rb", encoding="utf-8") as lines:
            self._lines = json.parse(lines.read)

        with open(stops_path, "rb", encoding="utf-8") as stops:
            self._stops = json.parse(stops.read)

    def get_lines():
        return self._lines

    def get_stops():
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
