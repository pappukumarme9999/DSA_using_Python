# creating individual notes and connecting them

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# creating objects

obj_node_1 = Node(4)
obj_node_2 = Node(5)
obj_node_3 = Node(6)


# creating a linked list by connecting nodes
obj_node_1.next = obj_node_2
obj_node_2.next = obj_node_3


print('Node_1')
print('ID = ', id(obj_node_1))
print('Data = ', obj_node_1.data)
print('Next = ', obj_node_1.next)

print('-----------------------------------------')

print('Node_2')
print('ID = ', id(obj_node_2))
print('Data = ', obj_node_2.data)
print('Next = ', obj_node_2.next)

print('-----------------------------------------')

print('Node_3')
print('ID = ', id(obj_node_3))
print('Data = ', obj_node_3.data)
print('Next = ', obj_node_3.next)
