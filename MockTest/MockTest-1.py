def moveZeroes(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums = [0]
moveZeroes(nums)
print(nums)
