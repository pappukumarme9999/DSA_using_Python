class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def iterative_singly_reverse(head):
    prev = None
    current = head
    
    while current:                # while current is not None
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node
    
    return prev                   # New head of the reversed list


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
    
def build_linked_list(elements):
    head = Node(elements[0])
    current = head
    for item in elements[1:]:
        current.next = Node(item)
        current = current.next
    return head


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n1.next = n2
# n2.next = n3
# n3.next = n4

# print("Original List:")
# print_list(n1)

# new_head = iterative_singly_reverse(n1)
# print("Reversed List:")
# print_list(new_head)


head = build_linked_list([1, 2, 3, 4])
print("Original:")
print_list(head)

reversed_head = iterative_singly_reverse(head)
print("Reversed:")
print_list(reversed_head)
