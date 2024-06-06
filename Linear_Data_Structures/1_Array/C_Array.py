# creating a dynamic array(list) using c language types 
import ctypes
class myList:
    def __init__(self):
        self.size = 1       # size - how many elements can be stored
        self.n = 0          # n - how many elements are currently stored

        #  storing the c type array in a variable myVab
        self.myVab = self.__make_array(self.size)

    # creating a c type array with size : self.size
    def __make_array(self, capacity):
        return (capacity*ctypes.py_object)()
    
    # adding a length feature to the created array
    def __len__(self):
        return self.n
    
    # adding a print function to the array
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.myVab[i]) + ','
        return '[' + result[:-1] + ']'
    
    # adding an append function to our array
    def append(self, item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)
        
        else:
            self.myVab[self.n] = item
            self.n = self.n+1

    def __resize(self, new_capacity):
        # creating a new array with new capacity
        myVab2 = self.__make_array(new_capacity)
        self.size = new_capacity

        # copying the context from first array to the next array
        for i in range(self.n):
            myVab2[i] = self.myVab[i]
        
        # reassign myVab
        self.myVab = myVab2
    
newArr = myList()

print(type(newArr))
print(len(newArr))
print('--------------------1---------------------')
newArr.append('hello')
print(len(newArr))
print('--------------------2---------------------')
newArr.append(33333)
print(len(newArr))
print('--------------------3---------------------')
newArr.append(-12)
print(len(newArr))
print('---------------------4--------------------')
newArr.append(201.3)
print(len(newArr))
print('----------------------5-------------------')
newArr.append(232)
print(len(newArr))
print('---------------------6--------------------')
newArr.append('ffff')
print(len(newArr))
print('---------------------7--------------------')
newArr.append(0022.032)
print(len(newArr))
print('---------------------8--------------------')

print(newArr)
