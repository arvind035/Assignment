# Solution-1
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorderTraversal(root):
    if root is None:
        return []
    
    return inorderTraversal(root.left) + [root] + inorderTraversal(root.right)

def convertToBST(root):
    values = inorderTraversal(root)
    values.sort(key=lambda x: x.val)
    
    def assignValues(node, values):
        if node is None:
            return
        
        assignValues(node.left, values)
        node.val = values.pop(0).val
        assignValues(node.right, values)
    
    assignValues(root, values)

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

# print("Before conversion:")
# print("Inorder traversal:", [node.val for node in inorderTraversal(root)])

convertToBST(root)

# print("After conversion:")
# print("Inorder traversal:", [node.val for node in inorderTraversal(root)])

# Solution-2
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def findLCA(root, node1, node2):
    if root is None:
        return None

    if root.val > node1 and root.val > node2:
        return findLCA(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return findLCA(root.right, node1, node2)
    else:
        return root

def findDistance(root, node, distance):
    if root is None:
        return 0

    if root.val == node:
        return distance

    if root.val > node:
        return findDistance(root.left, node, distance + 1)
    else:
        return findDistance(root.right, node, distance + 1)

def distanceBetweenNodes(root, node1, node2):
    lca = findLCA(root, node1, node2)
    distance1 = findDistance(lca, node1, 0)
    distance2 = findDistance(lca, node2, 0)

    return distance1 + distance2

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

node1 = 6
node2 = 14

# print("The distance between the two keys:", distanceBetweenNodes(root, node1, node2))

# Solution-3
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

def binaryTreeToDoublyLinkedList(root):
    if root is None:
        return None

    head = DoublyLinkedListNode(None)
    tail = DoublyLinkedListNode(None)

    convertToDoublyLinkedList(root, head, tail)

    head = head.next
    tail = tail.prev

    head.prev = None
    tail.next = None

    return head

def convertToDoublyLinkedList(node, head, tail):
    if node is None:
        return

    convertToDoublyLinkedList(node.left, head, tail)

    new_node = DoublyLinkedListNode(node.val)

    if head.next is None:
        head.next = new_node
        tail.prev = new_node
    else:
        tail.prev.next = new_node
        new_node.prev = tail.prev
        tail.prev = new_node
        new_node.next = tail

    convertToDoublyLinkedList(node.right, head, tail)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

doubly_linked_list_head = binaryTreeToDoublyLinkedList(root)

current = doubly_linked_list_head
while current is not None:
    print(current.val, end=" ")
    current = current.next

# Solution-4
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

def connectNodesAtSameLevel(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        size = len(queue)

        for i in range(size):
            node = queue.pop(0)

            if i < size - 1:
                node.next = queue[0]

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

connectNodesAtSameLevel(root)

current = root
while current is not None:
    node = current
    while node is not None:
        if node.next is None:
            print(node.val, "→ -1")
        else:
            print(node.val, "→", node.next.val)
        node = node.next
    current = current.left

