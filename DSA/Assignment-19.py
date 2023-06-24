# Solution-1
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    dummy = ListNode(0)
    curr = dummy

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i))

    while min_heap:
        val, idx = heapq.heappop(min_heap)
        node = lists[idx]
        curr.next = node
        curr = curr.next

        if node.next:
            lists[idx] = node.next
            heapq.heappush(min_heap, (node.next.val, idx))

    return dummy.next

# Solution-2
def countSmaller(nums):
    n = len(nums)
    count = [0] * n

    def mergeSort(start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        i, j = start, mid + 1
        rightCount = 0
        merged = []

        while i <= mid and j <= end:
            if nums[j] < nums[i]:
                count[i] += rightCount + 1
                merged.append(nums[j])
                j += 1
            else:
                merged.append(nums[i])
                rightCount += 1
                i += 1

        while i <= mid:
            count[i] += rightCount + 1
            merged.append(nums[i])
            i += 1

        nums[start:start+len(merged)] = merged

    mergeSort(0, n - 1)
    return count

# Solution-3
def partition(nums, start, end):
    pivot = nums[end]
    pivotIndex = start

    for i in range(start, end):
        if nums[i] < pivot:
            nums[i], nums[pivotIndex] = nums[pivotIndex], nums[i]
            pivotIndex += 1

    nums[pivotIndex], nums[end] = nums[end], nums[pivotIndex]
    return pivotIndex

def quicksort(nums, start, end):
    if start < end:
        pivotIndex = partition(nums, start, end)
        quicksort(nums, start, pivotIndex - 1)
        quicksort(nums, pivotIndex + 1, end)

def sortArray(nums):
    quicksort(nums, 0, len(nums) - 1)
    return nums

# Solution-4
def moveZerosToEnd(nums):
    left = right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    while left < len(nums):
        nums[left] = 0
        left += 1

    return nums

# Solution-5
def rearrangeAlternate(nums):
    left = right = 0

    while right < len(nums):
        if nums[right] < 0 and nums[left] > 0:
            temp = nums[right]
            for i in range(right, left, -1):
                nums[i] = nums[i - 1]
            nums[left] = temp
            left += 1
        right += 1

    if left > len(nums) // 2:
        i = left
        j = 1
        while i < len(nums) and j < len(nums):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 2
    else:
        i = len(nums) - 1
        j = len(nums) - 2
        while i >= left and j >= 0:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j -= 2

    return nums

# Solution-6
def mergeSortedArrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Solution-7
def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = []

    for num in nums2:
        if num in set1 and num not in intersection:
            intersection.append(num)

    return intersection

# Solution-8
from collections import defaultdict

def intersection(nums1, nums2):
    frequency = defaultdict(int)
    intersection = []

    for num in nums1:
        frequency[num] += 1

    for num in nums2:
        if frequency[num] > 0:
            intersection.append(num)
            frequency[num] -= 1

    return intersection
