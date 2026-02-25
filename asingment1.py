def reverse_array(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

# Example
arr = [1, 4, 3, 2, 6, 5]
print(reverse_array(arr))

def find_min_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    
    for num in arr:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return [min_val, max_val]


arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr)) 
