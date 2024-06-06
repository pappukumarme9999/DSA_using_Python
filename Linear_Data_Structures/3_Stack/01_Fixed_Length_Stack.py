# stack of fixed length, using array

class Stack:


    def __init__(self, size):

        self.size = size
        self._stack_ = [None]*self.size
        self.top = -1


    def push(self, value):

        if self.top == self.size - 1:
            return "OverFlow"
        else:
            self.top += 1
            self._stack_[self.top] = value


    def pop(self):

        if self.top == -1:
            return 'Empty _Stack_'
        else:
            data = self._stack_[self.top]
            self._stack_[self.top] = None   # explicitly remove elements from memory
            self.top -= 1
            return data

    
    def traverse(self):

        for i in range(self.top + 1):
            print(self._stack_[i], end=' ')






s = Stack(3)
print('New stack: ', s._stack_)
print()

print('Pushing 11 - ',s.push(11))
print('Traversing:', end=' ')
s.traverse()
print()
print()

print('Pushing 21 - ',s.push(21))
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Pushing 31 - ',s.push(31))
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Pushing 41 - ',s.push(41))
print()

print('Printing _stack_: ', s._stack_)
print()

print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Popping - ', s.pop())
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Popping - ', s.pop())
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Popping - ', s.pop())
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Popping - ', s.pop())
print('Traversing: ', end=' ')
s.traverse()
print()
print()

print('Printing _stack_: ', s._stack_)



















'''
Memory Management in Python:
Python uses a memory management system that includes reference counting and a garbage collector.
When an object (such as a list or an array) is created, Python keeps track of how many references point to it.
When the reference count drops to zero (i.e., no variables or data structures reference the object), 
Python’s garbage collector deallocates the memory associated with that object.

When you pop elements from the stack, the top index is decremented, 
but the elements themselves are not explicitly removed from memory.

Garbage Collection:
Python’s garbage collector does not immediately reclaim memory for objects that are no longer referenced.
Instead, it periodically scans the memory and deallocates objects that are no longer reachable.
This delayed cleanup allows Python to manage memory efficiently without causing performance overhead during frequent push and pop operations.

If you want to explicitly remove elements from memory, you can set them to None after popping them from the stack.
self._stack_[self.top] = None

'''
