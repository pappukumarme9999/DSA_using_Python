import math

def jump_search(arr, x):

    n = len(arr)
    previous = 0
    step = int(math.sqrt(n))

    #  index accessed within the array does not exceed the array length
    while arr[min(step, n) - 1] < x:
        # min(step, n) -> This ensures that if "step" exceeds "n", it will use "n" instead.
        previous = step
        step += int(math.sqrt(n))
        if previous >= n:
            return -1
        
    # Doing a linear search for x in block beginning with prev
    while arr[previous] < x:
        previous += 1
        if previous == min(step, n):
            return -1
        
    # If element is found  
    if arr[previous] == x:
            return previous
    
    return -1
    
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 7
index = jump_search(arr, x)
print(f"Number {x} is at index {index}")



'''

import math

def jump_search(arr, item):
    length = len(arr)
    step = int(math.sqrt(length))
    prev = 0 
    
    while prev < length and arr[min(step, length) - 1] < item:
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1 
    
    while prev < min(step, length) and arr[prev] < item:
        prev += 1
        if prev == min(step, length):
            return -1 
    
    if prev < length and arr[prev] == item:
        return prev
    
    return -1

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
x = 7
index = jump_search(arr, x)
print(f"Number {x} is at index {index}")

'''
