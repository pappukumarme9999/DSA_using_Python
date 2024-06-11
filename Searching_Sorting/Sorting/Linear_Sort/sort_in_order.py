# always sort in increasing order 

import random

def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

# this function will always sort the array in ascending order 
# because it validates the above codition "is_sorted" which checks for increasing order
def monkey_sort(arr):
    while is_sorted(arr) == False:
        random.shuffle(arr)
    return arr
    
def reverse_order(arr):
    return arr[::-1]



arr = [10,19,8,36,7,55,400,53,20]
print("is Sorted? ", is_sorted(arr))
print("sorted in ascending: ", monkey_sort(arr))
print("sorted in decending: ", reverse_order(arr))
