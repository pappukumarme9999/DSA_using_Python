# time complexity = O(n^2)
def bubble_sort(arr):

    # (no. of passes = no. of items - 1)
    # no. of comparisons between adjacent pairs, (n-1) comparisons in each pass
    # after every paas, the no. of adjacent pairs reduces by the number of pass
    for i in range(len(arr)-1):                         # pass 
        for j in range(len(arr)-1-i):                   # comparisons
            if arr[j] > arr[j+1]:                       # checking for order
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swapping
    return arr

arr = [10,19,8,36,7,55,400,53,20]
print(bubble_sort(arr))


# -------------------------------------------------------------------------------------


# adaptive Bubble sort 
# time complexity = O(n)
def bubble_sort(arr):

    for i in range(len(arr)-1):      

        flag = 0     
        for j in range(len(arr)-1-i):      
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1        # agar swapping huyi to flag = 1
        if flag == 0:           # check for each pass
            # matlab swapping nhi huyi (array already sorted hai)
            break
    return arr

arr = [10,19,8,36,7,55,400,53,20]
print(bubble_sort(arr))

arr2 = [2,3,4,5,7,6,8,9,10]
print(bubble_sort(arr2))

