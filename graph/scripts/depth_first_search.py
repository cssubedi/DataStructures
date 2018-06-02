import sys
sys.path.append("../../")
from stack.stack import Stack


def parameters():
    """
    The decorator for the class DFS, selects previsit() and postvisit() function
    based on the input arguments.
    Example:
    param = dict(generate_linearized_graph=True,
                generate_stack=False,
                generate_scc=False)
    dfs = DFS(graph, **param)       (dfs becomes instance of WrappedClass)

    For such case, the decorator selects appropriate postvisit() function
    to generate the linearized graph of the input graph and returns the
    instance.

    Returns:
        WrappedClass: An instance of the WrappedClass is returned.
    """
    def wrapper(wrapped):
        class WrappedClass(wrapped):
            def __init__(self, *args, **kwargs):
                super(WrappedClass, self).__init__(*args, **kwargs)
                self.book_keeping(kwargs)

            def update_interval(self, node):
                node.data.interval.append(self.clock)
                self.clock += 1

            def update_stack(self, node):
                self.update_interval(node)
                self.stack.push(node.data.element)

            def update_linearized_graph(self, node):
                self.update_interval(node)
                self.linearized_graph.insert(0, node.data.element)

            def update_scc(self, node):
                self.update_interval(node)
                self.strongly_connected_components[self.num_scc - 1]\
                    .append(node.data.element)

            def search_scc(self):
                for node in self.graph:
                    node.data.visited = False

                for node in self.graph:
                    if not node.data.visited:
                        self.strongly_connected_components.append([])
                        self.num_scc += 1
                        self.explore(node)

            def book_keeping(self, param):
                for key, val in param.items():
                    if (key == "generate_stack") and val:
                        self.stack = Stack()
                        self.previsit = self.update_interval
                        self.postvisit = self.update_stack

                    elif (key == "generate_linearized_graph") and val:
                        self.linearized_graph = []
                        self.previsit = self.update_interval
                        self.postvisit = self.update_linearized_graph

                    elif (key == "generate_scc") and val:
                        self.strongly_connected_components = []
                        self.num_scc = 0
                        self.previsit = self.update_scc
                        self.postvisit = self.update_interval
                        self.search = self.search_scc
                    else:
                        self.previsit = self.update_interval
                        self.postvisit = self.update_interval

        return WrappedClass
    return wrapper


@parameters()
class DFS(object):
    def __init__(self, graph, **param):
        self.graph = graph
        self.clock = 1

    def explore(self, node):
        node.data.visited = True
        self.previsit(node)

        for edge_node in node.data.edges:
            if not edge_node.data.visited:
                self.explore(edge_node)

        self.postvisit(node)

    def search(self):
        for node in self.graph:
            node.data.visited = False

        for node in self.graph:
            if not node.data.visited:
                self.explore(node)



