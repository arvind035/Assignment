# Solution-1
def isPowerOfTwo(n):
    if n <= 0:
        return False
    
    while n % 2 == 0:
        n = n // 2
    
    return n == 1

# print(isPowerOfTwo(1))
# print(isPowerOfTwo(16))
# print(isPowerOfTwo(3))

# Solution-2
def sumOfFirstN(n):
    return (n * (n + 1)) // 2

# print(sumOfFirstN(3))
# print(sumOfFirstN(5))

# Solution-3
# Using Recursion
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

# print(factorial(5))
# print(factorial(4))
# Using loop
def factorial(N):
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    return fact

# print(factorial(5))
# print(factorial(4))

# Solution-4
def calculate_exponent(N, P):
    result = N ** P
    return result

# print(calculate_exponent(5, 2))
# print(calculate_exponent(2, 5))

# Solution-5
def find_max(arr, start, end):
    if start == end:
        return arr[start]
    mid = (start + end) // 2
    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)
    return max(left_max, right_max)

arr = [1, 4, 3, -5, -4, 8, 6]
# print(find_max(arr, 0, len(arr) - 1))

arr = [1, 4, 45, 6, 10, -8]
# print(find_max(arr, 0, len(arr) - 1))

# Solution-6
def find_nth_term(a, d, N):
    return a + (N - 1) * d

a = 2
d = 1
N = 5
# print(find_nth_term(a, d, N))

a = 5
d = 2
N = 10
# print(find_nth_term(a, d, N))

# Solution-7
def permute(s):
    chars = list(s)
    n = len(chars)
    result = []

    def backtrack(start):
        if start == n:
            result.append(''.join(chars))
            return

        for i in range(start, n):
            chars[start], chars[i] = chars[i], chars[start]
            backtrack(start + 1)
            chars[start], chars[i] = chars[i], chars[start]
    backtrack(0)
    return result

S = "ABC"
# print(permute(S))

S = "XY"
# print(permute(S))

# Solution-8
def productOfArray(arr):
    product = 1
    for num in arr:
        product *= num
    return product

arr = [1, 2, 3, 4, 5]
# print(productOfArray(arr))

arr = [1, 6, 3]
# print(productOfArray(arr))
