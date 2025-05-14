class CSLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_circular_singly_linked_list(head):
    if not head or head.next == head:
        return head

    prev = None
    current = head
    start = head

    while True:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        if current == start:
            break

    head.next = prev  # Maintain circular link
    return prev       # New head



# Helper Functions
def create_csll(elements):
    head = CSLLNode(elements[0])
    current = head
    for val in elements[1:]:
        node = CSLLNode(val)
        current.next = node
        current = node
    current.next = head  # Make circular
    return head

def print_csll(head, count):
    current = head
    for _ in range(count):
        print(current.data, end=" -> ")
        current = current.next
    print("(back to head)")


# Test
csll_head = create_csll([1, 2, 3, 4])
print("Original CSLL:")
print_csll(csll_head, 8)

reversed_csll = reverse_circular_singly_linked_list(csll_head)
print("Reversed CSLL:")
print_csll(reversed_csll, 8)
