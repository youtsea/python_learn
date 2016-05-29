
parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print ' '.join(parts)
print ','.join(parts)
print ''.join(parts)

a = 'Is Chicago'
b = 'Not Chicago?'
print a + ' ' + b
print '{} {}'.format(a,b)

a = 'Hello' 'World'
print a

s = ''
for p in parts:
    s += p

print s

data = ['ACME', 50, 91.1]
print ','.join(str(d) for d in data)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ','.join(sample())
print text
for part in sample():
    print part


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    print part