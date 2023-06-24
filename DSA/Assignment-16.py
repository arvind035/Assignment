# Solution-1
def findNearestGreaterFrequency(arr):
    stack = []
    frequency = {}
    result = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and frequency.get(arr[stack[-1]], 0) <= frequency.get(arr[i], 0):
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(arr[stack[-1]])

        frequency[arr[i]] = frequency.get(arr[i], 0) + 1
        stack.append(i)

    return result[::-1]

# Solution-2
def sortStack(stack):
    tempStack = []

    while stack:
        temp = stack.pop()

        while tempStack and tempStack[-1] > temp:
            stack.append(tempStack.pop())

        tempStack.append(temp)

    while tempStack:
        stack.append(tempStack.pop())

    return stack
stack1 = [34, 3, 31, 98, 92, 23]
# print(sortStack(stack1))

stack2 = [3, 5, 1, 4, 2, 8]
# print(sortStack(stack2))

# Solution-3
def deleteMiddle(stack):
    if not stack:
        return

    middle = len(stack) // 2
    deleteMiddleUtil(stack, middle)

def deleteMiddleUtil(stack, current, index=0):
    if not stack or index == current:
        stack.pop()
        return

    temp = stack.pop()
    deleteMiddleUtil(stack, current, index+1)
    stack.append(temp)
stack1 = [1, 2, 3, 4, 5]
deleteMiddle(stack1)
# print(stack1)

stack2 = [1, 2, 3, 4, 5, 6]
deleteMiddle(stack2)
# print(stack2)

# Solution-4
def checkQueueArrangement(queue):
    stack = []
    secondQueue = []
    expected = 1

    while queue:
        if queue[0] == expected:
            secondQueue.append(queue.pop(0))
            expected += 1
        elif stack and stack[-1] == expected:
            secondQueue.append(stack.pop())
            expected += 1
        else:
            stack.append(queue.pop(0))

    while stack and stack[-1] == expected:
        secondQueue.append(stack.pop())
        expected += 1

    if not stack:
        return "Yes"
    else:
        return "No"
queue1 = [5, 1, 2, 3, 4]
# print(checkQueueArrangement(queue1))

queue2 = [5, 1, 2, 6, 3, 4]
# print(checkQueueArrangement(queue2))

# Solution-5
def reverseNumber(num):
    stack = []
    num_str = str(num)

    for digit in num_str:
        stack.append(int(digit))

    reversed_num = ''
    while stack:
        reversed_num += str(stack.pop())

    reversed_num = int(reversed_num)

    return reversed_num
num1 = 365
# print(reverseNumber(num1))

num2 = 6899
# print(reverseNumber(num2))

# Solution-6
from queue import Queue

def reverseK(queue, k):
    if k <= 0 or k > queue.qsize():
        return queue

    stack = []
    for _ in range(k):
        stack.append(queue.get())

    while not queue.empty():
        queue.put(queue.get())

    while stack:
        queue.put(stack.pop())

    return queue
q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

k = 3
reversed_q = reverseK(q, k)
while not reversed_q.empty():
    print(reversed_q.get(), end=" ")

# Solution-7
def countWordsLeft(sequence):
    stack = []

    for word in sequence:
        if not stack or word != stack[-1]:
            stack.append(word)
        else:
            stack.pop()

    return len(stack)
sequence1 = ['ab', 'aa', 'aa', 'bcd', 'ab']
# print(countWordsLeft(sequence1))

sequence2 = ['tom', 'jerry', 'jerry', 'tom']
# print(countWordsLeft(sequence2))

# Solution-8
def maxAbsoluteDifference(arr):
    n = len(arr)
    leftSmaller = [0] * n
    rightSmaller = [0] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] > arr[i]:
            element = stack.pop()
            rightSmaller[element] = arr[i]

        stack.append(arr[i])

    stack = []

    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            element = stack.pop()
            leftSmaller[element] = arr[i]

        stack.append(arr[i])

    maxDiff = 0

    for i in range(n):
        maxDiff = max(maxDiff, abs(leftSmaller[i] - rightSmaller[i]))

    return maxDiff
arr1 = [2, 1, 8]
# print(maxAbsoluteDifference(arr1))

arr2 = [2, 4, 8, 7, 7, 9, 3]
# print(maxAbsoluteDifference(arr2))

arr3 = [5, 1, 9, 2, 5, 1, 7]
# print(maxAbsoluteDifference(arr3))
