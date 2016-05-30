
print ','.join(('ACME', '50', '91.5'))

print('ACME', '50', '91.5', spe=',')
print('ACME', '50', '91.5', spe=',', end='!!\n')

for i in range(5):
    print i

for i in range(5):
    print (i, end=' ')

row = ('ACME', '50', '91.5')
print (*row, sep=',')