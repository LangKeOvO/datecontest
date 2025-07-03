from collections import Counter
import string

with open("D:/CODE/datecontest/ttest/Test/sample_test.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = text.lower().translate(str.maketrans("", "", string.punctuation))
words = text.split()

counter = Counter(words)

for word, count in counter.most_common(10):
    print(f"{word}: {count}")
