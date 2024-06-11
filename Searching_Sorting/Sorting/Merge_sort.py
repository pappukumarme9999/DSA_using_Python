# space complexity = O(n)
# time complexity = O(nlogn)
def merge_two_arrays(arr1, arr2, arr):
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        arr[k] = arr1[i]       
        i += 1
        k += 1
    while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1

def merge_sort(arr):
    if len(arr) <= 1:
          return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_arrays(left, right, arr)

arr = [10,19,8,36,7,55,400,53,20]
merge_sort(arr)
print(arr)










# space complexity = 2n
'''

def merge_two_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):      # comparing the elements of both arrays and appending them to result array
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    # appending the remaining elements of either array to result array
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
            result.append(arr2[j])
            j += 1
    return result

def merge_sort(arr):
    if len(arr) <= 1:
          return arr
    else:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

    return merge_two_arrays(left, right)


'''


