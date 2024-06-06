def binary_search(arr, target):
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


def exponential_search(arr, item):
    if arr[0] == item:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= item:
        i *= 2
    return binary_search(arr[:i], item)
