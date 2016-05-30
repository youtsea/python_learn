from itertools import dropwhile

with open('passwd') as f:
    for line in dropwhile(lambda  line: line.startswith('pass'), f):
        print line

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print x

with open('passwd') as f:
    while True:
        line = next(f, '')
        if not line.startswith('pass'):
            break
    while line:
        print line
        line = next(f, None)

with open('passwd') as f:
    lines = (line for line in f if not line.startswith('pass'))
    for line in lines:
        print line