# Solution-1
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

def binaryTreeToDLL(root):
    if root is None:
        return None

    left = binaryTreeToDLL(root.left)

    newNode = DoublyLinkedListNode(root.val)

    if left:
        while left.next:
            left = left.next
        left.next = newNode
        newNode.prev = left

    right = binaryTreeToDLL(root.right)

    if right:
        right.prev = newNode
        newNode.next = right

    return newNode

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

head = binaryTreeToDLL(root)

current = head
while current:
    print(current.val, end=" ")
    current = current.next

# Solution-2
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def flipBinaryTree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    flippedLeft = flipBinaryTree(root.left)
    flippedRight = flipBinaryTree(root.right)

    root.left = flippedRight
    root.right = flippedLeft

    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

flippedTree = flipBinaryTree(root)

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)

inorderTraversal(flippedTree)

# Solution-3
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def printRootToLeafPaths(root):
    if root is None:
        return

    stack = [(root, str(root.val))]
    paths = []

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            paths.append(path)
        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))
        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))

    for path in paths:
        print(path)

root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

printRootToLeafPaths(root)

# Solution-4
def checkSameTree(inorder, preorder, postorder):
    if len(inorder) == 0 or len(preorder) == 0 or len(postorder) == 0:
        return False
    if len(inorder) != len(preorder) or len(inorder) != len(postorder):
        return False
    if len(inorder) == 1 and inorder[0] == preorder[0] and inorder[0] == postorder[0]:
        return True
    if inorder[0] != preorder[0] or inorder[-1] != postorder[-1]:
        return False

    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]

    left_preorder = preorder[1:root_index+1]
    right_preorder = preorder[root_index+1:]

    left_postorder = postorder[:root_index]
    right_postorder = postorder[root_index:-1]

    return checkSameTree(left_inorder, left_preorder, left_postorder) and checkSameTree(right_inorder, right_preorder, right_postorder)

inorder1 = [4, 2, 5, 1, 3]
preorder1 = [1, 2, 4, 5, 3]
postorder1 = [4, 5, 2, 3, 1]
# print(checkSameTree(inorder1, preorder1, postorder1))

inorder2 = [4, 2, 5, 1, 3]
preorder2 = [1, 5, 4, 2, 3]
postorder2 = [4, 1, 2, 3, 5]
# print(checkSameTree(inorder2, preorder2, postorder2))
