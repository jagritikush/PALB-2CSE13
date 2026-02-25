def smallest_subarray(x, arr):
    n = len(arr)
    min_len = n + 1
    curr_sum = 0
    start = 0
    
    for end in range(n):
        curr_sum += arr[end]
        
        while curr_sum > x:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1
    
    if min_len == n + 1:
        return 0
    return min_len


x1 = 51
arr1 = [1, 4, 45, 6, 0, 19]
print(smallest_subarray(x1, arr1))

x2 = 100
arr2 = [1, 10, 5, 2, 7]
print(smallest_subarray(x2, arr2))