def rotate_clockwise(arr):
    n= len(arr)
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
     
        
    arr[0]=last 
    return arr

arr = [1,2,3,4,5]
rotated_arr = rotate_clockwise(arr)
print("Rotated array:",rotated_arr)