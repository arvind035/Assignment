# Solution-1
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findMaxSubtreeSum(root):
    if root is None:
        return 0
    
    curr_sum = root.value + findMaxSubtreeSum(root.left) + findMaxSubtreeSum(root.right)
    
    if findMaxSubtreeSum.max_sum is None or curr_sum > findMaxSubtreeSum.max_sum:
        findMaxSubtreeSum.max_sum = curr_sum
    
    return curr_sum

def createBinaryTree(arr, index):
    if index < len(arr):
        if arr[index] is None:
            return None
        root = Node(arr[index])
        root.left = createBinaryTree(arr, 2 * index + 1)
        root.right = createBinaryTree(arr, 2 * index + 2)
        return root

arr1 = [1, 2, 3, 4, 5, 6, 7]
root1 = createBinaryTree(arr1, 0)
findMaxSubtreeSum.max_sum = None
max_sum1 = findMaxSubtreeSum(root1)
# print("Maximum subtree sum:", max_sum1)

arr2 = [1, -2, 3, 4, 5, -6, 2]
root2 = createBinaryTree(arr2, 0)
findMaxSubtreeSum.max_sum = None
max_sum2 = findMaxSubtreeSum(root2)
# print("Maximum subtree sum:", max_sum2)

# Solution-2
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def constructBST(level_order):
    if not level_order:
        return None
    
    root = Node(level_order[0])
    queue = [root]
    i = 1

    while i < len(level_order):
        current_node = queue.pop(0)
        
        left_val = level_order[i]
        if left_val != -1:
            left_node = Node(left_val)
            current_node.left = left_node
            queue.append(left_node)
        
        i += 1
        
        if i < len(level_order):
            right_val = level_order[i]
            if right_val != -1:
                right_node = Node(right_val)
                current_node.right = right_node
                queue.append(right_node)
            
            i += 1

    return root

def printLevelOrder(root):
    if root is None:
        return
    
    queue = [root]
    while queue:
        level_nodes = len(queue)
        while level_nodes > 0:
            node = queue.pop(0)
            print(node.value, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            level_nodes -= 1
        print()

level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(level_order)
# print("BST:")
printLevelOrder(root)

# Solution-3
def isLevelOrderBST(level_order):
    if not level_order:
        return "No"
    
    n = len(level_order)
    stack = []
    root = float('inf')
    
    for i in range(n):
        if level_order[i] < root:
            return "No"
        
        while stack and level_order[i] > stack[-1]:
            root = stack.pop()
            
        stack.append(level_order[i])
        
    while stack:
        if stack.pop() < root:
            return "No"
    
    return "Yes"

level_order1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
level_order2 = [11, 6, 13, 5, 12, 10]

# print("Output1:", isLevelOrderBST(level_order1))
# print("Output2:", isLevelOrderBST(level_order2))
