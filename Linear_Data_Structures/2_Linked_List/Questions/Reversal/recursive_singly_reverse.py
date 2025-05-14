class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def recursive_singly_reverse(head):
    if head is None or head.next is None:
        return head

    new_head = recursive_singly_reverse(head.next)
    head.next.next = head
    head.next = None

    return new_head

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


head = build_linked_list([1, 2, 3, 4])
print("Original:")
print_list(head)

reversed_head = recursive_singly_reverse(head)
print("Reversed:")
print_list(reversed_head)
