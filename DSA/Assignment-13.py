# Solution-1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNewList(list1, list2):
    ptr1 = list1
    ptr2 = list2
    newList = None
    tail = None

    while ptr1 and ptr2:
        if ptr1.val >= ptr2.val:
            newNode = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            newNode = ListNode(ptr2.val)
            ptr2 = ptr2.next

        if newList is None:
            newList = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    while ptr1:
        newNode = ListNode(ptr1.val)
        tail.next = newNode
        tail = newNode
        ptr1 = ptr1.next

    while ptr2:
        newNode = ListNode(ptr2.val)
        tail.next = newNode
        tail = newNode
        ptr2 = ptr2.next

    return newList


node1 = ListNode(5)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4

list1 = node1

node5 = ListNode(1)
node6 = ListNode(7)
node7 = ListNode(4)
node8 = ListNode(5)

node5.next = node6
node6.next = node7
node7.next = node8

list2 = node5

newList = createNewList(list1, list2)

current = newList
while current:
    # print(current.val, end=" ")
    current = current.next




# Solution-2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeDuplicates(head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head


node1 = ListNode(11)
node2 = ListNode(11)
node3 = ListNode(11)
node4 = ListNode(21)
node5 = ListNode(43)
node6 = ListNode(43)
node7 = ListNode(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

head = node1

head = removeDuplicates(head)

current = head
while current:
    # print(current.val, end=" ")
    current = current.next



# Solution-3
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    if k == 1 or not head:
        return head

    def reverseGroup(prev, curr, k):
        next_node = None
        count = 0

        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        return prev, curr

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        next_group = curr
        for _ in range(k - 1):
            if next_group:
                next_group = next_group.next

        if not next_group:
            break

        prev, curr = reverseGroup(prev, curr, k)

        prev.next = curr

    return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

head = node1

k = 4

head = reverseKGroup(head, k)

current = head
while current:
    # print(current.val, end=" ")
    current = current.next


# Solution-4
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseAlternateKNodes(head, k):
    if k == 1 or not head:
        return head

    def reverseGroup(prev, curr, k):
        next_node = None
        count = 0

        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        return prev, curr

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    reverse = True
    while curr:
        next_group = curr
        for _ in range(k - 1):
            if next_group:
                next_group = next_group.next

        if not next_group:
            break

        if reverse:
            prev, curr = reverseGroup(prev, curr, k)
        else:
            for _ in range(k):
                prev = curr
                curr = curr.next

        reverse = not reverse

        prev.next = curr

    return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

head = node1

k = 3

head = reverseAlternateKNodes(head, k)

current = head


# Solution-6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteLastOccurrence(head, key):
    if not head:
        return None

    prev = None
    last = None
    current = head

    while current:
        if current.val == key:
            last = current
        prev = current
        current = current.next

    if not last:
        return head

    if last == head:
        head = head.next
    else:
        prev.next = last.next

    return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(2)
node6 = ListNode(10)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1

key = 2

head = deleteLastOccurrence(head, key)

current = head



# Solution-6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(a, b):
    dummy = ListNode(0)
    current = dummy

    while a and b:
        if a.val <= b.val:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next

    if a:
        current.next = a
    elif b:
        current.next = b

    return dummy.next


node1 = ListNode(5)
node2 = ListNode(10)
node3 = ListNode(15)
node1.next = node2
node2.next = node3

head_a = node1

node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(20)
node4.next = node5
node5.next = node6

head_b = node4

merged_head = mergeTwoLists(head_a, head_b)

current = merged_head



# Solution-7
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def reverseDLL(head):
    if head is None or head.next is None:
        return head

    current = head
    while current:
        current.prev, current.next = current.next, current.prev

        current = current.prev

    head = current.prev

    return head


node1 = Node(10)
node2 = Node(8)
node3 = Node(4)
node4 = Node(2)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

head = node1

reversed_head = reverseDLL(head)

current = reversed_head
while current:
    print(current.data, end=" ")
    current = current.next



# Solution-8
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def deleteNode(head, position):
    if head is None:
        return head

    if position == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    current = head
    count = 1
    while current and count < position:
        current = current.next
        count += 1

    if current is None:
        return head

    prev_node = current.prev
    next_node = current.next
    if prev_node:
        prev_node.next = next_node
    if next_node:
        next_node.prev = prev_node

    return head


node1 = Node(1)
node2 = Node(5)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

head = node1

new_head = deleteNode(head, 1)

current = new_head
while current:
    # print(current.data, end=" ")
    current = current.next

