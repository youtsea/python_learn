
filename = 'spam.txt'

print filename.endswith('.txt')
print filename.startswith('file:')

url = 'http://www.python.org'

print url.startswith('http:')

import os
filenames = os.listdir('.')

print filenames
print [name for name in filenames if name.endswith('.py')]
print any(name.endswith('.py') for name in filenames)

choices = ['http:', 'ftp:']
url = 'http://python.org'
url.startswith(tuple(choices))
