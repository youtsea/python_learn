
p = (4, 5)
x, y = p
print x
print y

data = ['ACME', 50, 91.1, (2016, 05, 16)]
name, shares, price, date = data
print name
print shares
print price
print date
name, shares, price, (year, month, day) = data
print name
print shares
print price
print year
print month
print day

s = 'hello'
a, b, c, d, e = s
print a, b, c, d, e

_, shares, price, _ = data
print shares
print price
