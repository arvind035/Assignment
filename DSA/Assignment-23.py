# Solution-1
def calculateDepth(preorder):
    max_depth = 0
    current_depth = 0

    for char in preorder:
        if char == 'n':
            current_depth += 1
        elif char == 'l':
            max_depth = max(max_depth, current_depth)
            current_depth = 0

    return max_depth

preorder = 'nlnll'
# print(calculateDepth(preorder))

# Solution-2
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printLeftView(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.popleft()

            if i == 0:
                print(node.value, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

root = Node(4)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(1)
root.right.left.left = Node(6)
root.right.left.right = Node(7)

printLeftView(root)

# Solution-3
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printRightView(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)

        for i in range(size):
            node = queue.popleft()

            if i == size - 1:
                print(node.value, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)

printRightView(root)

# Solution-4
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printBottomView(root):
    if root is None:
        return

    queue = deque()
    horizontal_distances = {}
    queue.append((root, 0))

    while queue:
        node, horizontal_distance = queue.popleft()
        horizontal_distances[horizontal_distance] = node.value

        if node.left:
            queue.append((node.left, horizontal_distance - 1))
        if node.right:
            queue.append((node.right, horizontal_distance + 1))

    sorted_distances = sorted(horizontal_distances.items(), key=lambda x: x[0])
    for _, value in sorted_distances:
        print(value, end=' ')

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

# print(BottomView(root))

