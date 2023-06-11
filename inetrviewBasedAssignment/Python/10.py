import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import defaultdict

def count_pos(text):
    words = word_tokenize(text)

    tagged_words = pos_tag(words)

    counts = defaultdict(int)

    for word, pos in tagged_words:
        if pos.startswith('VB'):
            counts['Verbs'] += 1
        elif pos.startswith('NN'):
            counts['Nouns'] += 1
        elif pos == 'PRP' or pos == 'PRP$':
            counts['Pronouns'] += 1
        elif pos.startswith('JJ'):
            counts['Adjectives'] += 1

    return counts

text = "The quick brown fox jumps over the lazy dog."
counts = count_pos(text)
print(counts)