# DoublyLinkedList

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0


    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.n += 1


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.prepend(value)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.n += 1


    def insert_at_index(self,index, value):
        if index == 0 or index >= self.n:
            raise IndexError('Index out of range!')
        if index == 0:
            self.prepend(value)
        elif index == (self.n - 1):
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.n += 1


    def insert_after_value(self, after_value, value):
        current = self.head
        while current != None:
            if current.data == after_value:
                new_Node = Node(value)
                new_Node.next = current.next
                new_Node.prev = current
                if current.next != None:    # if it is not the last node
                    current.next.prev = new_Node
                else:
                    self.tail = new_Node
                current.next = new_Node
                self.n += 1
                return
            current = current.next
        raise ValueError(f'{after_value} not found!')



    def delete_head(self):
        if self.head == None:
            raise IndexError('Empty Linked List!')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.n -= 1

    def delete_tail(self):
        if self.tail == None:
            raise IndexError('Empty Linked List!')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.n -= 1


    def delete_at_index(self,index):
        if index < 0 or index >= self.n:
            raise IndexError('Index out of range!')
        if index == 0:
            self.delete_head()
        elif index == (self.n - 1):
            self.delete_tail()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.n -= 1

    def delete_by_value(self, value):
        current = self.head
        while current != None:
            if current.data == value:
                if current == self.head:
                    self.delete_head()
                elif current == self.tail:
                    self.delete_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.n -= 1
                return
            current = current.next
        raise ValueError(f'{value} not found!')

    def find_index(self, value):
        index = 0
        current = self.head
        while current != None:
            if current.data == value:
                return index
            index += 1
            current = current.next
        return -1


    def find_value(self, index):
        if index < 0 or index >= self.n:
            raise IndexError('Index out of range!')
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    

    def print_forward(self):
        str_output = ''
        current = self.head
        while current != None:
            str_output += str(current.data) + '->'
            current = current.next
        return str_output[:-2]


    def print_backward(self):
        str_output = ''
        current = self.tail
        while current != None:
            str_output += str(current.data) + '<-'
            current = current.prev
        return str_output[:-2]
    
    def __len__(self):
        return self.n
    

    def reverse(self):
        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            if current.prev == None:
                self.tail = current
            self.head = current
            current = current.prev


    def __iter__(self):
        current = self.head
        while current != None:
            yield current.data
            current = current.next

    def __iter_reverse__(self):
        current = self.tail
        while current != None:
            yield current.data
            current = current.prev

    def iter_filter(self, predicate):
        current = self.head
        while current != None:
            if predicate(current.data):
                yield current.data
            current = current.next

    def iter_range(self, start, end):
        if start < 0 or end >= self.n or start > end:
            raise IndexError('Index out of range')
        current = self.head
        for _ in range(start):
            current = current.next
        for _ in range(start, end + 1):
            yield current.data
            current = current.next

'''

def __iter_reverse__(self):

Nature: Non-destructive, does not alter the list.
Use Case: Iteration in reverse order.
Performance: Efficient for traversal as it does not require extra space or major computation.
Output: Yields elements from tail to head.


def reverse(self):

Nature: Destructive, alters the list by reversing it.
Use Case: Permanently reverse the list structure.
Performance: Requires in-place modification, iterates through the list once, but changes pointers.
Output: The list is reversed in place, and the head and tail references are updated

'''

dl = DoublyLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)

dl.prepend(0)

print(dl.print_forward())
print(dl.print_backward())

dl.insert_at_index(2, 1.5)

print(dl.print_forward())

dl.delete_by_value(1.5)

print(dl.print_forward())

print(dl.find_index(2)) 
print(dl.find_value(2))

dl.reverse()
print(dl.print_forward())

print("Reverse iteration:")
for value in dl.__iter_reverse__():
    print(value, end=' ')
print()

print("Filtered iteration (even numbers):")
for value in dl.iter_filter(lambda x: x % 2 == 0):
    print(value, end=' ') 
print()

print("Range iteration (index 1 to 2):")
for value in dl.iter_range(1, 2):
    print(value, end=' ') 
print()