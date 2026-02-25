def has_triplet(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            s = arr[i] + arr[left] + arr[right]

            if s == target:
                return True
            elif s < target:
                left += 1
            else:
                right -= 1

    return False


print(has_triplet([1, 4, 45, 6, 10, 8], 13))
print(has_triplet([1, 2, 4, 3, 6, 7], 10))
print(has_triplet([40, 20, 10, 3, 6, 7], 24))