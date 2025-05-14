class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    current = head
    temp = None

    while current:
        # Swap prev and next
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev  # Was current.next before swap

    # After loop, temp points to old prev of the old head
    if temp:
        head = temp.prev

    return head

# Helper functions
def create_dll(elements):
    head = DLLNode(elements[0])
    current = head
    for val in elements[1:]:
        node = DLLNode(val)
        node.prev = current
        current.next = node
        current = node
    return head

def print_dll(head):
    while head:
        print(head.data, end=" <-> " if head.next else "")
        head = head.next
    print()


dll_head = create_dll([1, 2, 3, 4, 5])
print("Original DLL:")
print_dll(dll_head)

reversed_dll = reverse_doubly_linked_list(dll_head)
print("Reversed DLL:")
print_dll(reversed_dll)
