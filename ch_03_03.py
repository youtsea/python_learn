
x = 1234.56789

print format(x, '0.2f')
print format(x, '>10.1f')
print format(x, '<10.1f')
print format(x, '^10.1f')
print format(x, ',')
print format(x, '0,.1f')
print format(x, 'e')
print format(x, '0.2E')
print 'The Value is {:0,.2f}'.format(x)
print '%0.2f' % x
print '%10.1f' % x
print '%-10.1f' % x