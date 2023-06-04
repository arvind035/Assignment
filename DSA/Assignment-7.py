# Solution-1
def isIsomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for ch_s, ch_t in zip(s, t):
        if ch_s not in s_to_t and ch_t not in t_to_s:
            s_to_t[ch_s] = ch_t
            t_to_s[ch_t] = ch_s
        elif s_to_t.get(ch_s) != ch_t or t_to_s.get(ch_t) != ch_s:
            return False

    return True
s = "egg"
t = "add"
# print(isIsomorphic(s, t))

# Solution-2
def isStrobogrammatic(num):
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in mapping or num[right] not in mapping or mapping[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True
num = "69"
# print(isStrobogrammatic(num))

# Solution-3
def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0:
        x = 0 if i < 0 else int(num1[i])
        y = 0 if j < 0 else int(num2[j])
        total = x + y + carry
        result.append(str(total % 10))
        carry = total // 10
        i -= 1
        j -= 1

    if carry > 0:
        result.append(str(carry))

    return ''.join(result[::-1])
num1 = "11"
num2 = "123"
# print(addStrings(num1, num2))

# Solution-4
def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
s = "Let's take LeetCode contest"
# print(reverseWords(s))

# Solution-5
def reverseStr(s, k):
    s_list = list(s)
    n = len(s)
    
    for i in range(0, n, 2 * k):
        start = i
        end = min(i + k, n)
        s_list[start:end] = reversed(s_list[start:end])
    
    return ''.join(s_list)
s = "abcdefg"
k = 2
# print(reverseStr(s, k))

# Solution-6
def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    s_concat = s + s
    if goal in s_concat:
        return True

    return False
s = "abcde"
goal = "cdeab"
# print(rotateString(s, goal))

# Solution-7
def backspaceCompare(s, t):
    def build_stack(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return stack

    return build_stack(s) == build_stack(t)
s = "ab#c"
t = "ad#c"
# print(backspaceCompare(s, t))

# Solution-8
def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    slope = (y2 - y1) / (x2 - x1)

    for i in range(2, len(coordinates)):
        x1, y1 = coordinates[i-1]
        x2, y2 = coordinates[i]

        current_slope = (y2 - y1) / (x2 - x1)

        if current_slope != slope:
            return False

    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# print(checkStraightLine(coordinates))

