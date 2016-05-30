import pickle

data = 'shishixin'
f = open('somefile', 'wb')
pickle.dump(data, f)
s = pickle.dumps(data)

f = open('somefile', 'rb')
data = pickle.loads(f)

print data

data = pickle.loads(s)

print data