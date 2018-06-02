#!/usr/bin/python

import sys
sys.path.append("../include/")
from undirected_graph_data_structures import Node, Vertex, LinkedList
from depth_first_search import DFS


class UGraph(object):
    def __init__(self):
        self.graph = LinkedList()

    def add_vertex(self, vertex):
        vertex_object = Vertex(vertex)
        vertex_node = Node(vertex_object)

        self.graph.add(vertex_node)

    def remove_vertex(self, vertex):
        vertex_node = self.graph.get_node(vertex)

        for node in vertex_node.data.edges:
            node.data.edges.remove(vertex)

        self.graph.remove(vertex)

    def add_edge(self, source, destination):
        source_node = self.graph.get_node(source)
        destination_node = self.graph.get_node(destination)

        if source_node and destination_node:
            source_node.data.edges.add(Node(destination_node.data))
            destination_node.data.edges.add(Node(source_node.data))
        else:
            if not source_node:
                print("Source vertex {} does not exist in graph.".format(source))
            if not destination_node:
                print("Destination vertex {} does not exist in graph.".format(destination))

    def remove_edge(self, source, destination):
        source_node = self.graph.get_node(source)
        destination_node = self.graph.get_node(destination)

        source_node.data.edges.remove(destination)
        destination_node.data.edges.remove(source)

    def size(self):
        num_vertices = len(self.graph)
        count = 0

        for node in self.graph:
            if node is not None:
                count += len(node.data.edges)
        num_edges = count/2

        return num_vertices, num_edges

    def connected_components(self):
        depth_first_search = DFS(self.graph, generate_scc=True)
        depth_first_search.search()

        return depth_first_search.num_scc, \
               depth_first_search.strongly_connected_components

    def __str__(self):
        result = ""
        for source_node in self.graph:
            if source_node is not None:
                result += source_node.data.element
                for destination_node in source_node.data.edges:
                    if destination_node is not None:
                        result += ("---->" + destination_node.data.element)
            if source_node.next is not None:
                result += ("\n" + "|" + "\n" + "|" + "\n")
            else:
                result += "\n"
        return result
