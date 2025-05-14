class CDLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_circular_doubly_linked_list(head):
    if not head or head.next == head:
        return head

    current = head
    while True:
        current.prev, current.next = current.next, current.prev
        current = current.prev  # Because we swapped pointers
        if current == head:
            break

    return head.prev  # New head is old tail


# Helper Functions
def create_cdll(elements):
    head = CDLLNode(elements[0])
    current = head
    for val in elements[1:]:
        node = CDLLNode(val)
        node.prev = current
        current.next = node
        current = node
    current.next = head
    head.prev = current
    return head

def print_cdll(head, count):
    current = head
    for _ in range(count):
        print(current.data, end=" <-> ")
        current = current.next
    print("(back to head)")


# Test
cdll_head = create_cdll([10, 20, 30, 40])
print("Original CDLL:")
print_cdll(cdll_head, 8)

reversed_cdll = reverse_circular_doubly_linked_list(cdll_head)
print("Reversed CDLL:")
print_cdll(reversed_cdll, 8)
