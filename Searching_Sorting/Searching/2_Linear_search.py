"""
Linear Search (Sequential Search)

Overview:
    - Checks each element sequentially until the target is found or the end is reached.
    - No requirement for sorting; works on both sorted and unsorted data.

Time Complexity:
    - Best: O(1)
    - Average: O(n/2)
    - Worst: O(n)

Space Complexity: O(1)

Applications:
    - Small datasets
    - Unsorted collections (e.g., linked lists)
    - Simple validations, lookups
    - Preliminary checks
"""

def linear_search(arr, target):
    """
    Performs linear search on the array.

    :param arr: List to search in
    :param target: Element to find
    :return: Index of the target if found, else -1
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        self.data = [2, 5, 6, 9, 11, 15, 8, 4, 10, 3, 1, 77, 88, 34, 76, 21, 78, 90, 67, 44, 5, 67]

    def test_found_first(self):
        self.assertEqual(linear_search(self.data, 2), 0)

    def test_found_duplicate(self):
        self.assertEqual(linear_search(self.data, 5), 1)  # First occurrence

    def test_not_found(self):
        self.assertEqual(linear_search(self.data, 888), -1)

    def test_edge_cases(self):
        self.assertEqual(linear_search([], 5), -1)
        self.assertEqual(linear_search([10], 10), 0)
        self.assertEqual(linear_search([10], 5), -1)


if __name__ == "__main__":
    unittest.main()
