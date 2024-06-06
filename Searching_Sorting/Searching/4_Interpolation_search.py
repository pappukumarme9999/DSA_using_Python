def interpolation_search(arr, item):
    length = len(arr)
    low = 0
    high = length - 1
    while low <= high and item >= arr[low] and item <= arr[high]:
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (item - arr[low])))
        if arr[pos] == item:
            return pos
        elif arr[pos] < item:
            low = pos + 1
            print(low)
        else:
            high = pos - 1
            print(high)
        print(pos)
        print(arr[pos])