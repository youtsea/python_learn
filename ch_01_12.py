words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

from collections import Counter
words_counts = Counter(words)
top_one = words_counts.most_common(10)
print top_one

print words_counts['not']
print words_counts['eyes']

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
	words_counts[word] += 1

print words_counts['eyes']

words_counts.update(morewords)
print words_counts['eyes']

a = Counter(words)
b = Counter(morewords)

c = a + b
print c

d = a - b
print d