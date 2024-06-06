# stack of dynamic size using linked list 

from typing import Any

class Node:
    def __init__(self, value) -> None:
        '''initialize a node with a value'''
        self.data = value
        self.next = None

class  Stack:
    def __init__(self) -> None:
        self.top = None
        self.n = 0

    def is_empty(self) -> bool:
        return self.top == None
    
    def push(self, value) -> None:
        new_node = Node(value)
        new_node.next, self.top = self.top, new_node
        self.n += 1
    
    def pop(self) -> None:
        if self.is_empty():
            raise IndexError('Stack is empty!')
        self.top = self.top.next
        self.n -= 1

        # implement these three lines to get the popped element as output 
        # popped_element = self.top.data    
        # self.top = self.top.next
        # return popped_element

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError('Stack is empty!')
        return self.top.data     

    def __len__(self) -> int:
        return self.n

    def clear(self) -> None:
        self.top = None
        self.n = 0

    def __str__(self) -> str:
        if self.is_empty():
            return 'Stack is empty!'
        current = self.top
        s_str = ''
        while current:
            s_str += str(current.data) + '->'
            current = current.next
        return s_str.rstrip('->')
        # return s_str[:-2]


s = Stack()

print('Stack: ', s)
print('Empty? ',s.is_empty())


print('------------------------------')
print('Pushing........')

s.push(10)
print(s)

s.push(20)
print(s)

s.push(30)
print(s)

s.push(40)
print(s)

s.push(50)
print(s)


print('------------------------------')

print('Stack: ', s)
print('Len: ', len(s))
print('Empty? ',s.is_empty())

print('------------------------------')


print('Peek: ', s.peek())

print('------------------------------')
print('Popping........')

s.pop()
print(s)

s.pop()
print(s)

print('------------------------------')

print('Stack: ', s)
print('Len: ', len(s))
print('Empty? ',s.is_empty())


print('------------------------------')

print('deleting the stack.......')
s.clear()
print('Stack: ', s)
print('Len: ', len(s))
print('Empty? ',s.is_empty())

print('------------------------------')
