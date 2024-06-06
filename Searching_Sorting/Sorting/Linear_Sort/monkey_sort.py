import random

# check if array is sorted in increasing order 
def is_sorted_increasing(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

# check if array is sorted in decreasing order 
def is_sorted_decreasing(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            sorted = False
    return sorted


# check if array is sorted in any of increasing or decreasing order 
def is_sorted(arr):
    return is_sorted_increasing(arr) or is_sorted_decreasing(arr)


# find out the order of sorting 
def order(arr):
    if is_sorted(arr):
        if is_sorted_increasing(arr):
            return "increasing"
        return "decreasing"
    return 'unsorted'


# sort an array 
def monkey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    return arr
    

# reverse the order of an array 
def reverse_order(arr):
    if is_sorted(arr):
        return arr[::-1]
    
     

'''
# convert decreasing to increasing 
def convert_to_increasing(arr):
    if is_sorted_decreasing(arr):
        return reverse_order(arr)

    
# convert increasing to decreasing
def convert_to_decreasing(arr):
    if is_sorted_increasing(arr):
        return reverse_order(arr)
'''




arr1 = [2,3,4,5,6,7,8,9,10]
print('original arr1: ', arr1)
print('is arr1 sorted : ', is_sorted(arr1))
print('order of arr1 : ', order(arr1))
print('order reversed: ', reverse_order(arr1))
print('--------------------------------------------')

arr2 = [10,9,8,7,6,5,4,3,2]
print('original arr2: ', arr2)
print('is arr2 sorted : ', is_sorted(arr2))
print('order of arr2 : ', order(arr2))
print('order reversed: ', reverse_order(arr2))
print('--------------------------------------------')


arr3 = [10,19,8,36,7,55,400,53,20]
print('original arr3: ', arr3)
print('is arr3 sorted : ', is_sorted(arr3))
sorted = monkey_sort(arr3)
print('sorted array : ', sorted)
print('order of arr3 : ', order(arr3))
print('order reversed: ', reverse_order(sorted))
print('--------------------------------------------')
