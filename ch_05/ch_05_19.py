from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello World\n')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()
    print data

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print 'filename is:', f.name

with NamedTemporaryFile('w+t', delete=False) as f:
    print 'filename is:', f.name