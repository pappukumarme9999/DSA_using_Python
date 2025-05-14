"""
Jump Search Algorithm

Overview:
    - Designed for sorted arrays
    - Divides the array into blocks and performs a block-wise jump
    - After identifying the block, it performs linear search within that block

Time Complexity:
    - Best: O(1)
    - Average/Worst: O(√n)

Space Complexity: O(1)

Applications:
    - Sorted arrays with random access (like arrays or lists)
    - Efficient alternative to linear search for large sorted data

Requirements:
    - Array must be sorted
"""

import math

def jump_search(arr, target):
    """
    Perform jump search on a sorted array.

    :param arr: Sorted list of elements
    :param target: Value to search
    :return: Index of target if found, else -1
    """
    n = len(arr)
    if n == 0:
        return -1

    step = int(math.sqrt(n))
    prev = 0

    # Finding the block where the element may be present
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    while prev < min(step, n) and arr[prev] < target:
        prev += 1

    if prev < n and arr[prev] == target:
        return prev

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestJumpSearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = list(range(0, 100, 5))  # [0, 5, 10, ..., 95]

    def test_found(self):
        self.assertEqual(jump_search(self.sorted_list, 0), 0)
        self.assertEqual(jump_search(self.sorted_list, 25), 5)
        self.assertEqual(jump_search(self.sorted_list, 95), 19)

    def test_not_found(self):
        self.assertEqual(jump_search(self.sorted_list, 3), -1)
        self.assertEqual(jump_search(self.sorted_list, 97), -1)

    def test_edge_cases(self):
        self.assertEqual(jump_search([], 5), -1)
        self.assertEqual(jump_search([10], 10), 0)
        self.assertEqual(jump_search([10], 5), -1)


if __name__ == "__main__":
    unittest.main()
