import random
from typing import List
from src import GraphInterface
from DiGraph import DiGraph
import json
import heapq
import matplotlib.pyplot as plt


class GraphAlgo:

    def __init__(self, g=None):
        if g:
            self.graph = g
        else:
            self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        new_graph = DiGraph()

        try:

            with open(file_name, 'r') as file:
                data = json.load(file)

                for n in data['Nodes']:

                    try:

                        pos = n['pos'].split(",")
                        x, y, z = float(pos[0]), float(pos[1]), float(pos[2])
                        new_graph.add_node(n['id'], (x, y, z))
                    except:
                        new_graph.add_node(n['id'])

                for e in data['Edges']:
                    new_graph.add_edge(e['src'], e['dest'], e['w'])

                self.graph = new_graph

                return True

        except OSError as e:
            print("OSError {}".format(e))

        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        nodes = self.graph.get_all_v()

        data = {'Edges': [], 'Nodes': []}

        for n in nodes:
            node = nodes[n]
            if node.pos:
                data['Nodes'].append({
                    'id': node.key,
                    'pos': node.pos
                })
            else:
                data['Nodes'].append({
                    'id': node.key
                })

            for o in node.out_edges:
                data['Edges'].append({
                    'src': node.key,
                    'dest': o,
                    'w': node.out_edges[o].weight
                })
        try:
            with open(file_name, 'w') as file:
                json.dump(data, file)
                return True

        except OSError as e:
            print("OSError {}".format(e))
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Example:
#        >>> from GraphAlgo import GraphAlgo
#        >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        nodes = self.graph.get_all_v()

        if id1 in nodes and id2 in nodes:

            parent = {i: None for i in nodes}
            distance = {i: float('inf') for i in nodes}

            distance[id1] = 0
            visit = set()

            # this is a priority queue = (priority, node_id)
            priority_q = [(distance[id1], id1)]

            while priority_q:

                current_distance, index = heapq.heappop(priority_q)

                if index in visit:
                    continue

                visit.add(index)

                for ni in self.graph.all_out_edges_of_node(index):
                    if ni in visit:
                        continue

                    dist = current_distance + self.graph.all_out_edges_of_node(index)[ni].weight

                    if dist < distance[ni]:
                        distance[ni] = dist
                        parent[ni] = index

                        heapq.heappush(priority_q, (dist, ni))

            runner = id2
            path = [runner]

            while runner:

                path.append(parent[runner])
                runner = parent[runner]

                if runner == id1:
                    break

                if runner is None:
                    return distance[id2], []

            # path[::-1] to reverse path
            return distance[id2], path[::-1]

        return float('inf'), []

    def transpose(self):
        """
        transpose a graph
        :return: a transposed graph
        """

        transposed = DiGraph()
        nodes = self.graph.get_all_v()

        for node in nodes:
            transposed.add_node(node)

        for node in nodes:
            for ni in nodes[node].out_edges:
                transposed.add_edge(ni, node, nodes[node].out_edges[ni].weight)

        return transposed

    def BFS_util(self, node, nodes, stack):
        q = [node]
        nodes[node].tag = True

        while q:
            index = q.pop()

            for i in self.graph.all_out_edges_of_node(index):
                if not nodes[i].tag:
                    nodes[i].tag = True
                    q.append(i)
            stack.append(index)

    def BFS(self, node, graph, final):
        """
        this method implement breath-first search
        :param node: the node
        :param graph: the graph we want to implement on
        :param final: this is the list that we will need in the end
        :return: finds the gcc of the graph using transpose graph and BFS twice
        """
        q = [node]
        final.append(node)
        graph.graph_nodes[node].tag = True

        while q:
            index = heapq.heappop(q)

            for i in graph.all_out_edges_of_node(index):

                if not graph.graph_nodes[i].tag:
                    graph.graph_nodes[i].tag = True
                    q.append(i)
                    final.append(i)

        return final

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        nodes = self.graph.get_all_v()

        for node in nodes:
            nodes[node].tag = False

        stack = []
        self.BFS_util(id1, nodes, stack)
        transpose_graph = self.transpose()
        sConnected_path = []
        self.BFS(id1, transpose_graph, sConnected_path)

        return list(set(stack).intersection(sConnected_path))

    def connected_components(self) -> List[list]:
        """
        BFS(src)
        transpose_graph
        BFS(src -> transpose)

        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        nodes = self.graph.get_all_v()
        for node in nodes:
            nodes[node].tag = False

        result = []
        for node in nodes:
            flag = False
            for i in result:
                if node in i:
                    flag = True

            if flag:
                continue

            for x in nodes:
                nodes[x].tag = False

            stack = []
            self.BFS_util(node, nodes, stack)

            transpose_graph = self.transpose()
            sConnected_path = []
            nodes = transpose_graph.get_all_v()

            self.BFS(node, transpose_graph, sConnected_path)

            result.append(list(set(stack).intersection(sConnected_path)))

        return result

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        nodes = self.graph.get_all_v()
        for n in nodes:
            if nodes[n].pos is None:
                v_size = self.graph.v_size()
                x, y, z = random.uniform(0, v_size), random.uniform(0, v_size), 0
                nodes[n].pos = (x, y, z)
        X = []
        Y = []
        Z = []

        ax = plt.axes()

        for n in nodes:
            node = nodes[n]
            x, y, z = node.pos

            for out in node.out_edges:

                dest_node = self.graph.graph_nodes[out]

                dest_x, dest_y, dest_z = dest_node.pos

                ax.quiver(x, y, dest_x - x, dest_y - y, angles='xy', scale_units="xy", scale=1)

            X.append(x)
            Y.append(y)
            Z.append(z)

        plt.plot(X, Y, 'ro')
        plt.show()

    """
    isEquals for graphs
    """
    def __eq__(self, other=None):
        if other is not None:
            return self.get_graph() == other.get_graph()

        return False
