import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data)

print json_str

data = json.loads(json_str)

print data

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
    print data

print json.dumps(False)

d = {
    'a': True,
    'b': 'Hello',
    'c': None
}

print json.dumps(d)

s = '{"name": "ACME", "shares": 50, "price": 490.1}'

from collections import OrderedDict

data = json.loads(s, object_pairs_hook=OrderedDict)

print data


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

data = json.loads(s, object_hook=JSONObject)

print data.name
print data.shares
print data.price