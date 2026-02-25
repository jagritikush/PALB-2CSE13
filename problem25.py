def is_palindrome(num):
    return str(num) == str(num)[::-1]

def all_palindromes(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


arr1 = [111, 222, 333, 444, 555]
print(all_palindromes(arr1))

arr2 = [121, 131, 20]
print(all_palindromes(arr2))