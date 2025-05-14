from typing import Dict, List, Set


class Graph:
    """
    A class to represent an unweighted graph using an adjacency list.

    Attributes:
        is_directed (bool): Whether the graph is directed or not.
        adj_list (Dict[str, List[str]]): Stores the graph's adjacency list.
    """

    def __init__(self, is_directed: bool = False):
        """
        Initializes the graph.

        Args:
            is_directed (bool): Set to True for a directed graph. Defaults to False.
        """
        self.is_directed = is_directed
        self.adj_list: Dict[str, List[str]] = {}

    def add_edge(self, u: str, v: str):
        """
        Adds an edge between nodes u and v.

        Args:
            u (str): The source node.
            v (str): The destination node.
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

        if not self.is_directed:
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.adj_list[v].append(u)

    def dfs(self, start_node: str) -> List[str]:
        """
        Performs Depth-First Search (DFS) traversal from the given start node.

        Args:
            start_node (str): The starting node for DFS.

        Returns:
            List[str]: A list representing the DFS traversal order.
        """
        visited: Set[str] = set()
        dfs_order: List[str] = []

        def dfs_recursive(node: str):
            if node not in visited:
                visited.add(node)
                dfs_order.append(node)
                for neighbor in self.adj_list.get(node, []):
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return dfs_order

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())



import unittest
# from depth_first_search import Graph

class TestDepthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")
        self.graph.add_edge("C", "E")
        self.graph.add_edge("D", "F")
        self.graph.add_edge("E", "F")

    def test_dfs_from_A(self):
        expected_order = ["A", "B", "D", "F", "C", "E"]
        self.assertEqual(self.graph.dfs("A"), expected_order)

    def test_dfs_from_C(self):
        expected_order = ["C", "E", "F", "D", "B", "A"]
        self.assertEqual(self.graph.dfs("C"), expected_order)

    def test_dfs_disconnected_component(self):
        self.graph.add_edge("X", "Y")
        self.assertEqual(self.graph.dfs("X"), ["X", "Y"])

    def test_dfs_on_nonexistent_node(self):
        self.assertEqual(self.graph.dfs("Z"), ["Z"])


if __name__ == '__main__':
    unittest.main()
