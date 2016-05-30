x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print a(10)
print b(10)

funcs = [lambda x: x + n for n in range(5)]

for f in funcs:
    print f(0)

funcs = [lambda x, n=n: x+n for n in range(5)]

for f in funcs:
    print f(0)