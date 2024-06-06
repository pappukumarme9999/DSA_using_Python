import time
import random

# check if array is sorted in increasing order 
def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

# randomly suffeling the array after every second until the array is sorted  
def monkey_sort(arr):
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)

arr = [10,19,8,36,7,55,400,53,20]
monkey_sort(arr)

