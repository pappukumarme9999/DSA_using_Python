class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None


    def add_to_empty(self, value):
        if self.head != None:
            return
        self.head = Node(value)
        self.head.next = self.head

    def insert_head(self, value):
        if self.head == None:
            self.add_to_empty(value)
            return
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def append(self, value):
        if self.head == None:
            self.add_to_empty(value)
            return
        else:
            new_node = Node(value)
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

'''


    def add_after(self, data, item):
        if self.head is None:
            return
        new_node = Node(data)
        current = self.head
        while True:
            if current.data == item:
                new_node.next = current.next
                current.next = new_node
                if current == self.head:
                    self.head = new_node
                return
            current = current.next
            if current == self.head:
                break

    def delete_node(self, key):
        if self.head is None:
            return

        current = self.head
        prev = None

        while True:
            if current.data == key:
                if current == self.head:
                    while current.next != self.head:
                        current = current.next
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        current.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head.next
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head.next:
                break
        print()

# Example usage:
cll = CircularLinkedList()
cll.add_to_end(1)
cll.add_to_end(2)
cll.add_to_end(3)
cll.add_to_beginning(0)
cll.add_after(1.5, 1)
cll.display()  # Output: 0 1 1.5 2 3
cll.delete_node(1.5)
cll.display()  # Output: 0 1 2 3
cll.delete_node(0)
cll.display()  # Output: 1 2 3


'''