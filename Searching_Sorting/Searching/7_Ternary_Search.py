"""
Ternary Search Algorithm

Overview:
    - Used to find the position of a target element in a sorted array
    - Divides the array into three parts instead of two (as in binary search)

Time Complexity:
    - Best: O(1)
    - Average/Worst: O(log₃ n)

Space Complexity: O(1) - Iterative
                 O(log₃ n) - Recursive (due to stack)

Applications:
    - Search in unimodal functions (functions which increase then decrease or vice versa)
    - Sorted arrays where more balanced partitions can help reduce comparisons
"""

def ternary_search(arr, target):
    """
    Perform ternary search on a sorted list iteratively.

    :param arr: Sorted list of elements
    :param target: Value to find
    :return: Index of the target if found, else -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestTernarySearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = list(range(0, 1001, 2))  # Even numbers 0 to 1000

    def test_found_values(self):
        self.assertEqual(ternary_search(self.sorted_list, 0), 0)
        self.assertEqual(ternary_search(self.sorted_list, 1000), 500)
        self.assertEqual(ternary_search(self.sorted_list, 200), 100)

    def test_not_found_values(self):
        self.assertEqual(ternary_search(self.sorted_list, 3), -1)
        self.assertEqual(ternary_search(self.sorted_list, -5), -1)
        self.assertEqual(ternary_search(self.sorted_list, 1001), -1)

    def test_edge_cases(self):
        self.assertEqual(ternary_search([], 10), -1)
        self.assertEqual(ternary_search([7], 7), 0)
        self.assertEqual(ternary_search([7], 3), -1)
        self.assertEqual(ternary_search([1, 2, 3, 4], 4), 3)

if __name__ == "__main__":
    unittest.main()
