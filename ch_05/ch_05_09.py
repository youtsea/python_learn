import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')

print buf

buf[0:5] = b'Hallo'

print buf

with open('newsample.bin', 'wb') as f:
    f.write(buf)

record_size = 30
buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        print n

buf = b'Hello World'
m1 = memoryview(buf)
m2 = m1[-5:]

print m2
print m2[:]
print buf
