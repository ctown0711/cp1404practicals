"""
Word Occurences
Estimate: 15 minutes
Actual: 11 minutes
"""

word_to_count = {}
user_string = input("Text: ").lower().split()
for word in sorted(user_string):
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
format_width = max(len(word) for word in word_to_count)
for word, count in word_to_count.items():
    print(f"{word:{format_width}} : {count}")
