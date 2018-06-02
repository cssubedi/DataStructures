#!/usr/bin/python
import sys
sys.path.append("../include/")
from copy import deepcopy
from directed_graph_data_structures import *
from depth_first_search import DFS


class DGraph(object):
    def __init__(self):
        """
        Implements directed graph data structure using Adjacency lists.

        """
        self.graph = LinkedList()

    @property
    def acyclic(self):
        queue = Queue()
        for node in self.graph:
            if node.data.in_degree == 0:
                queue.enqueue(node.data.element)

        return deepcopy(self).is_acyclic(queue)

    def add_vertex(self, vertex):
        vertex_object = Vertex(vertex)
        vertex_node = Node(vertex_object)

        self.graph.add(vertex_node)

    def remove_vertex(self, vertex):
        vertex_node = self.graph.get_node(vertex)

        for node in vertex_node.data.parents:
            node.data.children.remove(vertex)

        for node in vertex_node.data.children:
            node.data.parents.remove(vertex)

        self.graph.remove(vertex)

    def add_edge(self, source, destination):
        source_node = self.graph.get_node(source)
        destination_node = self.graph.get_node(destination)

        if source_node and destination_node:
            source_node.data.children.add(Node(destination_node.data))
            destination_node.data.parents.add(Node(source_node.data))
        else:
            if not source_node:
                raise ValueError("Source vertex {} does not exist in graph.".format(source))
            if not destination_node:
                raise ValueError("Destination vertex {} does not exist in graph.".format(destination))

    def remove_edge(self, source, destination):
        source_node = self.graph.get_node(source)
        destination_node = self.graph.get_node(destination)

        source_node.data.children.remove(destination)
        destination_node.data.parents.remove(source)

    def is_acyclic(self, queue):
        """
        Implements a linear time algorithm to check if the graph is acyclic.
        Algorithm:
            Find a source                               --> O(V)
            Delete it from the graph and update queue   --> O(V)
            Repeat until the graph is empty             --> O(V)
            If the graph is empty, then it is acyclic

        A queue is maintained containing node with 0 in-degree to find source
        in linear time. is_acyclic() is recursively run on remaining graph.

        """
        if len(self.graph) == 0:
            return True

        elif not queue.is_empty():
            source = queue.dequeue()
            source_node = self.graph.get_node(source)
            for node in source_node.data.children:
                if (node.data.in_degree - 1) == 0:
                    queue.enqueue(node.data.element)
            self.remove_vertex(source)
            result = self.is_acyclic(queue)
        else:
            result = False

        return result

    def reverse_graph(self):
        """
        Implements a linear time algorithm to generate reverse/tranpose of the graph.
        Algorithm:
            Switch children and parents linked list of each vertex. --> O(V)

        """
        rgraph = DGraph()
        rgraph.graph = deepcopy(self.graph)

        for node in rgraph.graph:
            node.data.children, node.data.parents = node.data.parents, node.data.children

        return rgraph

    def linearize(self):
        """
        Implements a linear time algorithm to linearize a dag.
        Algorithm:
            Arrange elements in decreasing order of their post numbers. --> O(V+E)

        Post number is the time equivalent when a node is
        completely explored. Post number is generated during dfs.
        Output list is updated as nodes get completely explored.

        """
        if self.acyclic:
            dfs = DFS(self.graph, generate_linearized_graph=True)
            dfs.search()
            return dfs.linearized_graph
        else:
            return "The graph is cyclic and cannot be linearized."

    def strongly_connected_components(self):
        """
        Implements a linear time Kosaraju's algorithm to find strongly connected
        components. It runs two depth first search.
        Algorithm:
            Generate reverse/transpose of a graph                   --> O(V)
            Run dfs on reverse graph                                --> O(V+E)
            Run dfs on graph by processing vertices in decreasing   --> O(V+E)
            order of post numbers (obtained from previous dfs)

        In order to process vertices in decreasing order of post numbers
        and in linear time, a stack is maintained. First dfs populates the stack.

        """
        for node in self.graph:
            node.data.visited = False

        reverse_graph = self.reverse_graph()
        dfs_reverse_graph = DFS(reverse_graph.graph, generate_stack=True)
        dfs_reverse_graph.search()

        dfs_graph = DFS(self.graph, generate_scc=True)

        while dfs_reverse_graph.stack:
            node = self.graph.get_node(dfs_reverse_graph.stack.top_pop())
            if not node.data.visited:
                dfs_graph.strongly_connected_components.append([])
                dfs_graph.num_scc += 1
                dfs_graph.explore(node)
        return dfs_graph.num_scc, dfs_graph.strongly_connected_components

    def size(self):
        num_vertices = len(self.graph)
        count = 0

        for node in self.graph:
            if node is not None:
                count += len(node.data.edges)

        num_edges = count/2
        return num_vertices, num_edges

    def __str__(self):
        result = ""
        for source_node in self.graph:
            if source_node is not None:
                result += source_node.data.element
                for destination_node in source_node.data.children:
                    if destination_node is not None:
                        result += ("---->" + destination_node.data.element)
            if source_node.next is not None:
                result += ("\n" + "|" + "\n" + "|" + "\n")
            else:
                result += "\n"

        return result
