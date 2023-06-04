# Solution-1
def reconstructPermutation(s):
    n = len(s)
    perm = []
    low, high = 0, n

    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1

    perm.append(low)

    return perm
s = "IDID"
# print(reconstructPermutation(s))

# Solution-2
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
# print(searchMatrix(matrix, target))

# Solution-3
def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False
    
    left = 0
    right = n - 1

    while left < n - 1 and arr[left] < arr[left + 1]:
        left += 1

    while right > 0 and arr[right] < arr[right - 1]:
        right -= 1

    if left == right and left != 0 and right != n - 1:
        return True

    return False
arr = [2, 1]
# print(validMountainArray(arr))


# Solution-4
def findMaxLength(nums):
    maxLen = 0
    count = 0
    sumMap = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count -= 1

        if count in sumMap:
            maxLen = max(maxLen, i - sumMap[count])
        else:
            sumMap[count] = i

    return maxLen
nums = [0, 1]
# print(findMaxLength(nums))

# Solution-5
import itertools

def minimumProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)

    minSum = float('inf')

    for perm in itertools.permutations(nums1):
        productSum = sum(a * b for a, b in zip(perm, nums2))
        minSum = min(minSum, productSum)

    return minSum
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
# print(minimumProductSum(nums1, nums2))

# Solution-6
def findOriginalArray(changed):
    frequency = {}

    for num in changed:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    original = []

    for num in changed:
        if frequency[num] == 0:
            continue

        frequency[num] -= 1

        double_num = num * 2

        if double_num not in frequency or frequency[double_num] == 0:
            return []

        frequency[double_num] -= 1
        original.append(num)

    return original
changed = [1, 3, 4, 2, 6, 8]
# print(findOriginalArray(changed))

# Solution-7
def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    direction = 1
    row, col = 0, 0
    rowStart, rowEnd = 0, n - 1
    colStart, colEnd = 0, n - 1

    while num <= n * n:
        matrix[row][col] = num

        if direction == 1:
            if col == colEnd:
                row += 1
                direction = 2
            else:
                col += 1
        elif direction == 2:
            if row == rowEnd:
                colEnd -= 1
                direction = 3
            else:
                row += 1
        elif direction == 3:
            if col == colStart:
                rowEnd -= 1
                direction = 4
            else:
                col -= 1
        elif direction == 4:
            if row == rowStart + 1:
                colStart += 1
                direction = 1
            else:
                row -= 1

        num += 1

    return matrix
n = 3
# print(generateMatrix(n))

# Solution-8
def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k, n = len(mat2), len(mat2[0])

    result = [[0] * n for _ in range(m)]
    sparse_mat1 = {}

    for i in range(m):
        for j in range(k):
            if mat1[i][j] != 0:
                sparse_mat1[(i, j)] = mat1[i][j]

    for i in range(k):
        for j in range(n):
            if mat2[i][j] != 0:
                for row, col in sparse_mat1:
                    if col == i:
                        result[row][j] += mat2[i][j] * sparse_mat1[(row, col)]

    return result
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
# print(multiply(mat1, mat2))

