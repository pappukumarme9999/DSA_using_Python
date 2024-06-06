'''

Binary search
    -> finding an item from a sorted list
    -> works by repeatedly dividing in half the portion of the list that could contain the item, until you narrow down the possible locations to just one.

    
---------------------------------------------------------------------------------
Time Complexity: O(log n)
Space Complexity: O(1) for iterative binary search, 
                  O(log n) for recursive binary search due to the call stack.
Requirement: The list must be sorted.
    
----------------------------------------------------------------------------------
Applications
1. Finding an Element in a Sorted Array

2. Efficiently Finding the Lower/Upper Bound
Binary search can be modified to find the lower or upper bounds of an element in a sorted array. This is useful in range queries and problems where you need to find the first or last occurrence of a number.

3. Search in Infinite Sorted Arrays
Binary search can be adapted to work with infinite sorted arrays by first finding a suitable range where the target might exist.

4. Dictionary Lookup
Binary search trees or balanced trees (like AVL trees, Red-Black trees) use binary search principles to maintain a sorted order of elements, enabling efficient search, insert, and delete operations.

5. Finding Square Root or Other Numerical Methods
Binary search can be used to find the square root of a number or solve equations numerically by searching within a range.

6. Database Indexing
Databases often use B-trees or B+ trees, which are variants of binary search trees, to index data efficiently and support fast query retrieval.

'''





# suppose the array is sorted in increasing order 

# recursive 
def binary_search_recursive(arr, low, high, item):
    # we can remove the "low" and "high" parameters if we want to searh through the whole array, and initialize the local variable. 
    # low, high = 0, len(arr) - 1
    if low <= high:
        mid = low + (high-low)//2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:                       # item will on left side of the array
            return binary_search_recursive(arr, low, mid-1, item)
        else:                                       # item will on right side of the array
            return binary_search_recursive(arr, mid+1, high, item)
    
    else:
        return -1
    
arr1 = [2,5,6,9,11,15,18,56,65,66,90,99,101]
print(binary_search_recursive(arr1, 0, len(arr1)-1, 2))
print(binary_search_recursive(arr1, 0, len(arr1)-1, 101))
print(binary_search_recursive(arr1, 3, 10, 66))            # custom searching

result = binary_search_recursive(arr1, 0, len(arr1) - 1, 200)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

# -----------------------------------------------------------------------------------

# iterative 
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr2 = [2,5,6,9,11,15,18,56,65,66,90,99,101]
print(binary_search_iterative(arr2, 2))
print(binary_search_iterative(arr2, 101))

result = binary_search_iterative(arr2, 200)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
