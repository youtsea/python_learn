s = '{name} has {n} messages.'

print s.format(name='Guido', n=37)

name = 'Guido'
n = 37
s = '%(name)s has %(n)s messages.'

print s % vars()