"""
Binary Search Algorithm

Overview:
    - Efficient search in a sorted array
    - Time Complexity: O(log n)
    - Space Complexity:
        - Iterative: O(1)
        - Recursive: O(log n) due to call stack
    - Requirement: Sorted array

Applications:
    - Dictionary lookups, database indexing
    - Numerical approximations
    - Finding boundaries, search in infinite arrays
"""

def binary_search_recursive(arr, target, low=0, high=None):
    """
    Recursive binary search
    :param arr: Sorted list
    :param target: Element to search
    :param low: Starting index
    :param high: Ending index
    :return: Index of target, or -1 if not found
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


def binary_search_iterative(arr, target):
    """
    Iterative binary search
    :param arr: Sorted list
    :param target: Element to search
    :return: Index of target, or -1 if not found
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = [2, 5, 6, 9, 11, 15, 18, 56, 65, 66, 90, 99, 101]

    def test_recursive_found(self):
        self.assertEqual(binary_search_recursive(self.sorted_list, 2), 0)
        self.assertEqual(binary_search_recursive(self.sorted_list, 101), 12)
        self.assertEqual(binary_search_recursive(self.sorted_list, 66), 9)

    def test_recursive_not_found(self):
        self.assertEqual(binary_search_recursive(self.sorted_list, 200), -1)
        self.assertEqual(binary_search_recursive(self.sorted_list, -5), -1)

    def test_iterative_found(self):
        self.assertEqual(binary_search_iterative(self.sorted_list, 2), 0)
        self.assertEqual(binary_search_iterative(self.sorted_list, 101), 12)

    def test_iterative_not_found(self):
        self.assertEqual(binary_search_iterative(self.sorted_list, 999), -1)

if __name__ == "__main__":
    unittest.main()
