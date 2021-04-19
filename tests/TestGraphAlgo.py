import unittest
from src import DiGraph
from src import NodeData
from NodeData import NodeData
from NodeData import EdgeData
from src import GraphAlgo
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class TestGraphAlgo(unittest.TestCase):
    def setUp(self) -> None:
        self.algo = GraphAlgo

    def test_get_graph(self):
        """
        Tests if the method "get_graph" is in order
        :return: True if so
        """
        print("first test")
        algo = GraphAlgo()
        self.assertTrue(algo.get_graph())
        print("Completed")

    def test_load_save_json(self):
        """
        Tests load_from_json works correctly
        :return: True if so
        """
        print("second test")
        algo = GraphAlgo()
        file = "../data/T0.json"
        # print the graph to the screen
        algo.load_from_json(file)
        algo.plot_graph()
        algo.save_to_json("../data/T0_saved.json")
        g_algo = GraphAlgo()
        file = "../data/T0_saved.json"
        g_algo.load_from_json(file)

        # print the graph to the screen
        g_algo.plot_graph()
        self.assertFalse(algo.__eq__(g_algo))
        print("Completed")

    def testa_shortest_path(self):
        """
        This method tests the shortest path between 2 nodes
        :return: True if the graphs are the same
        """
        print("third test")
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 0.0)
        algo = GraphAlgo(graph)
        algo.save_to_json("../tests/third_algo_test.json")
        s_path_algo = algo.shortest_path(0, 1)

        g_algo = GraphAlgo()
        file = '../tests/third_algo_test.json'
        g_algo.load_from_json(file)

        s_path_g_algo = g_algo.shortest_path(0, 1)
        self.assertEqual(s_path_algo, s_path_g_algo)
        print("Completed")

    def testb_shortest_path(self):
        """
        This method tests the shortest path between 2 nodes in a liniar graph
        :return: True if the paths are the same
        """
        print("fourth test")
        algo = GraphAlgo(self.liniar_graph())
        algo.save_to_json("../tests/third_algo_test.json")
        s_path_algo = algo.shortest_path(0, 9)

        g_algo = GraphAlgo()
        file = '../tests/third_algo_test.json'
        g_algo.load_from_json(file)
        s_path_g_algo = g_algo.shortest_path(0, 9)
        self.assertEqual(s_path_algo, s_path_g_algo)
        print("Completed")

    def testc_shortest_path(self):
        """
        This method tests the shortest path on one node graph
        :return: True if the paths are the same
        """
        print("fifth test")
        algo = GraphAlgo(self.single_node_graph())
        ans = algo.shortest_path(1,1)

        self.assertEqual((float('inf'), []), ans)
        print("Completed")

    def testa_transpose(self):
        """
        This method checks if the method 'transpose', that we chose to
        implement is working the way we wished for
        :return: True if it does
        """
        print("sixth test")
        algo = GraphAlgo(self.single_node_graph())
        trans = algo.transpose()
        self.assertEqual(trans, algo.get_graph())
        print("Completed")

    def test_connected_component(self):
        """
        This test checks if there is a connected to a specific node
        :return: True if it does
        """
        print("seventh test")
        algo = GraphAlgo(self.single_node_graph())
        ans = algo.connected_component(100)
        self.assertEqual([100], ans)
        print("Completed")

    def test_ccg_graph(self):
        """
        This test checks if the graph is strongly connected
        :return: True if it does
        """
        print("eighth test")
        graph = DiGraph()
        graph.add_node(100)
        algo = GraphAlgo()
        algo.graph = graph
        ans = algo.connected_components()
        self.assertEqual([[100]], ans)

        g_algo = GraphAlgo(self.connected_graph())
        res = g_algo.connected_components()
        exp = []
        for i in g_algo.get_graph().graph_nodes:
            exp.append(i)

        self.assertEqual([exp], res)

        print("Completed")

    def single_node_graph(self) -> DiGraph:
        """
        This method creates a new graph with only one node
        :return: DiGraph
        """
        graph = DiGraph()
        graph.add_node(100)
        return graph

    def liniar_graph(self) -> DiGraph:
        """
        This method create a linear 10 node graph
        :return: DiGraph
        """
        graph = DiGraph()
        for i in range(0, 10):
            graph.add_node(i)
        for i in range(0, 10):
            graph.add_edge(i, i + 1, 1.0)
        return graph

    def connected_graph(self) -> DiGraph:
        """
        This method create a linear 10 node graph
        :return: DiGraph
        """
        graph = DiGraph()
        for i in range(0, 10):
            graph.add_node(i)
        for i in range(0, 10):
            for j in range(0,10):
                if i is not j:
                    graph.add_edge(i, j, 1.0)
        return graph

if __name__ == 'main':
    unittest.main()
