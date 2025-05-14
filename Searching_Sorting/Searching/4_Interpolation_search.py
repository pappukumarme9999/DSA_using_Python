"""
Interpolation Search Algorithm

Overview:
    - Works on sorted, uniformly distributed arrays
    - Improves over Binary Search by estimating the position of the search key

Time Complexity:
    - Best: O(1)
    - Average: O(log log n)
    - Worst: O(n)

Space Complexity: O(1)

Applications:
    - Searching in large uniformly distributed datasets
    - Index search in sparse databases
"""

def interpolation_search(arr, target):
    """
    Perform interpolation search on a sorted and uniformly distributed array.

    :param arr: Sorted list of numbers
    :param target: Value to find
    :return: Index of the target if found, otherwise -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Prevent division by zero if values are the same
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Estimate the probable position
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])

        if pos < 0 or pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestInterpolationSearch(unittest.TestCase):
    def setUp(self):
        # Uniform distribution ideal for interpolation search
        self.data = list(range(0, 1001, 5))  # [0, 5, 10, ..., 1000]

    def test_found_values(self):
        self.assertEqual(interpolation_search(self.data, 0), 0)
        self.assertEqual(interpolation_search(self.data, 250), 50)
        self.assertEqual(interpolation_search(self.data, 1000), 200)

    def test_not_found_values(self):
        self.assertEqual(interpolation_search(self.data, 3), -1)
        self.assertEqual(interpolation_search(self.data, 1001), -1)

    def test_edge_cases(self):
        self.assertEqual(interpolation_search([], 10), -1)
        self.assertEqual(interpolation_search([7], 7), 0)
        self.assertEqual(interpolation_search([7], 10), -1)
        self.assertEqual(interpolation_search([1, 1, 1, 1], 1), 0)
        self.assertEqual(interpolation_search([1, 1, 1, 1], 2), -1)

if __name__ == "__main__":
    unittest.main()
