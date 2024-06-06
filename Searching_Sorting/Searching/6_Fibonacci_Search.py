def fibboanacci_search(arr, x):
    # fibM2 = 0
    # fibM1 = 1
    # fibM = fibM1 + fibM2
    while fibM < len(arr):
        fibM2 = fibM1
        fibM1 = fibM
        fibM = fibM1 + fibM2
    while fibM > 1:
        i = min(fibM2, len(arr) - 1)
        if x > arr[i]:
            fibM = fibM1
            fibM1 = fibM2
            fibM2 = fibM - fibM1
        elif x < arr[i]:
            fibM = fibM2
            fibM1 = fibM1 - fibM2
            fibM2 = fibM - fibM1
        else:
            return i
        