
with open('passwd') as f:
    try:
        while True:
            line = next(f)
            print line
    except StopIteration:
        pass

with open('passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print line

items = [1, 2, 3]
it = iter(items)
print next(it)
print next(it)
print next(it)
print next(it)
