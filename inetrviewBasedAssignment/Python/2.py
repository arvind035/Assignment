from collections import Counter

def is_valid_string(s):
    char_count = Counter(s)

    freq_count = Counter(char_count.values())

    if len(freq_count) == 1 or (len(freq_count) == 2 and 1 in freq_count.values()):
        return "YES"
    else:
        return "NO"

input_string1 = "abc"
result1 = is_valid_string(input_string1)
print(result1)

input_string2 = "abcc"
result2 = is_valid_string(input_string2)
print(result2)

input_string3 = "aabbcc"
result3 = is_valid_string(input_string3)
print(result3)

input_string4 = "aabbccc"
result4 = is_valid_string(input_string4)
print(result4)
