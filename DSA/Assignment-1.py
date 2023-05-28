# Solution-1
def twoIndices(nums, target):
    numDict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numDict:
            return [numDict[complement], i]
        numDict[num] = i
    return []
nums = [2, 7, 11, 15]
target = 9
# print(twoIndices(nums, target))

# Solution-2
def removeElement(nums, val):
    i = j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
# print(k)
# print(nums)


# Solution-3
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
# print(index)

# Solution-4
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

# Solution-5
def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    if p2 >= 0:
        nums1[:p2 + 1] = nums2[:p2 + 1]

    return nums1
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

result = merge(nums1, m, nums2, n)
# print(result)

# Solution-6
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
# print(result)


# Solution-7
def moveZeroes(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[j:] = [0] * (len(nums) - j)
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
# print(nums)

# Solution-8
def findErrorNums(nums):
    xor_sum = 0
    for i, num in enumerate(nums):
        xor_sum ^= num ^ (i + 1)
    
    bit_mask = 1
    while xor_sum & bit_mask == 0:
        bit_mask <<= 1
    
    missing = duplicate = 0
    for num in nums:
        if num & bit_mask:
            missing ^= num
        else:
            duplicate ^= num
    
    for i in range(1, len(nums) + 1):
        if i & bit_mask:
            missing ^= i
        else:
            duplicate ^= i
    
    return [duplicate, missing]
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)





