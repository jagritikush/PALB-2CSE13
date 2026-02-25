def min_swaps(arr, k):
    n = len(arr)
    count = 0
    
    for num in arr:
        if num <= k:
            count += 1
    
    if count == 0:
        return 0
    
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    
    ans = bad
    
    for i in range(n - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)
    
    return ans


arr1 = [2, 1, 5, 6, 3]
print(min_swaps(arr1, 3))

arr2 = [2, 7, 9, 5, 8, 7, 4]
print(min_swaps(arr2, 6))

arr3 = [2, 4, 5, 3, 6, 1, 8]
print(min_swaps(arr3, 6))