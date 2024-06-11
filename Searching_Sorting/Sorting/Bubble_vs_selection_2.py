import random
import time


def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

def sort_array(arr):
    while is_sorted(arr) == False:
        random.shuffle(arr)
    return arr

# adaptive bubble sort 
def bubble_sort(arr):
    for i in range(len(arr)-1):      
        flag = 0     
        for j in range(len(arr)-1-i):      
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1 
        if flag == 0:  
            break
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[j]
    return arr



L1 = []
for i in range(10000):
    L1.append(random.randint(1, 10000))

# L2 = L1.copy() 
L2 = L1[:]          #cloning

start1 = time.time()
bubble_sort(L1)
print("Time taken by bubble sort: ", time.time() - start1, " seconds")

start2 = time.time()
selection_sort(L2)
print("Time taken by selection sort: ", time.time() - start2, " seconds")
