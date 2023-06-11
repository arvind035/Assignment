def get_highest_frequency_word_length(string):
    words = string.split()

    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    highest_frequency = max(frequency_dict.values())

    highest_frequency_word_length = 0
    for word, frequency in frequency_dict.items():
        if frequency == highest_frequency:
            word_length = len(word)
            if word_length > highest_frequency_word_length:
                highest_frequency_word_length = word_length

    return highest_frequency_word_length


input_string1 = "write write write all the number from from from 1 to 100"
result1 = get_highest_frequency_word_length(input_string1)
print("Length of the highest-frequency word:", result1)

input_string2 = "apple apple orange orange orange orange orange apple apple apple"
result2 = get_highest_frequency_word_length(input_string2)
print("Length of the highest-frequency word:", result2)

input_string3 = "Hello there, how are you? I hope you are doing well."
result3 = get_highest_frequency_word_length(input_string3)
print("Length of the highest-frequency word:", result3)
