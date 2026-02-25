def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    
    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)
    
    desired = (n * m) // 2
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        
        for row in mat:
            l, r = 0, m
            while l < r:
                md = (l + r) // 2
                if row[md] <= mid:
                    l = md + 1
                else:
                    r = md
            count += l
        
        if count <= desired:
            low = mid + 1
        else:
            high = mid
    
    return low


mat1 = [[1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]]
print(matrix_median(mat1))

mat2 = [[2, 4, 9],
        [3, 6, 7],
        [4, 7, 10]]
print(matrix_median(mat2))

mat3 = [[3],
        [4],
        [8]]
print(matrix_median(mat3))