
data = b'Hello World'

print data[0:5]
print data.startswith(b'Hello')
print data.split()
print data.replace(b'Hello', b'Hello Cruel')

data = bytearray(b'Hello World')
print data[0:5]
print data.split()
print data.replace(b'Hello', b'Hello Cruel')

data = b'FOO:BAR,SPAM'

import re

print re.split(b'[:,]', data)