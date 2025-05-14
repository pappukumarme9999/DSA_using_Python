"""
Exponential Search Algorithm

Overview:
    - Efficient for unbounded or large sorted arrays
    - Combines exponential range expansion with binary search

Time Complexity:
    - Best: O(1)
    - Average/Worst: O(log i), where i is the position of the target

Space Complexity: O(1)

Applications:
    - Searching in large sorted arrays
    - Useful when the size of the array is unknown (e.g., infinite arrays, file streams)
"""

def binary_search(arr, left, right, target):
    """
    Standard binary search within given bounds.

    :param arr: Sorted list
    :param left: Left index of subarray
    :param right: Right index of subarray
    :param target: Value to search for
    :return: Index if found, else -1
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def exponential_search(arr, target):
    """
    Perform exponential search on a sorted list.

    :param arr: Sorted list of elements
    :param target: Value to find
    :return: Index of the target if found, else -1
    """
    n = len(arr)
    if n == 0:
        return -1

    if arr[0] == target:
        return 0

    index = 1
    while index < n and arr[index] <= target:
        index *= 2

    # Apply binary search within the found bounds
    return binary_search(arr, index // 2, min(index, n - 1), target)


# ------------------------------- TESTING -------------------------------
import unittest

class TestExponentialSearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = list(range(0, 10000, 7))  # Uniform gap

    def test_found_values(self):
        self.assertEqual(exponential_search(self.sorted_list, 0), 0)
        self.assertEqual(exponential_search(self.sorted_list, 350), 50)
        self.assertEqual(exponential_search(self.sorted_list, 9993), len(self.sorted_list) - 1)

    def test_not_found_values(self):
        self.assertEqual(exponential_search(self.sorted_list, -1), -1)
        self.assertEqual(exponential_search(self.sorted_list, 3), -1)
        self.assertEqual(exponential_search(self.sorted_list, 10001), -1)

    def test_edge_cases(self):
        self.assertEqual(exponential_search([], 1), -1)
        self.assertEqual(exponential_search([42], 42), 0)
        self.assertEqual(exponential_search([42], 5), -1)

if __name__ == "__main__":
    unittest.main()
