# Solution-1
def findCommonElements(arr1, arr2, arr3):
    p1 = p2 = p3 = 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        else:
            minval = min(arr1[p1], arr2[p2], arr3[p3])
            if arr1[p1] == minval:
                p1 += 1
            if arr2[p2] == minval:
                p2 += 1
            if arr3[p3] == minval:
                p3 += 1

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = findCommonElements(arr1, arr2, arr3)
# print(result)

# Solution-2
def findDistinctIntegers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    notinnums2 = list(set1 - set2)
    notInnums1 = list(set2 - set1)

    return [notInnums1, notinnums2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDistinctIntegers(nums1, nums2)
# print(result)

# Solution-3
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
# print(result)

# Solution-4
def arrayPairSum(nums):
    nums.sort()
    maxsum = 0
    for i in range(0, len(nums), 2):
        maxsum += nums[i]
    return maxsum
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
# print(result)

# Solution-5
def arrangeCoins(n):
    k = 0

    while k * (k + 1) / 2 <= n:
        k += 1

    return k - 1
n = 5
result = arrangeCoins(n)
# print(result)

# Solution-6
def sortedSquares(nums):
    result = []
    for num in nums:
        result.append(num * num)
    result.sort()
    return result
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
# print(result)

# Solution-7
def maxCount(m, n, ops):
    maxRow = m
    maxCol = n
    for op in ops:
        maxRow = min(maxRow, op[0])
        maxCol = min(maxCol, op[1])
    return maxRow * maxCol
m = 3
n = 3
ops = [[2, 2], [3, 3]]
result = maxCount(m, n, ops)
print(result)

# Solution-8
def rearrange(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result
nums = [2, 5, 1, 3, 4, 7]
n = 3
result = rearrange(nums, n)
# print(result)



