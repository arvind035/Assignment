# Solution-1
def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []

    result = []
    index = 0

    for i in range(m):
        row = []
        for j in range(n):
            row.append(original[index])
            index += 1
        result.append(row)

    return result
original = [1, 2, 3, 4]
m = 2
n = 2
# print(convert_to_2d_array(original, m, n))

# Solution-2
def countCompleteRows(n):
    left, right = 1, n
    complete_rows = 0

    while left <= right:
        mid = left + (right - left) // 2
        total_coins = (mid * (mid + 1)) // 2

        if total_coins <= n:
            complete_rows = mid
            left = mid + 1
        else:
            right = mid - 1

    return complete_rows
n = 5
# print(countCompleteRows(n))

# Solution-3
def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num ** 2)

    return sorted(result)
nums = [-4, -1, 0, 3, 10]
# print(sortedSquares(nums))

# solution-4
def findDisappearedNumbers(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result1 = []
    result2 = []

    for num in nums1:
        if num not in set2:
            result1.append(num)

    for num in nums2:
        if num not in set1:
            result2.append(num)

    return [result1, result2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
# print(findDisappearedNumbers(nums1, nums2))

# Solution-5
def findTheDistanceValue(arr1, arr2, d):
    distance = 0

    for num1 in arr1:
        found = False
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break
        if not found:
            distance += 1

    return distance
arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
# print(findTheDistanceValue(arr1, arr2, d))

# Solution-6
def findDuplicates(nums):
    result = []

    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] *= -1
        else:
            result.append(abs(num))

    return result
nums = [4, 3, 2, 7, 8, 2, 3, 1]
# print(findDuplicates(nums))

# Solution-7
def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
nums = [3, 4, 5, 1, 2]
# print(findMin(nums))

# Solution-8
from collections import defaultdict

def findOriginalArray(changed):
    count = defaultdict(int)
    for num in changed:
        count[num] += 1

    original = []
    for num in changed:
        if count[num] == 0:
            continue
        if num % 2 != 0 or count[num] == 0:
            return []
        count[num] -= 1
        count[num//2] -= 1
        original.append(num // 2)

    return original
changed = [1, 3, 4, 2, 6, 8]
# print(findOriginalArray(changed))

