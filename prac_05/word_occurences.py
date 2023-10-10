"""
Word Occurences
Estimate: 15 minutes
Actual: 11 minutes
"""

word_to_count = {}
user_string = input("Text: ").lower().split()
for word in user_string:
    try:
        word_to_count[word] = word_to_count[word] + 1
    except KeyError:
        word_to_count[word] = 1
print(word_to_count)
words = sorted(list(word_to_count.keys()))
for word in words:
    print(f"{word} : {word_to_count[word]}")