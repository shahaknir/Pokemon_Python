import time
from src.GraphAlgo import GraphAlgo
import json

import networkx as nx
import matplotlib.pyplot as plt


def check0():
    """
    this method times the load method implemented in python
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    algo = GraphAlgo()
    print("time of loading to algo in Python: ")
    for file in cl.fileList:
        start = time.perf_counter()

        algo.load_from_json(file)

        end = time.perf_counter()
        total = end - start
        # print("file name: {}".format(file))
        print("file: {}, took: {}, start time: {}, end time: {}".format(file, total, start, end))
        cl.all_data['file'] = {'loading in algo': total}


def check1():
    """
    this method times the shortest path method implemented in python
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    algo = GraphAlgo()
    print("time of shortest path to algo in Python: ")

    for file in cl.fileList:
        start = time.perf_counter()

        algo.load_from_json(file)
        shortest = algo.shortest_path(0, 6)

        end = time.perf_counter()
        total = end - start
        print("shortest path: {}, took: {}, start time: {}, end time: {}".format(shortest, total, start, end))
        cl.all_data['file'] = {'shortest path in algo': total}


def check2():
    """
    this method times the connected component method implemented in python
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    algo = GraphAlgo()
    print("time of connected component to algo in Python: ")
    for file in cl.fileList:
        start = time.perf_counter()

        algo.load_from_json(file)
        connected = algo.connected_component(6)

        end = time.perf_counter()
        total = end - start
        print("connected component on 6: file name: {}, took: {}, start time: {}, end time: {}".format(file, total, start, end))
        cl.all_data['file'] = {'connected component in algo': total}


def check_connected_algo():
    """
    this method times the connected components method implemented in python
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    algo = GraphAlgo()
    print("time of connected components to algo in Python: ")
    for file in cl.fileList:
        start = time.perf_counter()

        algo.load_from_json(file)
        connected = algo.connected_components()

        end = time.perf_counter()
        total = end - start
        print(
            "connected components in Graph: file name: {}, took: {}, start time: {}, end time: {}".format(file, total, start,
                                                                                               end))
        cl.all_data['file'] = {'connected components in algo': total}


######## Networkx ########


def check3():
    """
    this method times the load method implemented in Networkx
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    print("time of load to Networkx Graph in Python: ")

    for file in cl.fileList:
        start = time.perf_counter()
        cl.read_json_file(file)
        graph = cl.nxGraph
        # cl.nxGraph will be loaded graph after previous line
        end = time.perf_counter()
        total = end - start
        print("file: {}, took: {}, start time: {}, end time: {}".format(file, total, start, end))
        cl.all_data['file'] = {'loading in NetworkX': total}


def check4():
    """
    this method times the shortest path method implemented in Networkx
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    print("time of shortest path to algo in Python: ")
    for file in cl.fileList:
        start = time.perf_counter()

        cl.read_json_file(file)
        graph = cl.nxGraph
        # cl.nxGraph will be loaded graph after previous line
        shortest = nx.single_source_dijkstra_path(graph, 0, 6)
        end = time.perf_counter()
        total = end - start
        print("shortest path file name: {}, took: {}, start time: {}, end time: {}".format(file, total, start, end))
        cl.all_data['file'] = {'shortest path in NetworkX': total}


def check5():
    """
    this method times the connected components method implemented in Networkx
    :return: time of running
    """
    cl = comp()
    cl.file_names2array()
    print("time of connected components to algo in Python: ")
    for file in cl.fileList:
        start = time.perf_counter()

        cl.read_json_file(file)
        graph = cl.nxGraph
        # cl.nxGraph will be loaded graph after previous line
        connected = nx.strongly_connected_components(graph)
        end = time.perf_counter()
        total = end - start
        print("connected components: {}, took: {}, start time: {}, end time: {}".format(connected, total, start, end))
        cl.all_data['file'].append({'6': total})


def ploting(method, values):
    cl = comp()

    plt.subplots(values)
    plt.ylabel('time of running')
    plt.show()

class comp:
    """
    this class is made in order to run comp between the implements in
    """

    def __init__(self):
        self.fileList = []
        self.nxGraph = nx.DiGraph()
        self.all_data = {}

    def file_names2array(self):
        """
        gets all the files in one list
        :return: List of file names
        """
        self.fileList = [''] * 18
        # this group is of Graphs without pos
        self.fileList[0] = '../data/G_10_80_0.json'
        self.fileList[1] = '../data/G_100_800_0.json'
        self.fileList[2] = '../data/G_1000_8000_0.json'
        self.fileList[3] = '../data/G_10000_80000_0.json'
        self.fileList[4] = '../data/G_20000_160000_0.json'
        self.fileList[5] = '../data/G_30000_240000_0.json'

        # this group is of Graphs on circle
        self.fileList[6] = '../data/G_10_80_1.json'
        self.fileList[7] = '../data/G_100_800_1.json'
        self.fileList[8] = '../data/G_1000_8000_1.json'
        self.fileList[9] = '../data/G_10000_80000_1.json'
        self.fileList[10] = '../data/G_20000_160000_1.json'
        self.fileList[11] = '../data/G_30000_240000_1.json'

        # this group is of Graphs with random pos
        self.fileList[12] = '../data/G_10_80_2.json'
        self.fileList[13] = '../data/G_100_800_2.json'
        self.fileList[14] = '../data/G_1000_8000_2.json'
        self.fileList[15] = '../data/G_10000_80000_2.json'
        self.fileList[16] = '../data/G_20000_160000_2.json'
        self.fileList[17] = '../data/G_30000_240000_2.json'

        for file in self.fileList:
            self.all_data = {'file': []}

    def read_json_file(self, file_name):
        """
        this method loads a graph using NetworkX
        :param self: comp
        :param file_name: name of the graph
        :return: the graph loaded with the json information
        """
        try:
            with open(file_name, "r") as file:
                # loaded_graph = nx.DiGraph()
                f = json.load(file)
                for node in f.get("Nodes"):
                    id = node.get("id")
                    pos = None
                    if node.get("pos") is not None:
                        list_pos = node.get("pos").split(",")
                        x, y, z = float(list_pos[0]), float(list_pos[1]), float(list_pos[2])
                        pos = (x, y, z)
                    self.nxGraph.add_node(id, pos=pos)
                for edge in f['Edges']:
                    self.nxGraph.add_edge(edge['src'], edge['dest'], wieght=edge['w'])

        except IOError as exp:
            print(exp)
            return False
        return True

if __name__ == '__main__':
    check0()
    check1()
    check2()
    check_connected_algo()
    check3()
    check4()
    check5()

