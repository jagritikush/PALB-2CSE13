def factorial_digits(n):
    result = [1]

    for x in range(2, n + 1):
        carry = 0
        for i in range(len(result)):
            product = result[i] * x + carry
            result[i] = product % 10
            carry = product // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

    return result[::-1]


print(factorial_digits(5))
print(factorial_digits(10))
print(factorial_digits(1))