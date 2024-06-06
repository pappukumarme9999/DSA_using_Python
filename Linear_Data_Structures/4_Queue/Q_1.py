# queue using linkedList 

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None



    # insert at tail 
    def enqueue(self, value):

        new_node = Node(value)

        # if self.rear is None:
        #     self.front = self.rear = new_node

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node



    # delete from head 
    # def dequeue(self):
    #     if self.is_empty():
    #         return 'Empty Queue'
    #     else:
    #         self.front = self.front.next


    # def dequeue(self):
        # if not self.is_empty():
        #     self.front = self.front.next


    # def dequeue(self):
        # if self.front == None:
        #     return 'Empty Queue'
        # else:
        #     self.front = self.front.next


    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        else:
            dequeued_value = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_value



    def traverse(self):
        current = self.front
        while current != None:
            print(current.data, end=' ')
            current = current.next


    # def traverse(self):
    #     if self.front is None:
    #         return "Queue is empty"
    #     else:
    #         current = self.front
    #         while current:
    #             print(current.data, end=' ')
    #             current = current.next



    def is_empty(self):
        return self.front == None
    

    def len(self):
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count
    

    def peek_front(self):
        if self.is_empty():
            return 'Empty Queue'
        return self.front.data
    
    def peek_rear(self):
        if self.is_empty():
            return 'Empty Queue'
        return self.rear.data
    

            
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue('ssp')
q.enqueue(40)
q.enqueue(False)
q.enqueue(30)

print('Queued elements:', end=' ')
q.traverse()
print()

print('Length: ', q.len())
print()

print('first element: ', q.peek_front())
print('last element: ', q.peek_rear())
print()

print('is empty: ', q.is_empty())
print()

print('Dqueueing: ')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())
print()

print('Queued elements:', end=' ')
q.traverse()
print()

print('is empty: ', q.is_empty())
print()

print('first element: ', q.peek_front())
print('last element: ', q.peek_rear())
print()
