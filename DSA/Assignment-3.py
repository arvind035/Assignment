# Solution-1
def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if abs(currentSum - target) < abs(closest_sum - target):
                closest_sum = currentSum

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return target

    return closest_sum
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
# print(result)

# Solution-2
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[j] + nums[left] + nums[right]

                if currentSum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif currentSum < target:
                    left += 1
                else:
                    right -= 1
    return result
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
# print(result)

# Solution-3
def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1

        while j > i and nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
nums = [1, 2, 3]
nextPermutation(nums)
# print(nums)

# Solution-4
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
# print(result)

# Solution-5
def plusOne(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        else:
            carry = 0
            break
    if carry == 1:
        return [1] + digits
    else:
        return digits
digits = [1, 2, 3]
result = plusOne(digits)
# print(result)

# Solution-6
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result
nums = [2, 2, 1]
result = singleNumber(nums)
# print(result)

# Solution-7
def findMissingRanges(nums, lower, upper):
    result = []

    def addRange(start, end):
        if start == end:
            result.append([start,start])
        else:
            result.append([start,end])

    if lower < nums[0]:
        addRange(lower, nums[0] - 1)

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] + 1:
            addRange(nums[i - 1] + 1, nums[i] - 1)

    if upper > nums[-1]:
        addRange(nums[-1] + 1, upper)

    return result
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
# print(result)

# Solution-8
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
# print(result)
