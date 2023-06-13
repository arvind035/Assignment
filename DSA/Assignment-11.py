# Solution-1
def mySqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right

x1 = 4
result1 = mySqrt(x1)
print(result1)

x2 = 8
result2 = mySqrt(x2)
print(result2)

# Solution-2
def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

nums1 = [1, 2, 3, 1]
result1 = findPeakElement(nums1)
print(result1)

nums2 = [1, 2, 1, 3, 5, 6, 4]
result2 = findPeakElement(nums2)
print(result2)

# Solution-3
def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    array_sum = sum(nums)
    missing_num = total_sum - array_sum
    return missing_num

# Example usage
nums1 = [3, 0, 1]
result1 = missingNumber(nums1)
print(result1)

nums2 = [0, 1]
result2 = missingNumber(nums2)
print(result2)

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
result3 = missingNumber(nums3)
print(result3)

# Solution-4
def findDuplicate(nums):
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

nums1 = [1, 3, 4, 2, 2]
result1 = findDuplicate(nums1)
# print(result1)

nums2 = [3, 1, 3, 4, 2]
result2 = findDuplicate(nums2)
# print(result2)

# Solution-5
def intersection(nums1, nums2):
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result1 = intersection(nums1, nums2)
# print(result1)

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
result2 = intersection(nums3, nums4)
# print(result2)

# Solution-6
def findMin(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] <= nums[right]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

nums1 = [3, 4, 5, 1, 2]
result1 = findMin(nums1)
# print(result1)

nums2 = [4, 5, 6, 7, 0, 1, 2]
result2 = findMin(nums2)
# print(result2)

nums3 = [11, 13, 15, 17]
result3 = findMin(nums3)
# print(result3)

# Solution-7
def searchRange(nums, target):
    left = findLeftPosition(nums, target)
    right = findRightPosition(nums, target)

    return [left, right]

def findLeftPosition(nums, target):
    left = 0
    right = len(nums) - 1
    position = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

        if nums[mid] == target:
            position = mid

    return position

def findRightPosition(nums, target):
    left = 0
    right = len(nums) - 1
    position = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

        if nums[mid] == target:
            position = mid

    return position

nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
result1 = searchRange(nums1, target1)
print(result1)

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
result2 = searchRange(nums2, target2)
# print(result2)

nums3 = []
target3 = 0
result3 = searchRange(nums3, target3)
# print(result3)

# Solution-8
from collections import Counter

def intersect(nums1, nums2):
    counter = Counter(nums1)
    intersection = []

    for num in nums2:
        if num in counter and counter[num] > 0:
            intersection.append(num)
            counter[num] -= 1

    return intersection

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result1 = intersect(nums1, nums2)
# print(result1)

nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
result2 = intersect(nums3, nums4)
# print(result2)
