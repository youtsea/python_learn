from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10.19')
print sub
print sub.addr
print sub.joined

print len(sub)

add, joined = sub

print add
print joined

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares + s.price
    return total

s = [Stock('ACME', 100, 123.45), Stock('ACME', 100, 123.45)]
print compute_cost(s)

s = Stock('ACME', 100, 12.45)
s = s._replace(shares=75)
print s.shares