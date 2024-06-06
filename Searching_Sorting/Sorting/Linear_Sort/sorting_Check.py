'''
def is_sorted_increasing(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted
def is_sorted_decreasing(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            sorted = False
    return sorted

def is_sorted(arr):
    return is_sorted_increasing(arr) or is_sorted_decreasing(arr)

    
arr1 = [2,3,4,5,6,7,8,9,10]
arr2 = [2,3,4,5,7,6,8,9,10]
arr3 = [10,9,8,7,6,5,4,3,2]
arr4 = [10,9,8,6,7,5,4,3,2]
print('arr1  : ', is_sorted(arr1))
print('arr2  : ', is_sorted(arr2))
print('arr3  : ', is_sorted(arr3))
print('arr4  : ', is_sorted(arr4))

'''

class sorting_validation:
    
    @staticmethod
    def is_sorted_increasing(arr):
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
        return sorted
    
    @staticmethod
    def is_sorted_decreasing(arr):
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                sorted = False
        return sorted
    
    @staticmethod
    def check_sorting(arr):
        if sorting_validation.is_sorted_increasing(arr):
            return 'Sorted in increasing order'
        elif sorting_validation.is_sorted_decreasing(arr):
            return 'Sorted in decreasing order'
        else:
            return 'unsorted array'




if __name__ == '__main__':
    ob = sorting_validation()
    arr1 = [2,3,4,5,6,7,8,9,10]
    arr2 = [2,3,4,5,7,6,8,9,10]
    arr3 = [10,9,8,7,6,5,4,3,2]
    arr4 = [10,9,8,6,7,5,4,3,2]

    print('arr1  : ', ob.check_sorting(arr1))
    print('arr2  : ', ob.check_sorting(arr2))
    print('arr3  : ', ob.check_sorting(arr3))
    print('arr4  : ', ob.check_sorting(arr4))
    
