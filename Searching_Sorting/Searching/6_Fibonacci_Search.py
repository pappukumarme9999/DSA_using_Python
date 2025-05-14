"""
Fibonacci Search Algorithm

Overview:
    - A search algorithm that uses Fibonacci numbers to divide the array
    - Works on sorted arrays similar to Binary Search, but with potentially fewer comparisons

Time Complexity:
    - Best: O(1)
    - Average/Worst: O(log n)

Space Complexity: O(1)

Applications:
    - When element access cost increases with index (e.g., memory/page faults)
    - For sorted arrays where division (used in binary search) is expensive or avoided
"""

def fibonacci_search(arr, target):
    """
    Perform Fibonacci Search on a sorted array.

    :param arr: Sorted list
    :param target: Value to search
    :return: Index of the target if found, else -1
    """
    n = len(arr)
    
    # Initialize Fibonacci numbers
    fibMMm2 = 0       # (m-2)'th Fibonacci number
    fibMMm1 = 1       # (m-1)'th Fibonacci number
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci number

    # Find the smallest Fibonacci number >= n
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marks the eliminated range from front
    offset = -1

    while fibM > 1:
        # Check if fibMMm2 is a valid index
        i = min(offset + fibMMm2, n - 1)

        if arr[i] < target:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > target:
            fibM = fibMMm2
            fibMMm1 -= fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i

    # Check if the last remaining element is target
    if fibMMm1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestFibonacciSearch(unittest.TestCase):
    def setUp(self):
        self.sorted_list = list(range(0, 1000, 4))  # Uniform increment

    def test_found_values(self):
        self.assertEqual(fibonacci_search(self.sorted_list, 0), 0)
        self.assertEqual(fibonacci_search(self.sorted_list, 200), 50)
        self.assertEqual(fibonacci_search(self.sorted_list, 996), 249)

    def test_not_found_values(self):
        self.assertEqual(fibonacci_search(self.sorted_list, -1), -1)
        self.assertEqual(fibonacci_search(self.sorted_list, 997), -1)
        self.assertEqual(fibonacci_search(self.sorted_list, 1000), -1)

    def test_edge_cases(self):
        self.assertEqual(fibonacci_search([], 1), -1)
        self.assertEqual(fibonacci_search([42], 42), 0)
        self.assertEqual(fibonacci_search([42], 5), -1)

if __name__ == "__main__":
    unittest.main()
