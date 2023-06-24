# Solution-1
def merge_intervals(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)

    return merged
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals1))

intervals2 = [[1, 4], [4, 5]]
print(merge_intervals(intervals2))

# Solution-2
def sortColors(nums):
    red_end = 0
    white_start = 0
    blue_start = len(nums) - 1

    while white_start <= blue_start:
        if nums[white_start] == 0:
            nums[white_start], nums[red_end] = nums[red_end], nums[white_start]
            red_end += 1
            white_start += 1
        elif nums[white_start] == 1:
            white_start += 1
        else:
            nums[white_start], nums[blue_start] = nums[blue_start], nums[white_start]
            blue_start -= 1

    return nums
nums1 = [2, 0, 2, 1, 1, 0]
print(sortColors(nums1))

nums2 = [2, 0, 1]
# print(sortColors(nums2))

# Solution-3
def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

# Solution-4
def maximumGap(nums):
    if len(nums) < 2:
        return 0

    max_num = max(nums)

    exp = 1
    while max_num // exp > 0:
        countingSort(nums, exp)
        exp *= 10

    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - nums[i - 1])

    return max_diff


def countingSort(nums, exp):
    count = [0] * 10
    n = len(nums)
    output = [0] * n

    for num in nums:
        count[(num // exp) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (nums[i] // exp) % 10
        output[count[digit] - 1] = nums[i]
        count[digit] -= 1

    for i in range(n):
        nums[i] = output[i]

# Solution-5
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

# Solution-6
def findMinArrowShots(points):
    if len(points) == 0:
        return 0

    points.sort(key=lambda x: x[1])
    arrowPos = points[0][1]
    arrowCount = 1

    for i in range(1, len(points)):
        if points[i][0] > arrowPos:
            arrowPos = points[i][1]
            arrowCount += 1

    return arrowCount

# Solution-7
def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Solution-8
def find132pattern(nums):
    stack = []
    third = float('-inf')

    for i in range(len(nums)-1, -1, -1):
        if nums[i] < third:
            return True
        while stack and nums[i] > stack[-1]:
            third = max(third, stack.pop())
        stack.append(nums[i])

    return False
