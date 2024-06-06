def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[j]
    return arr


arr = [10,19,8,36,7,55,400,53,20]
print(selection_sort(arr))

# arr2 = [2,3,4,5,7,6,8,9,10]
# print(selection_sort(arr2))
