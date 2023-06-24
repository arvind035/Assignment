# Solution-1
def firstUniqChar(s):
    charCount = {}

    for char in s:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for i, char in enumerate(s):
        if charCount[char] == 1:
            return i

    return -1

s = "leetcode"
result = firstUniqChar(s)
# print(result)

# Solution-2
def maxSubarraySumCircular(nums):
    n = len(nums)

    def kadane(nums):
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum

    maxSum1 = kadane(nums)

    totalSum = sum(nums)
    invertedNums = [-num for num in nums]
    maxSum2 = totalSum + kadane(invertedNums)

    if maxSum2 == totalSum:
        return maxSum1

    return max(maxSum1, maxSum2)

nums = [1, -2, 3, -2]
result = maxSubarraySumCircular(nums)
# print(result)

# Solution-3
def countStudents(students, sandwiches):
    n = len(students)
    count = 0

    while count < n:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            count = 0
        else:
            students.append(students.pop(0))
            count += 1

    return len(students)

# Example usage
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
result = countStudents(students, sandwiches)
# print(result)

# Solution-4
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)
recentCounter = RecentCounter()
# print(recentCounter.ping(1))
# print(recentCounter.ping(100))
# print(recentCounter.ping(3001))
# print(recentCounter.ping(3002))

# Solution-5
def findTheWinner(n: int, k: int) -> int:
    friends = list(range(1, n + 1))
    current = 0

    while len(friends) > 1:
        current = (current + k - 1) % len(friends)

        friends.pop(current)

    return friends[0]
# print(findTheWinner(5, 2))
# print(findTheWinner(6, 5))

# Solution-6
from collections import deque
from typing import List

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    deck.sort()
    n = len(deck)
    result = [0] * n
    queue = deque(range(n))

    for card in deck:
        result[queue.popleft()] = card
        if queue:
            queue.append(queue.popleft())

    return result
# print(deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
# print(deckRevealedIncreasing([1, 1000]))

# Solution-7
from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if self.front:
            return self.front.popleft()
        elif self.back:
            return self.back.popleft()
        else:
            return -1

    def popMiddle(self) -> int:
        if len(self.front) == len(self.back):
            return self.front.pop()
        else:
            return self.back.popleft()

    def popBack(self) -> int:
        if self.back:
            return self.back.pop()
        elif self.front:
            return self.front.pop()
        else:
            return -1

    def _balance(self) -> None:
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())
q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
# print(q.popFront())
# print(q.popMiddle())
# print(q.popMiddle())
# print(q.popBack())
# print(q.popFront())

# Solution-8
from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if len(self.stream) < self.k:
            return False
        elif len(self.stream) > self.k:
            self.stream.popleft()
        return all(x == self.value for x in self.stream)
ds = DataStream(4, 3)
# print(ds.consec(4))
# print(ds.consec(4))
# print(ds.consec(4))
# print(ds.consec(3))
