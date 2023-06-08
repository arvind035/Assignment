# Solution-1
def isPowerOfThree(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(-1))

# Solution-2
def lastRemaining(n):
    left = 1
    right = n
    while left < right:
        length = right - left + 1
        left += length // 2
        if length % 2 == 1:
            right -= length // 2
    return left

print(lastRemaining(9))
print(lastRemaining(1))

# Solution-3
def subsets(set):
    result = []

    def generateSubsets(subset, remaining, index):
        if index == len(remaining):
            result.append(subset)
            return

        generateSubsets(subset + remaining[index], remaining, index + 1)
        generateSubsets(subset, remaining, index + 1)

    generateSubsets("", set, 0)
    return result

print(subsets("abc"))
print(subsets("abcd"))
# Solution-4
def calculateLength(string):
    if string == "":
        return 0
    return 1 + calculateLength(string[1:])

print(calculateLength("abcd"))
print(calculateLength("GEEKSFORGEEKS"))

# Solution-5
def countContiguousSubstrings(S):
    count = 0
    prev = None
    
    for c in S:
        count += 1
        if prev == c:
            count += prev
        prev = c
    
    return count
print(countContiguousSubstrings("abcab"))
print(countContiguousSubstrings("aba"))

# Solution-6
def towerOfHanoi(N, source, destination, auxiliary):
    if N == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1

    moves = 0

    moves += towerOfHanoi(N-1, source, auxiliary, destination)
    print("move disk", N, "from rod", source, "to rod", destination)
    moves += 1
    moves += towerOfHanoi(N-1, auxiliary, destination, source)

    return moves

N = 2
total_moves = towerOfHanoi(N, 1, 3, 2)
print("Total moves:", total_moves)

N = 3
total_moves = towerOfHanoi(N, 1, 3, 2)
print("Total moves:", total_moves)

# Solution-7
def permute(str, prefix):
    if len(str) == 0:
        print(prefix)
        return

    for i in range(len(str)):
        ch = str[i]
        remaining = str[:i] + str[i+1:]
        permute(remaining, prefix + ch)

str = "cd"
permute(str, "")

str = "abb"
permute(str, "")

# Solution-8
def count_consonants(string):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()

    for ch in string:
        if ch.isalpha() and ch not in vowels:
            count += 1

    return count

string = "abc de"
print(count_consonants(string))

string = "geeksforgeeks portal"
print(count_consonants(string))


