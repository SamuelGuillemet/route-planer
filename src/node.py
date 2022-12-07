class NeighborError(Exception):
    pass


class Node:
    def __init__(self, id, name, id_lines, lon, lat, neighbors=[]):
        self.id = id
        self.name = name
        self.id_lines = id_lines
        self.lon = lon
        self.lat = lat
        self.neighbors = neighbors

    def add_neighbor(self, node):
        if node in self.neighbors:
            raise NeighborError("Node already in neighbors")
        else:
            if not set(self.id_lines).intersection(node.id_lines):
                raise NeighborError("No common line")
            else:
                self.neighbors.append(node)
                node.neighbors.append(self)

    def remove_neighbor(self, node):
        if node not in self.neighbors:
            raise NeighborError("Node not in neighbors")
        else:
            self.neighbors.remove(node)
            node.neighbors.remove(self)
