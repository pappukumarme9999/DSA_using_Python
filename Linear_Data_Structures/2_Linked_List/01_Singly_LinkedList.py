class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0


    def __len__(self):
        return self.n
    

    def insert_head(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.n += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.n += 1

    def append(self, value):
        if self.head == None:
            self.insert_head(value)
        newNode = Node(value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.n += 1


    def insert_at_index(self, index, value):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        if self.head == None:
            return "Empty LinkedList"
        if index == 0:
            return self.insert_head(value)
        count = 0
        newNode = Node(value)
        current = self.head
        while current != None:
            if count == index-1:
                break
            current = current.next
            count += 1
        newNode.next = current.next
        current.next = newNode
        self.n += 1

        
    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current:
            if current.data == after:
                break
            current = current.next
        if current:
            new_node.next, current.next = current.next, new_node
            self.n += 1
        else:
            return 'Data not found'


    def __str__(self):
        if self.head == None:
            return "Empty LinkedList"
        str_result = ""
        current = self.head
        while current:
            str_result = str_result + str(current.data) + "->"
            current = current.next
        return str_result[:-2]
    

    def clear(self):
        self.head = None
        self.n = 0


    def delete_head(self):
        if self.head == None:
            raise IndexError("Empty LinkedList")
        self.head = self.head.next
        self.n -= 1


    def pop(self):
        if self.head == None:
            raise IndexError("Empty LinkedList")
        if self.head.next == None:
            return self.delete_head()
        current = self.head
        while current.next.next != None:
            current = current.next
        current.next = None
        self.n -= 1


    # delete by value 
    def remove(self, value):
        if self.head == None:
            raise IndexError("Empty LinkedList")
        if self.head.data == value:
            return self.delete_head()
        current = self.head 
        while current.next != None:
            if current.next.data == value:
                current.next = current.next.next
                self.n -= 1
                return
            current = current.next
        return "Item not found"
    

    def delete_at_index(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        if self.head == None:
            return "Empty LinkedList"
        if index == 0:
            return self.delete_head()
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.n -= 1


    def search_by_value(self, value):
        current = self.head
        index = 0
        while current != None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return "Not Found"


    # __getitem__ method 
    def search_by_index(self, index):
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")
        if self.head == None:
            return "Empty LinkedList"
        current = self.head
        position = 0
        while current != None:
            if position == index:
                return current.data
            current = current.next
            position += 1


        
l = LinkedList()

# __len__
# insert_head
# append
# insert_at_index
# insert_after
# __str__
# clear
# delete_head
# pop
# remove
# delete_at_index
# search_by_value
# search_by_index


l.insert_head(10)
l.insert_head(20)
l.insert_head(30)
l.insert_head(40)
l.insert_head(50)


print('L :', l)
print('Length: ', l.__len__())
print('--------------------------------------------------')



l.insert_head(999)
print('L :', l)

l.insert_after(20, 99)
print('L :', l)

l.insert_at_index(4, 100)
print('L :', l)

l.append(11.11)
print('L :', l)

print('Data using __str__: ', l.__str__())
print('Length: ', l.__len__())


print('--------------------------------------------------')


print('Searching for 100: ', l.search_by_value(100))
print('searching by index(3): ', l.search_by_index(3))


print('--------------------------------------------------')


l.delete_head()
print('L :', l)

l.pop()
print('L :', l)

l.remove(99)
print('L :', l)

l.delete_at_index(3)
print('L :', l)

print('deleting everything....')
l.clear()
print('L :', l)


print('--------------------------------------------------')

