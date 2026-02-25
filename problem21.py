def min_difference_choclates(arr,m):
    n=len(arr)
    if m==0 or n==0:
        return 0
    if m>n:
        return -1
    arr.sort()
    
    min_diff=float('inf')
    for i in range(n-m+1):
        diff=arr[i+m-1]-arr[i]
        
    return min_diff
#arr=[3,4,1,9,56,7,9,12]
arr=[7,3,2,4,9,12,56]
m=5
print(f"Minimum difference is {min_difference_choclates(arr,m)}")