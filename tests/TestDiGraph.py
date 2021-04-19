import unittest
from src import DiGraph
from src import NodeData
from NodeData import NodeData
from NodeData import EdgeData
from src import GraphAlgo
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def create_graph() -> DiGraph:
    """
    Creates a new graph
    :return: DiGraph
    """
    graph = DiGraph()

    # add 10 nodes to the graph
    for i in range(1, 11):
        graph.add_node(i)

    # connects = 10
    graph.add_edge(1, 2, 20)
    graph.add_edge(2, 3, 5)
    graph.add_edge(2, 4, 90)
    graph.add_edge(2, 6, 7)
    graph.add_edge(3, 7, 21)
    graph.add_edge(4, 2, 1)
    graph.add_edge(5, 10, 1)
    graph.add_edge(7, 9, 12)
    graph.add_edge(8, 9, 1)
    graph.add_edge(10, 3, 75)
    # mc = 20
    return graph


class TestDiGraph(unittest.TestCase):

    def test_basic_graph(self):
        """
        This test contains the basic methods implemented in DiGraph
        @:param: mc -> measured by the method "get_mc"
        :return: True if it works
        """
        print("first test")
        graph = DiGraph()
        mc = graph.get_mc()
        self.assertEqual(mc, 0, "No move was made in the Graph")
        print("Completed")

    def test_edge_size(self):
        """
        This test contains the basic methods implemented in DiGraph
        @:param: edges -> measured by the method "e_size"
        :return: True if it works
        """
        print("edges test")
        graph = DiGraph()
        eSize = graph.e_size()
        self.assertEqual(eSize, 0, "The graph is Edges free")
        print("Completed")

    def test_node_size(self):
        """
        This test contains the basic methods implemented in DiGraph
        @:param: nodes -> measured by the method "v_size"
        :return: True if it works
        """
        print("nodes test")
        graph = DiGraph()
        nSize = graph.v_size()
        self.assertEqual(nSize, 0, "The graph is nodes free")
        print("Completed")

    def test_add_remove(self):
        """
        This test contains the basic methods implemented in DiGraph
        @:param: mc -> measured by the method "get_mc"
        @:param: nodes -> measured by the method "v_size"
        @:param: edges -> measured by the method "e_size"
        :return: True if it  works
        """
        print("test add remove")
        graph = DiGraph()
        graph.add_node(1)
        self.assertEqual(graph.v_size(), 1, "You have added a node to your Graph")
        self.assertEqual(graph.get_mc(), 1, "You have added a node to your Graph")
        self.assertEqual(graph.e_size(), 0, "The graph is Edges free")
        graph.add_node(2)
        self.assertEqual(graph.v_size(), 2, "You have added a node to your Graph")

        graph.add_edge(1, 2, 2.0)
        self.assertEqual(graph.get_mc(), 3, "You have a 2 node Graph")
        self.assertEqual(graph.e_size(), 1, "The graph has 1 Edge")
        graph.remove_node(2)
        self.assertFalse(2 in graph.get_all_v())
        print("Completed")

    def test_remove_edge(self):
        """
        this method checks if an edge is removed correctly
        :return: True if it  works
        """
        print("fifth test")
        graph = create_graph()  # mc = 20
        graph.remove_edge(2, 4)  # mc = 21
        self.assertEqual(graph.e_size(), 9)
        graph.remove_node(10)  # mc = 22
        self.assertEqual(graph.e_size(), 7)
        self.assertEqual(graph.v_size(), 9)
        self.assertEqual(graph.get_mc(), 22)
        print("Completed")

    def test_add_edge(self):
        """
        this method checks if an edge is added correctly
        :return: True if it  works
        """
        print("sixth test")
        graph = create_graph()
        graph.add_edge(1, 8, 6)
        flag = False
        for i in graph.all_out_edges_of_node(1):
            if i == 8:
                flag = True
        self.assertTrue(flag)
        print("Completed")

    def test_is_equals(self):
        """
        this method checks if two graphs are equals
        :return: True if it  works
        """
        print("isEquals test")
        graph = create_graph()
        g2 = create_graph()
        self.assertTrue(graph.__eq__(g2), "doesn't equals")
        print("Completed")


if __name__ == 'main':
    unittest.main()
