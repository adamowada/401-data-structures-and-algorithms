def array_binary_search(arr, val):
    start = 0
    end = len(arr)-1

    while start <= end:
        temp = start + (end - start) // 2
        if arr[temp] == val:
            return temp
        elif arr[temp] < val:
            start = temp + 1
        else:
            end = temp-1

    return -1