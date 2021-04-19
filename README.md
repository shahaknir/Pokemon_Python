# Pokemon_Python
Pokemon Project, by Reut Hadad, Shahak Nir

<img src="/Pictures/OOP_EX3 Python.jpeg" height="70" width="350" >

This project represents a weighted and directed graph

This project based on Classes that we created such as:

NodeData - represents vertices on the graph.
EdgeData - represents graph's edges.
DiGraph - represents our graph that contains all the Vertex and Edges.
GraphAlgo- represents our graph which we operate our algorithms on.
Comp - represents a comperession against NetworkX.

Each class offers us multiple functions to get information about the object.
we have several algorithms that we can operate on our graph such as:

shortest_path(self, id1: int, id2: int) -> (float, list) - return the *shortest* path from Vertex 1 to Vertex 2,
by using Dijkstra's Algorithm.
connected_components(self) -> List[list] - Finds all the Strongly Connected Component(SCC) in the graph,
using BFS Algorithm and transpose.
connected_component(self, id1: int) -> list - return a list with the Strongly Connected Component(SCC) that node id1 is a part of,
using BFS Algorithm.

we made tests for each class and the graph we created for checking the methods is:

<img src="/Pictures/create_graph.jpeg" height="250" width="350" >
 
 
 😎 Enjoy!
