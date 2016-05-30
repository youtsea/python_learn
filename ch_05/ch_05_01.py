
with open('../passwd' , 'rt') as f:
    data = f.read()
    print data

with open('../passwd', 'rt') as f:
    for line in f:
        print line

with open('somefile.txt', 'wt') as f:
    f.write("111")

with open('../passwd', 'rt', encoding='latin-1') as f:
    print f.read()