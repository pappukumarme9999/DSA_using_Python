"""
Sentinel Search

Overview:
    - Linear search optimization that eliminates explicit bounds checking in each iteration
    - Temporarily adds the target element to the end of the list (as a sentinel)
    - Ensures that the loop terminates naturally without checking array bounds

Time Complexity: O(n)
    - Best: O(1) — if element is at the beginning
    - Worst: O(n) — if element is not in the list

Space Complexity: O(1)

Advantages:
    - Slightly faster than regular linear search due to reduced comparisons

Use Cases:
    - Small or unsorted datasets where search operations are frequent
"""

def sentinel_search(arr, target):
    """
    Perform sentinel search in an array.
    
    :param arr: List of elements to search in
    :param target: Element to find
    :return: Index of target if found, else -1
    """
    n = len(arr)
    if n == 0:
        return -1

    last = arr[-1]
    arr[-1] = target  # Place the sentinel

    index = 0
    while arr[index] != target:
        index += 1

    arr[-1] = last  # Restore original last element

    if index < n - 1 or arr[-1] == target:
        return index

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestSentinelSearch(unittest.TestCase):
    def setUp(self):
        self.arr = [7, 3, 9, 2, 5, 1, 8]

    def test_found(self):
        self.assertEqual(sentinel_search(self.arr[:], 7), 0)
        self.assertEqual(sentinel_search(self.arr[:], 5), 4)
        self.assertEqual(sentinel_search(self.arr[:], 8), 6)

    def test_not_found(self):
        self.assertEqual(sentinel_search(self.arr[:], 10), -1)
        self.assertEqual(sentinel_search(self.arr[:], -1), -1)

    def test_edge_cases(self):
        self.assertEqual(sentinel_search([], 5), -1)
        self.assertEqual(sentinel_search([5], 5), 0)
        self.assertEqual(sentinel_search([5], 3), -1)
        self.assertEqual(sentinel_search([1, 1, 1, 1, 1], 1), 0)

if __name__ == "__main__":
    unittest.main()
