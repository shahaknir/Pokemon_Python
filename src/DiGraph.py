from typing import List
from NodeData import NodeData
from NodeData import EdgeData
from src import GraphInterface


class DiGraph:

    def __init__(self):
        """
        Initiate a new Graph
        """
        self.graph_nodes = {}  # <Integer, Node_data>

        self.mc = 0
        self.edge_size = 0
        self.node_size = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.node_size

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edge_size

    def get_all_v(self) -> dict:
        """
        return a dictionary of all the nodes in the Graph,
        each node is represented using a pair  (key, node_data)
        """
        return self.graph_nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
        """
        return self.graph_nodes[id1].in_edges

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        return a dictionary of all the nodes connected from node_id ,
        each node is represented using a pair (key,weight)
        """
        return self.graph_nodes[id1].out_edges

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 not in self.graph_nodes:
            return False
        if id2 not in self.graph_nodes:
            return False

        node1 = self.graph_nodes[id1]
        node2 = self.graph_nodes[id2]

        if id1 is not id2 and weight > 0:

            if id2 not in node1.out_edges:

                node1.out_edges[id2] = EdgeData(id1, id2, weight)
                node2.in_edges[id1] = EdgeData(id1, id2, weight)

                self.edge_size += 1
                self.mc += 1

                return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id in self.graph_nodes:
            return False
        self.graph_nodes[node_id] = NodeData(node_id, pos)
        self.mc += 1
        self.node_size += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """

        if node_id in self.graph_nodes:

            node = self.graph_nodes[node_id]

            # removes the dest nodes of node_id
            for o in node.out_edges:
                del self.graph_nodes[o].in_edges[node_id]

                self.edge_size -= 1

            for i in node.in_edges:
                del self.graph_nodes[i].out_edges[node_id]

            self.edge_size -= len(node.in_edges)
            self.node_size -= 1
            self.mc += 1
            del self.graph_nodes[node_id]
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """

        if node_id1 == node_id2:
            return False

        if node_id1 in self.graph_nodes and node_id2 in self.graph_nodes:

            node1 = self.graph_nodes[node_id1]
            node2 = self.graph_nodes[node_id2]

            if node_id2 in node1.out_edges:

                del node1.out_edges[node_id2]
                del node2.in_edges[node_id1]

                self.mc += 1
                self.edge_size -= 1

                return True

        return False

    """
    toString of DiGraph
    @:returns according to the definition of Python 
    """
    # |V|=4 , |E|=5
    def __str__(self):
        return f"|V|={self.node_size} , |E|={self.edge_size}"

    def __repr__(self):
        return f"|V|={self.node_size} , |E|={self.edge_size}"

    """
    isEquals for graphs
    """
    def __eq__(self, other=None):
        if other is not None:
            return self.graph_nodes == other.graph_nodes\
               and self.edge_size == other.edge_size\
               and self.node_size == other.node_size

        return False
