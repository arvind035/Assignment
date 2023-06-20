# Solution-1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLoop(head):
    if head is None or head.next is None:
        return 0

    slowPtr = head
    fastPtr = head
    loopDetected = False

    while slowPtr and fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            loopDetected = True
            break

    if loopDetected:
        slowPtr = head
        while slowPtr.next != fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next

        fastPtr.next = None
        return 1

    return 0

# Solution-2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):
    if head is None:
        return None

    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    carry = 1
    current = head
    while current and carry:
        sum = current.data + carry
        current.data = sum % 10
        carry = sum // 10
        prev = current
        current = current.next

    if carry:
        new_node = Node(carry)
        prev.next = new_node

    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev

    return head

# Solution-3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeLists(a, b):
    if a is None:
        return b
    if b is None:
        return a
    
    result = None

    if a.data <= b.data:
        result = a
        result.bottom = mergeLists(a.bottom, b)
    else:
        result = b
        result.bottom = mergeLists(a, b.bottom)

    return result

def flatten(head):
    if head is None or head.next is None:
        return head
    
    head.next = flatten(head.next)
    head = mergeLists(head, head.next)

    return head

def printList(head):
    current = head
    while current:
        # print(current.data, end=" ")
        current = current.bottom
    # print()

# Example usage
head = Node(5)
head.next = Node(10)
head.next.next = Node(19)
head.next.next.next = Node(28)

head.bottom = Node(7)
head.bottom.bottom = Node(8)
head.bottom.bottom.bottom = Node(30)

head.next.bottom = Node(20)

head.next.next.bottom = Node(22)
head.next.next.next.bottom = Node(35)

head.next.next.bottom.bottom = Node(50)

head.next.next.next.bottom.bottom = Node(40)
head.next.next.next.bottom.bottom.bottom = Node(45)

head = flatten(head)

printList(head)

# Solution-4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def cloneLinkedList(head):
    if head is None:
        return None

    current = head
    while current:
        new_node = Node(current.data)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next

    new_head = head.next
    current = head
    new_current = new_head
    while current:
        current.next = new_current.next
        current = current.next
        if new_current.next:
            new_current.next = new_current.next.next
            new_current = new_current.next

    return new_head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head.random = head.next.next
head.next.random = head.next.next.next
head.next.next.random = head

cloned_head = cloneLinkedList(head)

current = cloned_head
while current:
    # print("Node:", current.data)
    if current.random:
        print("Random Pointer:", current.random.data)
    else:
        print("Random Pointer: None")
    # print()
    current = current.next

# Solution-5
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head

# Solution-6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def leftShiftLinkedList(head, k):
    if not head or not head.next or k == 0:
        return head

    current = head
    for _ in range(k):
        if current.next:
            current = current.next
        else:
            current = head

    new_head = current.next
    current.next = None

    current = new_head
    while current.next:
        current = current.next
    current.next = head

    return new_head

head = ListNode(2)
head.next = ListNode(4)
head.next.next = ListNode(7)
head.next.next.next = ListNode(8)
head.next.next.next.next = ListNode(9)
k = 3
result = leftShiftLinkedList(head, k)
current = result
while current:
    # print(current.val, end=" ")
    current = current.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
k = 4
result = leftShiftLinkedList(head, k)
current = result
while current:
    # print(current.val, end=" ")
    current = current.next

# Solution-7
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    stack = []
    answer = [0] * len(values)

    for i in range(len(values) - 1, -1, -1):
        while stack and values[i] >= stack[-1]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(values[i])

    return answer
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)
result = nextLargerNodes(head)
# print(result)

head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)
result = nextLargerNodes(head)
# print(result)

# Solution-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head
    stack = []
    curr = dummy
    running_sum = 0

    while curr:
        running_sum += curr.val

        if running_sum in stack:
            while stack[-1] != running_sum:
                node = stack.pop()
                del node

            prev = curr
            node = curr.next
            while node != stack[-1]:
                running_sum += node.val
                del node
                node = node.next
                prev.next = node
        else:
            stack.append(running_sum)

        curr = curr.next

    return dummy.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(-3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(1)
result = removeZeroSumSublists(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(4)
result = removeZeroSumSublists(head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(-3)
head.next.next.next.next = ListNode(-2)
result = removeZeroSumSublists(head)
