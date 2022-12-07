class NeighborError(Exception):
    pass


class Node:
    def __init__(self, id, name, lignes, lon, lat, neighbors=[]):
        self.id = id
        self.name = name
        self.lignes = lignes
        self.lon = lon
        self.lat = lat
        self.neighbors = neighbors

    def add_neighbor(self, node):
        if node in self.neighbors:
            raise NeighborError("Node already in neighbors")
        else:
            if not set(self.lignes).intersection(node.lignes):
                raise NeighborError("No common ligne")
            else:
                self.neighbors.append(node)
                node.neighbors.append(self)

    def remove_neighbor(self, node):
        if node not in self.neighbors:
            raise NeighborError("Node not in neighbors")
        else:
            self.neighbors.remove(node)
            node.neighbors.remove(self)
