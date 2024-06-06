class Stack:

    def __init__(self, size):
        self.size = size
        self.stack_items = []

    def push(self, item):
        if self.is_full():
            print('Stack is full')
        self.stack_items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty!')
        return self.stack_items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty!')
        return self.stack_items[-1]
    
    def is_empty(self):
        return len(self.stack_items) == 0
    
    def is_full(self):
        return len(self.stack_items) >= self.size

    def __len__(self):
        return self.size
    
    def get_data(self):
        return self.stack_items
    

def rev_String(str):
    my_Stack = Stack(len(str))
    new_String = ''
    for data in str:
        my_Stack.push(data)

    while not my_Stack.is_empty():
        new_String += my_Stack.pop()

print(rev_String('abcd'))