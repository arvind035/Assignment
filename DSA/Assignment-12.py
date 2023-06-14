# Solution-1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddleNode(head):
    if not head or not head.next:
        return None

    slow = fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return head

head1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

newHead1 = deleteMiddleNode(head1)
current = newHead1
while current:
    print(current.val, end=" ")
    current = current.next

# print()

head2 = ListNode(2)
node4 = ListNode(4)
node6 = ListNode(6)
node7 = ListNode(7)
node5 = ListNode(5)
node1 = ListNode(1)

head2.next = node4
node4.next = node6
node6.next = node7
node7.next = node5
node5.next = node1

newHead2 = deleteMiddleNode(head2)
current = newHead2
while current:
    # print(current.val, end=" ")
    current = current.next

# Solution-2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasLoop(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

head1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(3)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

# print(hasLoop(head1))

head2 = ListNode(1)
node5 = ListNode(8)
node6 = ListNode(3)
node7 = ListNode(4)

head2.next = node5
node5.next = node6
node6.next = node7

# print(hasLoop(head2))

# Solution-3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head, N):
    if not head:
        return -1
    fast = head
    slow = head

    for _ in range(N):
        if not fast:
            return -1
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    if not slow:
        return -1

    return slow.val

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

N = 2
# print(findNthFromEnd(head, N))

N = 5
# print(findNthFromEnd(head, N))

# Solution-4
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next

    return True


head1 = ListNode('R')
node2 = ListNode('A')
node3 = ListNode('D')
node4 = ListNode('A')
node5 = ListNode('R')

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# print(isPalindrome(head1))

head2 = ListNode('C')
node6 = ListNode('O')
node7 = ListNode('D')
node8 = ListNode('E')

head2.next = node6
node6.next = node7
node7.next = node8

# print(isPalindrome(head2))

# Solution-5
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectAndRemoveLoop(head):
    if not head or not head.next:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if slow != fast:
        return

    slow = head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None


head1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(2)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

detectAndRemoveLoop(head1)

current = head1
while current:
    # print(current.val, end=" -> ")
    if not current.next:
        print("None")
        break
    current = current.next


head2 = ListNode(1)
node5 = ListNode(8)
node6 = ListNode(3)
node7 = ListNode(4)

head2.next = node5
node5.next = node6
node6.next = node7

detectAndRemoveLoop(head2)

current = head2
while current:
    # print(current.val, end=" -> ")
    if not current.next:
        print("None")
        break
    current = current.next

# Solution-6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def skipMdeleteN(head, M, N):
    if not head:
        return None

    current = head
    previous = None

    while current:
        mCount = M

        while mCount > 1 and current:
            current = current.next
            mCount -= 1

        if not current:
            break

        previous = current

        nCount = N

        while nCount > 0 and current.next:
            current.next = current.next.next
            nCount -= 1

        current = current.next

    return head


head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

M = 2
N = 2

newHead = skipMdeleteN(head, M, N)

current = newHead
while current:
    # print(current.val, end=" -> ")
    if not current.next:
        # print("None")
        break
    current = current.next

# Solution-7
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeLists(first, second):
    if not second:
        return first

    firstPtr = first
    secondPtr = second

    while firstPtr and secondPtr:
        temp = firstPtr.next

        firstPtr.next = secondPtr
        secondPtr = secondPtr.next
        firstPtr.next.next = temp

        firstPtr = temp

    return first


first = ListNode(5)
node2 = ListNode(7)
node3 = ListNode(17)
node4 = ListNode(13)
node5 = ListNode(11)

first.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

second = ListNode(12)
node6 = ListNode(10)
node7 = ListNode(2)
node8 = ListNode(4)
node9 = ListNode(6)

second.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

mergedList = mergeLists(first, second)

current = mergedList
while current:
    # print(current.val, end=" -> ")
    if not current.next:
        # print("None")
        break
    current = current.next

current = second
while current:
    print(current.val, end=" -> ")
    if not current.next:
        # print("None")
        break
    current = current.next


# Solution-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isCircular(head):
    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

# print(isCircular(node1))

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# print(isCircular(node1))
