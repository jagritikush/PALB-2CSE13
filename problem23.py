def three_way_partition(arr, a, b):
    start = 0
    end = len(arr) - 1
    i = 0
    
    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            start += 1
            i += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    
    return True


arr1 = [1, 2, 3, 3, 4]
print(three_way_partition(arr1, 1, 2), arr1)

arr2 = [1, 4, 3, 6, 2, 1]
print(three_way_partition(arr2, 1, 3), arr2)