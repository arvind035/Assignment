# Solution-1
def arrayPairSum(nums):
    nums.sort()
    maxSum = 0
    for i in range(0, len(nums), 2):
        maxSum += nums[i]
    return maxSum
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
# print(result)

# Solution-2
def maxNumberOfDifferentTypes(candyType):
    uniqueCandies = set()
    for candy in candyType:
        uniqueCandies.add(candy)
    
    maxCandies = min(len(uniqueCandies), len(candyType) // 2)
    return maxCandies
candyType = [1, 1, 2, 2, 3, 3]
result = maxNumberOfDifferentTypes(candyType)
# print(result)

# Solution-3
def findLHS(nums):
    numCounts = {}
    for num in nums:
        numCounts[num] = numCounts.get(num, 0) + 1
    
    maxLength = 0
    for num in numCounts:
        if num + 1 in numCounts:
            maxLength = max(maxLength, numCounts[num] + numCounts[num + 1])
    
    return maxLength
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
# print(result)

# Solution-4
def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
    return count >= n
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
# print(result)

# Solution-5
def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1] * nums[n-1])
nums = [1, 2, 3]
result = maximumProduct(nums)
# print(result)

# Solution-6
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
# print(result)

# Solution-7
def isMonotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
        if not increasing and not decreasing:
            return False

    return True
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
# print(result)

# Solution-8
def minimumScore(nums, k):
    minNum = min(nums)
    maxNum = max(nums)

    if maxNum - minNum <= 2 * k:
        return 0

    return maxNum - k if minNum + k > maxNum - k else minNum + k
nums = [1]
k = 0
result = minimumScore(nums, k)
# print(result)
