from collections import deque
from typing import Dict, List, Set


class Graph:
    """
    A class to represent an unweighted graph using an adjacency list.

    Attributes:
        is_directed (bool): Whether the graph is directed or not.
        adj_list (Dict[Any, List[Any]]): Stores the graph's adjacency list.
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

    def bfs(self, start_node: str) -> List[str]:
        """
        Performs Breadth-First Search (BFS) traversal from the given start node.

        Args:
            start_node (str): The starting node for BFS.

        Returns:
            List[str]: A list representing the BFS traversal order.
        """
        visited: Set[str] = set()
        queue = deque([start_node])
        bfs_order: List[str] = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_order.append(node)
                queue.extend(neighbor for neighbor in self.adj_list.get(node, []) if neighbor not in visited)

        return bfs_order

    def __str__(self):
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())



import unittest
# from breadth_first_search import Graph

class TestBreadthFirstSearch(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_edge("B", "D")
        self.graph.add_edge("C", "E")
        self.graph.add_edge("D", "F")
        self.graph.add_edge("E", "F")

    def test_bfs_from_A(self):
        expected_order = ["A", "B", "C", "D", "E", "F"]
        self.assertEqual(self.graph.bfs("A"), expected_order)

    def test_bfs_from_D(self):
        expected_order = ["D", "B", "F", "A", "E", "C"]
        self.assertEqual(self.graph.bfs("D"), expected_order)

    def test_bfs_disconnected_graph(self):
        self.graph.add_edge("X", "Y")
        # From isolated node
        self.assertEqual(self.graph.bfs("X"), ["X", "Y"])
        self.assertEqual(self.graph.bfs("Y"), ["Y", "X"])

    def test_bfs_on_nonexistent_node(self):
        self.assertEqual(self.graph.bfs("Z"), ["Z"])


if __name__ == '__main__':
    unittest.main()
