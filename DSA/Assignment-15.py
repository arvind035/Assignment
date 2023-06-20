# Solution-1
def nextGreaterElements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result
arr = [1, 3, 2, 4]
result = nextGreaterElements(arr)

arr = [6, 8, 0, 1, 3]
result = nextGreaterElements(arr)

# Solution-2
def nearestSmallerElements(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result
arr = [1, 6, 2]
result = nearestSmallerElements(arr)

arr = [1, 5, 0, 3, 4, 5]
result = nearestSmallerElements(arr)

# Solution-3
class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1 and not self.q2:
            return -1

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        if not self.q2:
            return self.q1.pop(0)

        return self.q2.pop(0)
stack = Stack()

stack.push(2)
stack.push(3)
# print(stack.pop())

stack.push(4)
# print(stack.pop())
stack = Stack()

stack.push(2)
# print(stack.pop())
# print(stack.pop())

stack.push(3)
# print(stack.pop())

# Solution-4
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def reverse_stack(self):
        if not self.is_empty():
            temp = self.pop()
            self.reverse_stack()
            self.insert_at_bottom(temp)

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)
stack = Stack()

stack.push(3)
stack.push(2)
stack.push(1)
stack.push(7)
stack.push(6)

# print("Original Stack:", stack.items)

stack.reverse_stack()

# print("Reversed Stack:", stack.items)
stack = Stack()

stack.push(4)
stack.push(3)
stack.push(9)
stack.push(6)

# print("Original Stack:", stack.items)

stack.reverse_stack()

# print("Reversed Stack:", stack.items)
stack = Stack()

stack.push(4)
stack.push(3)
stack.push(9)
stack.push(6)

# print("Original Stack:", stack.items)

stack.reverse_stack()

# print("Reversed Stack:", stack.items)

# Solution-5
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]


def reverse_string(S):
    stack = Stack()

    for char in S:
        stack.push(char)

    reversed_string = ""

    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string
input_string = "GeeksforGeeks"
reversed_string = reverse_string(input_string)
print(reversed_string)

# Solution-6
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()


def evaluate_postfix(S):
    stack = Stack()

    for char in S:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)

    return stack.pop()


def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2


S = "231*+9-"
result = evaluate_postfix(S)
# print(result)

# Solution-7
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
# print(minStack.getMin())
minStack.pop()
# print(minStack.top())
# print(minStack.getMin())

# Solution-8
def trap(height):
    n = len(height)
    left = 0
    right = n - 1
    leftMax = 0
    rightMax = 0
    water = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# print(trap(height))

height = [4, 2, 0, 3, 2, 5]
# print(trap(height))

