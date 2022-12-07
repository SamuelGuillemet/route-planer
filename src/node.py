import math

class NeighborError(Exception):
    pass

class Node:
    def __init__(self, id_node, name, id_lines, location):
        self.id = id_node
        self.name = name
        self.id_lines = id_lines
        self.lon = location[0]
        self.lat = location[1]
        self.neighbors = []

    def get_neighbors_list(self):
        neighbors = []
        for node in self.neighbors:
            neighbors.append(node['node'])
        return neighbors

    def add_neighbor(self, node):
        if node == self:
            raise NeighborError("Node is itself")
        if node in self.get_neighbors_list():
            raise NeighborError("Node already in neighbors")
        if not set(self.id_lines).intersection(node.id_lines):
            raise NeighborError("No common line")
        weight = round(self.get_distance(node), 2)
        self.neighbors.append({'node':node, 'weight':weight})
        node.neighbors.append({'node':self, 'weight':weight})

    def remove_neighbor(self, node):
        if node not in self.get_neighbors_list():
            raise NeighborError("Node not in neighbors")
        for node_element in self.neighbors:
            if node_element['node'] == node:
                self.neighbors.remove(node_element)
        for node_element in node.neighbors:
            if node_element['node'] == self:
                node.neighbors.remove(node_element)
    
    def get_distance(self, node):
        lat_node = node.lat*math.pi/180
        lon_node = node.lon*math.pi/180
        lat_self = self.lat*math.pi/180
        lon_self = self.lon*math.pi/180
        return math.acos(math.sin(lat_self) * math.sin(lat_node) + math.cos(lat_self) * math.cos(lat_node) * math.cos(lon_self - lon_node)) * 6378137
