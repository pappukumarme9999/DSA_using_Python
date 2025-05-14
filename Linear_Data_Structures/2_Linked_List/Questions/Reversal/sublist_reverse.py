# Reversing Part of a Linked List (Reverse a Sublist)
# Reverse the list between positions m and n.
# Used in: Partial reversals, sliding window scenarios.

# Example
# Input: 1 → 2 → 3 → 4 → 5, m=2, n=4
# Output: 1 → 4 → 3 → 2 → 5

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_between(head, m, n):
    if not head or m == n:
        return head

    dummy = Node(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before m
    for _ in range(m - 1):
        prev = prev.next

    # Reverse the sublist
    reverse = None
    current = prev.next
    for _ in range(n - m + 1):
        next_node = current.next
        current.next = reverse
        reverse = current
        current = next_node

    # Reconnect
    prev.next.next = current
    prev.next = reverse

    return dummy.next
