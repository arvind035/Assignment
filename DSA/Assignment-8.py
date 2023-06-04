# Solution-1
def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

    return dp[m][n]
s1 = "sea"
s2 = "eat"
# print(minimumDeleteSum(s1, s2))

# Solution-2
def checkValidString(s):
    stack = []
    asterisks = []
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == '*':
            asterisks.append(i)
        else:
            if stack:
                stack.pop()
            elif asterisks:
                asterisks.pop()
            else:
                return False
    
    while stack and asterisks:
        if stack[-1] > asterisks[-1]:
            return False
        stack.pop()
        asterisks.pop()

    return len(stack) == 0
s = "()"
# print(checkValidString(s))

# Solution-3
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]
word1 = "sea"
word2 = "eat"
# print(minDistance(word1, word2))

# Solution-4
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(s):
    if not s:
        return None

    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit() or s[i] == '-':
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                j += 1
            value = int(s[i:j])
            node = TreeNode(value)

            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

            stack.append(node)
            i = j
        elif s[i] == ')':
            stack.pop()
            while stack and stack[-1].right:
                stack.pop()
            i += 1
        else:
            i += 1

    return stack[0] if stack else None

def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

s = "4(2(3)(1))(6(5))"
root = buildTree(s)
result = inorderTraversal(root)
# print(result)

# Solution-5
def compress(chars):
    read = write = 0

    while read < len(chars):
        curr = chars[read]
        count = 1

        while read + 1 < len(chars) and chars[read + 1] == curr:
            read += 1
            count += 1

        chars[write] = curr
        write += 1

        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write] = digit
                write += 1

        read += 1

    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]
length = compress(chars)
# print(length)
# print(chars[:length])

# Solution-6
from collections import Counter

def findAnagrams(s, p):
    freq_p = Counter(p)
    freq_s = Counter()
    left = right = 0
    match_count = 0
    result = []

    while right < len(s):
        if s[right] in freq_p:
            freq_s[s[right]] += 1
            if freq_s[s[right]] == freq_p[s[right]]:
                match_count += 1

        if right - left + 1 == len(p):
            if match_count == len(freq_p):
                result.append(left)

            if s[left] in freq_p:
                if freq_s[s[left]] == freq_p[s[left]]:
                    match_count -= 1
                freq_s[s[left]] -= 1

            left += 1

        right += 1

    return result

s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
# print(indices)

# Solution-7
def decodeString(s):
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append(current_str)
            stack.append(current_num)
            current_str = ""
            current_num = 0
        elif char == "]":
            num = stack.pop()
            prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str

s = "3[a]2[bc]"
decoded = decodeString(s)
# print(decoded)

# Solution-8
def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    differences = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            differences.append(i)

    return len(differences) == 2 and s[differences[0]] == goal[differences[1]] and s[differences[1]] == goal[differences[0]]

s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
# print(result)
