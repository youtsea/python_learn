from itertools import chain

a = [1, 2, 3]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print x