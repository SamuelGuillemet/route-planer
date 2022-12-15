from typing import List
import math

class NeighborError(Exception):
    pass

class Node:
    def __init__(self, id_node, name, id_lines, location):
        self.id = id_node
        self.name = name
        self.id_lines: List[str] = id_lines
        self.lon = location[0]
        self.lat = location[1]
        self.neighbors: List[Node] = []

    def get_neighbors_list(self):
        return self.neighbors

    def add_neighbor(self, node: "Node"):
        if node == self:
            raise NeighborError("Node is itself")
        if node in self.get_neighbors_list():
            raise NeighborError("Node already in neighbors")
        if not set(self.id_lines).intersection(node.id_lines):
            raise NeighborError("No common line")
        self.neighbors.append(node)
        node.neighbors.append(self)

    def get_distance(self, node):
        lat_node = node.lat*math.pi/180
        lon_node = node.lon*math.pi/180
        lat_self = self.lat*math.pi/180
        lon_self = self.lon*math.pi/180
        res = math.acos(math.sin(lat_self) * math.sin(lat_node)
        + math.cos(lat_self) * math.cos(lat_node) * math.cos(lon_self - lon_node)) * 6378137
        return round(res, 2)
