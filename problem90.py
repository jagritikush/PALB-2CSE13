def largestString(s, k):
    stack = []
    
    for ch in s:
        while k > 0 and stack and stack[-1] < ch:
            stack.pop()
            k -= 1
        stack.append(ch)
    
    return ''.join(stack[:-k] if k else stack)