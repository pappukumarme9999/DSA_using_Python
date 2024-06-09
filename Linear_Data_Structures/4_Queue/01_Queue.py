class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        # print("insertion started")
        if self.rear == None:
            self.front = new_node = self.rear
        else:
            self.rear.next = new_node
            self.rear = new_node
        # print("insertion done")

    def dequeue(self):
        if self.front == None:
            return "Empty Queue"
        else:
            self.front = self.front.next

    def traverse(self):
        current = self.front
        # print("Traversal started")
        while current != None:
            print(current.data, end=" ")
            current = current.next
        # print("Traversal done")

    def peek(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.front.data
        
    def is_empty(self):
        return self.front == None
    
    def size(self):
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    
    def front_item(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.front.data
        
    def rear_item(self):
        if self.front == None:
            return "Empty Queue"
        else:
            return self.rear.data
    

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.traverse()
print(q.size())