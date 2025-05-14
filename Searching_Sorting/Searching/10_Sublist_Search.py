"""
Sublist Search

Problem:
    Determine whether a list (sublist) appears as a contiguous subsequence within another list (main list).

Approach 1: Naive Brute Force (Sliding Window)
    - Slide the sublist window across the main list and check for match at each position
    - Time Complexity: O((n - m + 1) * m)
    
Approach 2: Optimized Pattern Matching (KMP-like)
    - Use pattern preprocessing (e.g., prefix table) to skip unnecessary comparisons
    - Time Complexity: O(n + m)
"""

def sublist_search_naive(main_list, sublist):
    """
    Naive sublist search using sliding window.

    :param main_list: The list to be searched
    :param sublist: The sequence to be found as a contiguous part of main_list
    :return: Starting index of match or -1 if not found
    """
    n, m = len(main_list), len(sublist)

    if m == 0:
        return 0
    if n < m:
        return -1

    for i in range(n - m + 1):
        if main_list[i:i + m] == sublist:
            return i
    return -1


def build_prefix_table(pattern):
    """
    Construct prefix table (failure function) for KMP-style skipping.

    :param pattern: The sublist to be searched
    :return: Prefix table
    """
    prefix = [0] * len(pattern)
    j = 0  # length of previous longest prefix suffix

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
    return prefix


def sublist_search_kmp(main_list, sublist):
    """
    Optimized KMP-style sublist search.

    :param main_list: The list to search in
    :param sublist: The list to find
    :return: Starting index or -1 if not found
    """
    n, m = len(main_list), len(sublist)

    if m == 0:
        return 0
    if n < m:
        return -1

    prefix = build_prefix_table(sublist)
    i = j = 0

    while i < n:
        if main_list[i] == sublist[j]:
            i += 1
            j += 1
            if j == m:
                return i - m
        else:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    return -1


# ------------------------------- TESTING -------------------------------
import unittest

class TestSublistSearch(unittest.TestCase):
    def setUp(self):
        self.main = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_found_naive(self):
        self.assertEqual(sublist_search_naive(self.main, [3, 4, 5]), 2)
        self.assertEqual(sublist_search_naive(self.main, [1]), 0)
        self.assertEqual(sublist_search_naive(self.main, [9]), 8)

    def test_not_found_naive(self):
        self.assertEqual(sublist_search_naive(self.main, [10, 11]), -1)
        self.assertEqual(sublist_search_naive(self.main, [4, 6]), -1)

    def test_found_kmp(self):
        self.assertEqual(sublist_search_kmp(self.main, [3, 4, 5]), 2)
        self.assertEqual(sublist_search_kmp(self.main, [1]), 0)
        self.assertEqual(sublist_search_kmp(self.main, [9]), 8)

    def test_not_found_kmp(self):
        self.assertEqual(sublist_search_kmp(self.main, [10, 11]), -1)
        self.assertEqual(sublist_search_kmp(self.main, [4, 6]), -1)

    def test_edge_cases(self):
        self.assertEqual(sublist_search_naive([], []), 0)
        self.assertEqual(sublist_search_kmp([], []), 0)
        self.assertEqual(sublist_search_naive([], [1]), -1)
        self.assertEqual(sublist_search_kmp([], [1]), -1)

if __name__ == "__main__":
    unittest.main()
