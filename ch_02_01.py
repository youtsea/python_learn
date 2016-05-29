
line = 'asdf fjdk; afed, fjek,asdf,      foo'
import re

print re.split(r'[;,\s]\s*', line)

fields = re.split(r'(;|,|\s)\s*', line)

print fields

values = fields[::2]
print values

delimiters = fields[1::2] + ['']
print delimiters

print ''.join(v+d for v,d in zip(values, delimiters))

print re.split(r'(?:,|;|\s)\s*', line)

