import random


class NodeData:

    def __init__(self, key=0, pos=(0, 0, 0), tag=False, info=" ", weight=0.0):
        """
        Initiate a new NodeData
        """
        self.key = key
        self.pos = pos
        self.info = info
        self.tag = tag
        self.weight = weight

        self.in_edges = {}  # <Integer, edge_data>
        self.out_edges = {}

    """
    toString of DiGraph
    @:returns according to the definition of Python 
    """

    def __repr__(self):
        # 0: |edges out| 1 |edges in| 1
        return f"{self.key}: |edges out| {len(self.out_edges)} |edges in| {len(self.in_edges)}"

    def __str__(self):
        return f"{self.key}: |edges out| {len(self.out_edges)} |edges in| {len(self.in_edges)}"

    def __eq__(self, other):
        return self.key == other.key \
               and self.pos == other.pos \
               and self.info == other.info \
               and self.tag == other.tag \
               and self.weight == other.weight


class EdgeData:

    def __init__(self, source=0, destination=0, weight=0.0, info=" ", tag=0):
        """
        Initiate a new NodeData
        """
        self.source = source
        self.destination = destination
        self.weight = weight
        self.info = info
        self.tag = tag

    """
    toString of DiGraph
    @:returns according to the definition of Python 
    """

    def __repr__(self):
        return f"{self.weight}"

    def __str__(self):
        return f"{self.weight}"

    def __eq__(self, other=None):
        if other is not None:
            return self.source == other.source \
                   and self.destination == other.destination \
                   and self.weight == other.weight \
                   and self.info == other.info \
                   and self.tag == other.tag
        return False
